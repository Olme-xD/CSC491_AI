import node

class dfs(node.node):
    def __init__(self):
        pass

    def search(self, start_node, goal_node):
        stack = []
        visited = []

        stack.append(start_node)
        while stack:
            current_node = stack.pop()
            visited.append(current_node)

            # Check if the current node is the goal node
            if current_node == goal_node:
                break
            else:
                parent_node = current_node
                
                # Check if right child exists before adding to stack
                right_child = parent_node.get_rightChild()
                if right_child is not None:
                    stack.append(right_child)
                
                # Check if left child exists before adding to stack
                left_child = parent_node.get_leftChild()
                if left_child is not None:
                    stack.append(left_child)

        # Show organized visited nodes
        final_visited: str = ""
        for node in visited:
            final_visited += node.get_name() + " -> "
        print("DFS Visited: " + final_visited[:-4]) # Remove the last arrow

        # Start to add path nodes to final set
        final_path: str = ""
        visited_reverse = visited[::-1]
        final_path += visited_reverse[0].get_name() + " >- "
        prev_node = visited_reverse[0]

        # Trace back the path from goal to start using parent references
        for node in visited_reverse:
            if node.get_leftChild() == prev_node or node.get_rightChild() == prev_node:
                final_path += node.get_name() + " >- "
                prev_node = node

        final_path = final_path[:-4]  # Remove the last arrow
        final_path = final_path[::-1]  # Reverse the string to get correct order
        print("DFS Path: " + final_path)
        return