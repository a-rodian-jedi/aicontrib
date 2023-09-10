from contrib.data_structures.exceptions import NodeError


_NODE_CLASSES = ['Node', 'Condition', 'Action', 'Selector', 'Sequence', 'Inverter']

class NodeFactory:
    def __new__(cls):
        raise TypeError("NodeFactory is a static class and cannot be instantiated.")

    @staticmethod
    def create_node(cls, **kwargs):
        if cls.__name__ not in _NODE_CLASSES:
            raise NodeError("NodeFactory can only create Node subclasses.")

        return cls(kwargs)
