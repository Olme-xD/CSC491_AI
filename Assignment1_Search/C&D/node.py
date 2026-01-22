class node:
    parent: object
    left_child: object
    right_child: object

    def __init__(self, parent=None, left_child=None, right_child=None):
        if not isinstance(parent, object) or not isinstance(left_child, object) or not isinstance(right_child, object):
            raise TypeError("parent, left_child, and right_child must be objects")
        
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def get_parent(self):
        return self.parent
    
    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    
    def set_parent(self, parent):
        if not isinstance(parent, object):
            raise TypeError("parent must be an object")
        self.parent = parent

    def set_left_child(self, left_child):
        if not isinstance(left_child, object):
            raise TypeError("left_child must be an object")
        self.left_child = left_child

    def set_right_child(self, right_child):
        if not isinstance(right_child, object):
            raise TypeError("right_child must be an object")
        self.right_child = right_child