class node:
    left = None
    right = None

    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def get_leftChild(self):
        return self.left
    
    def get_rightChild(self):
        return self.right
    
    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right