import bfs, dfs

matrix_main = [
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