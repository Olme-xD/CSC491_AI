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

        # Show organize visited nodes
        final_set: str = ""
        for node in visited:
            final_set += node.get_name() + " -> "
        return print(final_set[:-4]) # Remove the last arrow