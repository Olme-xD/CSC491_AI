class node:
    name: str
    parent: object
    left: object
    right: object

    def __init__(self, name="node", parent=None, left=None, right=None):
        if not isinstance(name, str) and not isinstance(left, node) and not isinstance(right, node):
            raise ValueError("Invalid parameters for node initialization")
        
        self.name = name
        self.parent = parent
        self.left = left
        self.right = right
    
    def get_name(self):
        return self.name
    
    def get_parent(self):
        return self.parent

    def get_leftChild(self):
        return self.left
    
    def get_rightChild(self):
        return self.right
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.name = name

    def set_parent(self, parent):
        if not isinstance(parent, object):
            raise TypeError("Parent must be an object")
        self.parent = parent

    def set_left(self, left):
        if not isinstance(left, object):
            raise TypeError("Left must be an object")
        self.left = left

    def set_right(self, right):
        if not isinstance(right, object):
            raise TypeError("Right must be an object")
        self.right = right