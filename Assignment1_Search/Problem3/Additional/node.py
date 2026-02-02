class node:
    name: str
    edges: dict # edges is a dictionary of {node: cost}
    h: int

    def __init__(self, name, h=0):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(h, int) or h < 0:
            raise ValueError("Heuristic must be a non-negative integer")
        
        self.name = name
        self.h = h
        self.edges = {}
    
    def get_name(self):
        return self.name
    
    def set_edges(self, edges: dict):
        if not isinstance(edges, dict):
            raise ValueError("Edges must be a dictionary")
        self.edges = edges
    
    def get_edges(self):
        return self.edges
    
    def set_h(self, h: int):
        self.h = h

    def get_h(self):
        return self.h
    
    def __lt__(self, other):
        return self.h < other.h
    