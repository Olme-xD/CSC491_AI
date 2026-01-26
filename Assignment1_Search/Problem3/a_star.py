import node, heapq

class a_star():
    def __init__(self):
        pass

    def search(self, start, goal):
        g_score = {start: 0}
        came_from = {}
        frontier = []
        explored = {}
        closed = set()
        heapq.heappush(frontier, (start.get_h(), 0, id(start), start))

        while frontier:
            print('Frontier:')
            for (f, g, _id, node) in frontier:
                print(f"{node.get_name()} ({g}+{node.get_h()})={f}")

            print('Explored:')
            for node, f in explored.items():
                print(f"{node} ({f})")
            print('\n')

            f, current_g, _id, current = heapq.heappop(frontier)
            explored[current.get_name()] = f

            if current is goal:
                path = self.get_path(came_from, current)
                print(f"Path: {" -> ".join(path)}\nCost: {current_g}")
                return path

            if current in closed:
                continue
            closed.add(current)

            for neighbor, cost in current.get_edges().items():
                tentative_g = current_g + cost
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    tentative_frontier = tentative_g + neighbor.get_h()
                    heapq.heappush(frontier, (tentative_frontier, tentative_g, id(neighbor), neighbor))

        print("No path found")
        return None
            
    def get_path(self, came_from, current):
        path = []

        while current in came_from:
            path.append(current.get_name())
            current = came_from[current]

        path.append(current.get_name())
        path.reverse()
        return path
    