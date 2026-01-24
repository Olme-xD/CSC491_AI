import node

class dls(node.node):

    def __init__(self):
        pass

    def generate_tree_from_matrix(self, matrix, matrix_start, matrix_end):
        node_set = []
        current_node = matrix_start

        # Get traversable neighbors (up, down, left, right)
        neighbors = []
        current_x, current_y = current_node
        try: neighbors.append((current_x, current_y + 1)) if current_x >= 0 and (current_y + 1) >= 0 and matrix[current_x][current_y + 1] == 1 else None
        except IndexError: pass
        try: neighbors.append((current_x, current_y - 1)) if current_x >= 0 and (current_y - 1) >= 0 and matrix[current_x][current_y - 1] == 1 else None
        except IndexError: pass
        try: neighbors.append((current_x + 1, current_y)) if (current_x + 1) >= 0 and current_y >= 0 and matrix[current_x + 1][current_y] == 1 else None
        except IndexError: pass
        try: neighbors.append((current_x - 1, current_y)) if (current_x - 1) >= 0 and current_y >= 0 and matrix[current_x - 1][current_y] == 1 else None
        except IndexError: pass

        # Create node with left and right children
        left_child = neighbors[0] if len(neighbors) > 0 else None
        right_child = neighbors[1] if len(neighbors) > 1 else None
        node_set.append(node.node(name=str(current_node), parent=None, left=left_child, right=right_child))

        # Traverse the tree from start node
        stack = []
        visited = []
        index = 1 # Start from 1 because 0 is already used
        stack.append(current_node)
        while stack:
            current_node = stack.pop()
            if current_node == matrix_end:
                return

            # Get traversable neighbors (up, down, left, right)
            neighbors = []
            current_x, current_y = current_node
            try: neighbors.append((current_x, current_y + 1)) if current_x >= 0 and (current_y + 1) >= 0 and matrix[current_x][current_y + 1] == 1 else None
            except IndexError: pass
            try: neighbors.append((current_x, current_y - 1)) if current_x >= 0 and (current_y - 1) >= 0 and matrix[current_x][current_y - 1] == 1 else None
            except IndexError: pass
            try: neighbors.append((current_x + 1, current_y)) if (current_x + 1) >= 0 and current_y >= 0 and matrix[current_x + 1][current_y] == 1 else None
            except IndexError: pass
            try: neighbors.append((current_x - 1, current_y)) if (current_x - 1) >= 0 and current_y >= 0 and matrix[current_x - 1][current_y] == 1 else None
            except IndexError: pass

            # Process neighbors
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)
            
            # Create node with left and right children
            left_child = neighbors[0] if len(neighbors) > 0 else None
            right_child = neighbors[1] if len(neighbors) > 1 else None
            node_set.append(node.node(name=str(current_node), parent=current_node, left=left_child, right=right_child))
            index += 1

        return node_set

    def search(self, nodes, start, goal, limit):
        stack = []
        visited = []
        stack.append((start, 0))  # FORMAT: (node, depth)

        while stack:
            current, depth = stack.pop()

            if current == goal:
                print(f"Goal {goal} found at depth {depth}")
                print("Path to goal:", self.get_path(visited, nodes))
                return True

            if depth < limit:
                # Get left and right children
                for node in nodes:
                    if node.get_name() == str(current):
                        left_child = node.get_left()
                        right_child = node.get_right()

                        # Add children to stack
                        if right_child and right_child not in visited:
                            visited.append(right_child)
                            stack.append((right_child, depth + 1))
                        if left_child and left_child not in visited:
                            visited.append(left_child)
                            stack.append((left_child, depth + 1))

        print(f"Goal {goal} not found within depth limit {limit}")
        return False
    
    def get_path(self, visited, nodes):
        # Convert visited names to node objects
        for i in range(0, len(visited)):
            for node in nodes:
                if node.get_name() == str(visited[i]):
                    visited[i] = node

        # Start to add path nodes to final set
        path_list = []
        visited_reverse = visited[::-1]
        path_list.append(visited_reverse[0].get_name())
        prev_node = visited_reverse[0].get_name()

        # Trace back the path from goal to start using parent references
        for node in visited_reverse:
            if str(node.get_left()) == prev_node or str(node.get_right()) == prev_node:
                path_list.append(node.get_name())
                prev_node = node.get_name()

        # Reverse the path to get from start to goal
        path_list.reverse()
        final_string = " -> ".join(path_list)
        return final_string
