class node:
    def __init__(self, board):
        self.board = board
        self.children = []
    
    def get_board(self):
        return self.board
    
    def set_board(self, board):
        self.board = board
    
    def get_children(self):
        return self.children
    
    def set_children(self, children):
        self.children = children
    