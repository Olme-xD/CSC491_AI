class node:
    left: object
    right: object
    name: str

    def __init__(self, name="node", left=None, right=None):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be a string")  
        
        if left is not None or not isinstance(left, node) and right is not None or not isinstance(right, node):
            self.left = left
            self.right = right
        else:
            raise ValueError("Left and Right must be node objects or None")
    
    def get_name(self):
        return self.name

    def get_leftChild(self):
        return self.left
    
    def get_rightChild(self):
        return self.right
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.name = name

    def set_left(self, left):
        if not isinstance(left, object):
            raise TypeError("Left must be an object")
        self.left = left

    def set_right(self, right):
        if not isinstance(right, object):
            raise TypeError("Right must be an object")
        self.right = right