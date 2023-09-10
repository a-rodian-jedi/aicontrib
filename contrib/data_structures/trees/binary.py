from queue import Queue


__all__ = (
    "BinaryTree",
    "BinarySearchTree",
    "LoadedBST"
)

class BinaryTree:
    __slots__ = ("value", "left", "right", "__weakref__")

    def __init__(self, value):
       self.value = value
       self.left = None
       self.right = None 

    def insert_left(self, value):
        if self.left:
            new = BinaryTree(value)
            new.left = self.left
            self.left = new
        else:
           self.left = BinaryTree(value)

    def insert_right(self, value):
        if self.right:
            new = BinaryTree(value)
            new.right = self.right
            self.right = new
        else:
            self.right = BinaryTree(value)

    def pre_order(self, func):
        func(self.value)

        if self.left:
            self.left.pre_order(func)

        if self.right:
            self.right.pre_order(func)

    def in_order(self, func):
        if self.left:
            self.left.in_order(func)

        func(self.value)

        if self.right:
            self.right.in_order(func)

    def post_order(self, func):
        if self.left:
            self.left.post_order(func)

        if self.right:
            self.right.post_order(func)

        func(self.value)

    def bfs(self, func):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current = queue.get()
            func(current.value)

            if current.left:
                queue.put(current.left)

            if current.right:
                queue.put(current.right)

class BinarySearchTree:
    __slots__ = ("value", "left", "right", "__weakref__")

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def clear_node(self):
        self.value = None
        self.left = None
        self.right = None

    def find_minimum(self):
        if self.left:
            return self.left.find_minimum()
        else:
            return self.value

    def insert_node(self, value):
        if value <= self.value and self.left:
            self.left.insert_node(value)
        elif value <= self.value:
            self.left = BinarySearchTree(value)
        elif value > self.value and self.right:
            self.right.insert_node(value)
        else:
            self.right = BinarySearchTree(value)

    def has_value(self, value):
        if value < self.value and self.left:
            return self.left.has_value(value)
        if value > self.value and self.right:
            return self.right.has_value(value)
        
        return value == self.value
    
    def find_node(self, value):
        if value < self.value and self.left:
            return self.left.find_node(value)
        if value > self.value and self.right:
            return self.right.find_node(value)
        
        if value == self.value:
            return self
    
    def remove_node(self, value, parent):
        if value < self.value and self.left:
            return self.left.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right:
            return self.right.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            # if we are a left leaf
            if self.left is None and self.right is None and self == parent.left:
                # set parent.left to None (that's us)
                parent.left = None
                self.clear_node()
            # if we are a right leaf
            elif self.left is None and self.right is None and self == parent.right:
                parent.right = None
                self.clear_node()
            # if we are left, have a left child, and no right
            elif self.left and self.right is None and self == parent.left:
                parent.left = self.left
                self.clear_node()
            # if we are right, have a left child, and no right
            elif self.left and self.right is None and self == parent.right:
                parent.right = self.right
                self.clear_node()
            # if we are left, have a right child, and no left
            elif self.right and self.left is None and self == parent.left:
                parent.left = self.left
                self.clear_node()
            # if we are right, have a right child, and no left
            elif self.right and self.left is None and self == parent.right:
                parent.right = self.right
                self.clear_node()
            # if we have left and right children
            else:
                # find smallest value and set our self.value to it
                self.value = self.right.find_minimum()
                # remove smallest node (we swap places)
                self.right.remove_node(self.value, self)

            return True
        
class LoadedBST(BinarySearchTree):
    __slots__ = ("value", "left", "right", "_data", "__weakref__")

    def __init__(self, value, data):
        self.value = value
        self.left = None
        self.right = None
        self._data = data

    def clear_node(self):
        self.value = None
        self.left = None
        self.right = None
        self._data = None