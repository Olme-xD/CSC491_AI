import dls, os
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
end_point = 0,5
goal_point = 3,3

# Create dls object
dls_obj = dls.dls()
nodes = dls_obj.generate_tree_from_matrix(matrix, start_point, end_point)
dls_obj.search(nodes, start_point, goal_point, limit=8)
