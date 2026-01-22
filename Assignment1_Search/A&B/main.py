import bfs
import dfs
import node

# Create nodes
F = node.node("F", None, None)
E = node.node("E", None, None)
D = node.node("D", F, None)
C = node.node("C", E, None)
B = node.node("B", C, D)
A = node.node("A", B, None)

# Define start and goal nodes
start_node = A
goal_node = E

# Perform BFS
bfs_search = bfs.bfs()
bfs_result = bfs_search.search(start_node, goal_node)

# Perform DFS
dfs_search = dfs.dfs()
dfs_result = dfs_search.search(start_node, goal_node)