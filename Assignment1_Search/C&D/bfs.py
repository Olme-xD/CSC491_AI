from collections import deque
import node

class bfs(node.node):
    def __init__(self):
        pass

    def search(self, matrix, start, goal):
        queue = deque()
        visited = []

        # Validate start and goal points
        x_start, y_start = start
        if x_start < 0 or y_start < 0 or x_start >= len(matrix) or y_start >= len(matrix[0]):
            print("Start point out of bounds")
            return
        if matrix[x_start][y_start] != 1:
            print("Start point is not traversable")
            return
        
        # Validate goal point
        x_goal, y_goal = goal
        if x_goal < 0 or y_goal < 0 or x_goal >= len(matrix) or y_goal >= len(matrix[0]):
            print("Goal point out of bounds")
            return
        if matrix[x_goal][y_goal] != 1:
            print("Goal point is not traversable")
            return

        # First node append
        queue.append((x_start, y_start))
        visited.append(start)

        while queue:
            current = queue.popleft()

            if current == goal:
                break
            else:
                current_x, current_y = current

                # Get traversable neighbors (up, down, left, right)
                neighbors = []
                try: neighbors.append((current_x + 1, current_y)) if (current_x + 1) >= 0 and current_y >= 0 and matrix[current_x + 1][current_y] == 1 else None
                except IndexError: pass

                try: neighbors.append((current_x - 1, current_y)) if (current_x - 1) >= 0 and current_y >= 0 and matrix[current_x - 1][current_y] == 1 else None
                except IndexError: pass

                try: neighbors.append((current_x, current_y + 1)) if current_x >= 0 and (current_y + 1) >= 0 and matrix[current_x][current_y + 1] == 1 else None
                except IndexError: pass

                try: neighbors.append((current_x, current_y - 1)) if current_x >= 0 and (current_y - 1) >= 0 and matrix[current_x][current_y - 1] == 1 else None
                except IndexError: pass
                print('Neighbors: ', neighbors)

                # Process neighbors
                for neighbor in neighbors:
                    x, y = neighbor
                    if neighbor != goal:
                        if neighbor not in queue and neighbor not in visited:
                            queue.append(neighbor)
                            visited.append(neighbor)

                            # If nothing on queue, return
                            if not queue:
                                print("Queue is empty, goal not reachable")
                                return
                    else:
                        visited.append(neighbor)
                        print("Visited nodes: ", visited)
                        return
                    
            print("Queue: ", queue)
