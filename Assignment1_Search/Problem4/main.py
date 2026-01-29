import node, minimax, os
os.system("cls" if os.name == "nt" else "clear")

# Create state from given S
state = [
    ['O', 'O', 'X'],
    ['X', 'X', ''],
    ['O', '', '']
]

# Create instances
_minimax = minimax.minimax(state)
print("Current Board:")
_minimax.draw_state(state)
current_player = _minimax.player(state)
print(f"\nPlayer turn: {current_player}")
best_score = _minimax.max_value(state)
print(f"Best possible outcomes for X: {best_score}")

# Answer for a
_minimax.print_tree(state)
# Answer for b
print(f"Space complexity (including root): {_minimax.max_depth + 1}")
# Answer for c
print(f"Number of terminal states: {_minimax.terminalS_count}")
