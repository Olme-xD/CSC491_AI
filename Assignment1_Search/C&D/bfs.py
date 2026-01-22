from collections import deque
import node

class bfs(node.node):
    def __init__(self):
        pass

    def search(self, matrix, start, goal):
        queue = deque()
        visited = []

