import weakref
from collections import deque

from contrib.data_structures.exceptions import AdjacencyListError


__all__ = (
    "ListIndex",
    "AdjacencyList"
)

class ListIndex:
    __slots__ = ("index")

    def __init__(self):
        self.index = weakref.WeakValueDictionary()

    def add(self, key, value):
        self[key] = value

    def get(self, key):
        return self[key]()

    def remove(self, key):
        del self[key]

class AdjacencyList:
    """
    An Adjacency List enables you to do O(1) lookups of a Node, have disjointed "trees" that you
    can start from any Node, etc.
    """
    __slots__ = ("data", "index")

    def __init__(self):
        self.data = {}
        self.index = weakref.WeakValueDictionary()

    def add(self, node):
        self.data[node] = node.children
        self.index[node.name] = node

        if node.has_children():
            for child in node.children:
                self.add(child)

    def children(self, node, layers=1000, search="BFS"):
        """
        Returns every child of the provided node
        """
        visited = set()
        next = deque([node])

        while next and layers > 0:
            layers -= 1
            current = next.popleft()
            if current in visited:
                continue
            visited.add(current)
            children = set(self.data[current])
            if search == "BFS":
                next.extend(children - visited)
            elif search == "DFS":
                next.extendleft(children - visited)
            else:
                raise AdjacencyListError("Search of AdjacencyList must be BFS or DFS")

        visited.remove(node)
        return list(visited)
    
    def get_node_by_name(self, name):
        if name in self.index:
            return self.index[name]()