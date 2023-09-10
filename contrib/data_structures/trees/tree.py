import weakref
from collections import deque

from contrib.data_structures.exceptions import TreeError
from contrib.data_structures.general import Node
from contrib.data_structures.trees.factory import NodeFactory


__all__ = (
    "Tree",
    "BehaviorTree"
)

class BaseTree:
    """
    A Tree holds Nodes. There are many different types of Trees, and this class is a base for each.
    """
    __slots__ = ("name", "root")

    def __init__(self, name, root=None):
        self.name = name
        if root and issubclass(root.__class__, Node):
            self.root = root
        elif root:
            raise TreeError("Root of a Tree must be a Node type")

    def __call__(self):
        self.root()

    @property
    def type(self):
        return self.__class__.__name__
    
class Tree(BaseTree):
    pass

class BehaviorTree(Tree):
    def create_root(self, cls, **kwargs):
        self.root = NodeFactory.create_node(cls, **kwargs)
        # override parent if it was set
        self.root.parent = None
