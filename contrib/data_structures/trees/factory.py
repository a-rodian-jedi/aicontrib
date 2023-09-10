from contrib.data_structures.general import Node
from contrib.data_structures.exceptions import NodeError


class NodeFactory:
    def __new__(cls):
        raise TypeError("NodeFactory is a static class and cannot be instantiated.")

    @staticmethod
    def create_node(cls, **kwargs):
        if not issubclass(cls, Node):
            raise NodeError("NodeFactory can only create Node subclasses.")

        return cls(kwargs)
