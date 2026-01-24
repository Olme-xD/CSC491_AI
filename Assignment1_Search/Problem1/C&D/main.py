import bfs, dfs, os
os.system('cls' if os.name == 'nt' else 'clear')

matrix = [
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
]

# Define start and goal points
start_point = 6,0
end_point = 3,3

# Do BFS on the matrix
bfs_search = bfs.bfs()
bfs_search.search(matrix, start_point, end_point)

# Do DFS on the matrix
dfs_search = dfs.dfs()
dfs_search.search(matrix, start_point, end_point)
