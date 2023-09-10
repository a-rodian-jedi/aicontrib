from contrib.data_structures.exceptions import NodeError


class NodeFactory:
    def __new__(cls):
        raise TypeError("NodeFactory is a static class and cannot be instantiated.")

    @staticmethod
    def create_node(cls, **kwargs):
        return cls(**kwargs)
