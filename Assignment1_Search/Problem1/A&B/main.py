import bfs, dfs, node, os
os.system('cls' if os.name == 'nt' else 'clear')

# Create nodes
F = node.node("F", None, None, None)
E = node.node("E", None, None, None)
D = node.node("D", None, F, None)
C = node.node("C", None, E, None)
B = node.node("B", None, C, D)
A = node.node("A", None, B, None)
A.set_parent(None)
B.set_parent(A)
C.set_parent(B)
D.set_parent(B)
E.set_parent(C)
F.set_parent(D)

# Define start and goal nodes
start_node = A
goal_node = E

# Perform BFS
bfs_search = bfs.bfs()
bfs_result = bfs_search.search(start_node, goal_node)
print("\n")

# Perform DFS
dfs_search = dfs.dfs()
dfs_result = dfs_search.search(start_node, goal_node)