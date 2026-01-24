class node:
    name: str
    parent: object
    left: object
    right: object

    def __init__(self, name='', parent=None, left=None, right=None):
        self.name = name
        self.parent = parent
        self.left = left
        self.right = right

    def get_name(self):
        return self.name
    
    def get_parent(self):
        return self.parent
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_name(self, name):
        self.name = name

    def set_parent(self, parent):
        self.parent = parent
    
    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right
