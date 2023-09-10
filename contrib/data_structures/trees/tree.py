import weakref
from collections import deque

from contrib.data_structures.exceptions import TreeError
from contrib.data_structures.general.node import Node


class BaseTree:
    """
    A Tree holds Nodes. There are many different types of Trees, and this class is a base for each.
    """
    __slots__ = ("name", "root")

    def __init__(self, name, root):
        self.name = name
        if issubclass(root.__class__, Node):
            self.root = root
        else:
            raise TreeError("Root of a Tree must be a Node type")

    def __call__(self):
        self.root()

    def add(self):
        raise NotImplementedError

    def children(self):
        raise NotImplementedError

    @property
    def type(self):
        return self.__class__.__name__
    
class Tree(BaseTree):
    def add(self, node):
        pass

    def children(self):
        pass
