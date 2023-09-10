import types

from contrib.data_structures.exceptions import *
from contrib.data_structures.general import Node


__all__ = (
    "Condition",
    "Action",
    "Selector",
    "Sequence",
    "Inverter"
)

class Condition(Node):
    __slots__ = ("name", "parent", "children", "data", "check", "__weakref__")

    def __init__(self, name, check):
        self.check = check
        super().__init__(name)

    def __call__(self):
        return self.succeeds()

    def succeeds(self):
        if type(self.check) is list:
            return all(self._process_list())
        elif type(self.check) is types.FunctionType:
            return self.check()
        elif type(self.check) is bool:
            return self.check
        elif type(self.check) is dict:
            return all(self._process_dict())
        else:
            # last effort, it could be another Behavior node
            return self.check()

    def fails(self):
        return not self.succeeds()

    def _process_list(self):
        out = []
        for check in self.check:
            if type(check) is types.FunctionType:
                out.append(check())
            elif type(check) is dict:
                out.append(all(self._process_dict(check)))
            elif type(check) is bool:
                out.append(check)
            else:
                out.append(self.check())

        return out

    def _process_dict(self):
        out = []
        result = None
        for check_key, check_value in self.check.items():
            if type(check_key) is types.FunctionType:
                result = check_key() == check_value
            elif type(check_key) is bool:
                result = check_key == check_value
            else:
                result = check_key() == check_value

            out.append(result)
            result = None

class Action(Node):
    """
    An Action is a node responsible for performing an action. It can only take a function object.
    """
    __slots__ = ("name", "parent", "children", "data", "func", "__weakref__")

    def __init__(self, name, func, parent=None, children=None, data=None):
        if type(func) is not types.FunctionType:
            raise InvalidAction("Action node must receive a function object")

        self.func = func
        super().__init__(name, parent, children, data)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def add_child(self, node):
        raise ActionError("An Action node cannot have children")

class IterNode(Node):
    __slots__ = ("name", "parent", "children", "data", "current")

    def __init__(self, name, parent=None, children=None, data=None):
        self.current = 0

        super().__init__(name, parent, children, data)

    def __call__(self):
        raise NotImplementedError

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.children):
            self.current = 0
            raise StopIteration
        else:
            self.current += 1
            action = self.children[self.current - 1]
            return (action(), action)
        
    def __len__(self):
        return len(self.children)

    @property
    def remaining(self):
        return len(self.children) - self.current

class Selector(IterNode):
    """
    A Selector continues processing its children nodes until it reaches a success. If any nodes
    succeeds, the Selector succeeds.
    """
    __slots__ = ("name", "parent", "children", "data", "current", "__weakref__")

    def __call__(self):
        for action in self:
            if True in action:
                self.current = 0
                return True

        return False

class Sequence(IterNode):
    """
    A Sequence processes its children nodes until it reaches a failure. If any node fails, the
    Sequence fails. If all succeed, the Sequence succeeds.
    """
    __slots__ = ("name", "parent", "children", "data", "current", "__weakref__")

    def __call__(self):
        for action in self:
            if False in action:
                self.current = 0
                # debug here to find which action failed
                return False
        
        return True

class Inverter(Node):
    """
    An Inverter takes a result from another Node and inverts to response. True to False, False to True.
    An Inverter can only have a single child.
    """
    def __init__(self, name, children, parent=None, data=None):
        if len(children) != 1:
            raise InvalidInverter("An Inverter takes exactly one child")
        
        super().__init__(name, parent, children, data)

    def __call__(self):
        return not self.children[0]()