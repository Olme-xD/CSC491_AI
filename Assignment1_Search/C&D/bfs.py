from collections import deque

class bfs:
    def __init__(self):
        pass

    def search(self, matrix, start, goal):
        queue = deque()
        visited = []

        # Validate data
        x_start, y_start = start
        x_goal, y_goal = goal
        if x_start < 0 or y_start < 0 or x_start >= len(matrix) or y_start >= len(matrix[0]):
            print("BFS-> WARNING: Start point out of bounds")
            return
        if matrix[x_start][y_start] != 1:
            print("BFS-> WARNING: Start point is not traversable")
            return
        if x_goal < 0 or y_goal < 0 or x_goal >= len(matrix) or y_goal >= len(matrix[0]):
            print("BFS-> WARNING: Goal point out of bounds")
            return
        if matrix[x_goal][y_goal] != 1:
            print("BFS-> WARNING: Goal point is not traversable")
            return

        # First node append
        queue.append((x_start, y_start))
        visited.append((start, None)) # FORMAT: (node, parent)

        while queue:
            current = queue.popleft()
            if current == goal:
                break
            
            # Get traversable neighbors (up, down, left, right)
            neighbors = []
            current_x, current_y = current
            try: neighbors.append((current_x + 1, current_y)) if (current_x + 1) >= 0 and current_y >= 0 and matrix[current_x + 1][current_y] == 1 else None
            except IndexError: pass
            try: neighbors.append((current_x - 1, current_y)) if (current_x - 1) >= 0 and current_y >= 0 and matrix[current_x - 1][current_y] == 1 else None
            except IndexError: pass
            try: neighbors.append((current_x, current_y + 1)) if current_x >= 0 and (current_y + 1) >= 0 and matrix[current_x][current_y + 1] == 1 else None
            except IndexError: pass
            try: neighbors.append((current_x, current_y - 1)) if current_x >= 0 and (current_y - 1) >= 0 and matrix[current_x][current_y - 1] == 1 else None
            except IndexError: pass

            # Process neighbors
            for neighbor in neighbors:
                if neighbor != goal:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.append((neighbor, current))

                        # If nothing on queue, return
                        if not queue:
                            print("BFS-> WARNING: Queue is empty, goal not reachable")
                            return
                else:
                    visited.append((neighbor, current)) # Goal found, just add last node

                    # Start to add path nodes to final set
                    final_path = []
                    visited_reverse = visited[::-1]
                    target_node = visited_reverse[0][0]
                    final_path.append(target_node)

                    # Trace back the path from goal to start using parent references
                    for node, parent in visited_reverse:
                        if node == target_node and parent is not None:
                            final_path.append(parent)
                            target_node = parent
                        
                    final_path.reverse()
                    final_path_str = " -> ".join([str(p) for p in final_path])
                    return print("BFS path: " + final_path_str)
                    
        
