from collections import deque
import node

class bfs(node.node):
    def __init__(self):
        pass

    def search(self, start_node, goal_node):
        queue = deque()
        visited = []

        queue.append(start_node)
        while queue:
            current_node = queue.popleft()
            visited.append(current_node)

            # Check if the current node is the goal node
            if current_node == goal_node:
                break
            else:
                parent_node = current_node
                
                # Check if left child exists before adding to queue
                left_child = parent_node.get_leftChild()
                if left_child is not None:
                    queue.append(left_child)

                # Check if right child exists before adding to queue
                right_child = parent_node.get_rightChild()
                if right_child is not None:
                    queue.append(right_child)

        # Show path from start to goal
        return print(self.get_path(visited, start_node, goal_node))
    
    def get_path(self, visited, start, goal):
        path = []

        while visited:
            visited_reversed = visited[::-1]
            for node in visited_reversed:
                path.append(node.get_)
                if node == start:
                    return path
            