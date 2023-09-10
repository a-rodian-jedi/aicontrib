from enum import Enum


__all__ = (
    "Node",
    "NgonNode"
)

class Node:
    __slots__ = ("name", "parent", "_data")
    separator = "/"

    def __init__(self, name, parent=None, data=None):
        self.name = name
        self.parent = parent
        self._data = data

    def __call__(self):
        raise NotImplementedError
    
    def is_root(self):
        return self.parent is None

    @property
    def data(self, value=None):
        if value and value in self._data:
            return self._data[value]
        elif value:
            return None
        else:
            return self._data
    
    @data.setter
    def data(self, v1, v2=None):
        if v2:
            self._data[v1] = v2
        else:
            self._data = v1
    
    @property
    def type(self):
        return self.__class__.__name__

class NgonNode(Node):
    __slots__ = ("name", "parent", "children", "_data")

    def __init__(self, name, parent=None, children=None, data=None):
        if children:
            self.children = children
        else:
            self.children = []

        super().__init__(name, parent, data)

    def __call__(self):
        for child in self.children:
            result = child()
            if result:
                continue
            else:
                return (result, child.name)

    def __repr__(self):
        children = "::".join([child.name for child in self.children])
        if self.is_root():
            return f'Node("{self.name}{self.separator}{children}") root'
        else:
            return f'Node("{self.name}{self.separator}{children}") parent="{self.parent.name}"'

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

        return node

    def add_children(self, nodes):
        for node in nodes:
            self.add_child(node)

    def is_leaf(self):
        return len(self.children) == 0

    def has_children(self):
        return len(self.children) > 0
        