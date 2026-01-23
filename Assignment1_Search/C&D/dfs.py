class dfs:
    def __init__(self):
        pass

    def search(self, matrix, start, goal):
        stack = []
        visited = []
        visitedWparent = []

        # Validate data
        x_start, y_start = start
        x_goal, y_goal = goal
        if x_start < 0 or y_start < 0 or x_start >= len(matrix) or y_start >= len(matrix[0]):
            print("DFS-> WARNING: Start point out of bounds")
            return
        if matrix[x_start][y_start] != 1:
            print("DFS-> WARNING: Start point is not traversable")
            return
        if x_goal < 0 or y_goal < 0 or x_goal >= len(matrix) or y_goal >= len(matrix[0]):
            print("DFS-> WARNING: Goal point out of bounds")
            return
        if matrix[x_goal][y_goal] != 1:
            print("DFS-> WARNING: Goal point is not traversable")
            return
        
        # First node append
        stack.append((x_start, y_start))
        visited.append((x_start, y_start))
        visitedWparent.append((start, None)) # FORMAT: (node, parent)

        while stack:
            current = stack.pop()
            if current == goal:
                break
                    
            # Get traversable neighbors (up, down, left, right)
            neighbors = []
            current_x, current_y = current
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
                if neighbor != goal:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.append(neighbor)
                        visitedWparent.append((neighbor, current))
                            
                        # If nothing on stack, return
                        if stack == []:
                            print("DFS-> WARNING: Stack is empty, goal not reachable")
                            return
                else:
                    visitedWparent.append((neighbor, current)) # Goal found, just add last node

                    # Start to add path nodes to final set
                    final_path = []
                    visitedWparent_reverse = visitedWparent[::-1]
                    target_node = visitedWparent_reverse[0][0]
                    final_path.append(target_node)

                    # Trace back the path from goal to start using parent references
                    for node, parent in visitedWparent_reverse:
                        if node == target_node and parent is not None:
                            final_path.append(parent)
                            target_node = parent
                        
                    final_path.reverse()
                    final_path_str = " -> ".join([str(p) for p in final_path])
                    return print("DFS path: " + final_path_str)