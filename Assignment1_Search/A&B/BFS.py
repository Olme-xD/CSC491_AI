import Assignment1_Search.node as node

class BFS(node):
    def __init__(self):
        pass

    def search(self, start_node, goal_node):
        from collections import deque

        on_queue = deque()
        visited = set()

        on_queue.append(start_node)
        while on_queue:
            current_node = on_queue.pop()
            if current_node == goal_node:
                visited.add(current_node)
                return True
            
            left_child = current_node.get_letfChild()
            right_child = current_node.get_rightChild()
            on_queue.append(left_child)
            on_queue.append(right_child)

            if left_child == goal_node:
                visited.add(left_child)
                return True

