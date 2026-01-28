import copy

class minimax:
    def __init__(self, first_S):
        self.first_S = first_S
        self.max_depth = 0
        self.terminalS_count = 0

    # X player
    def max_value(self, state):
        if self.terminal(state):
            return self.utility(state)
        
        a = -float('inf') # NOTE: Negative float bc of X goals
        for action in self.actions(state):
            state_new = self.result(state, action)
            a = max(a, self.min_value(state_new))

        return a
    
    # O player
    def min_value(self, state):
        if self.terminal(state): 
            return self.utility(state)
            
        a = float('inf') # NOTE: Positive float bc of O goals
        for action in self.actions(state):
            new_state = self.result(state, action)
            a = min(a, self.max_value(new_state))

        return a
    
    def draw_state(self, S, indent=''):
        for x in range(3):
            print(indent, end='')
            for y in range(3):
                value = S[x][y]
                if value == '':
                    value = ' '
                
                print(f' {value} ', end='')
                if y < 2:
                    print(f'|', end='')
                
            print()
            if x < 2:
                print(f'{indent}------------')

    def print_tree(self, state, depth=0):
        # Update or reject new depth value
        self.max_depth = depth if depth > self.max_depth else self.max_depth

        # Current depth and player
        indent = "       " * depth
        player_turn = self.player(state)
        print(f"\n{indent}Depth: {depth}")
        self.draw_state(state, indent)

        # Check if Terminal
        if self.terminal(state):
            self.terminalS_count += 1
            val = self.utility(state)
            print(f"{indent}Terminal State Triggered\n{indent}Value: {val}")
            return
        print(f"{indent}Next player move: {player_turn}")

        # Check children
        for action in self.actions(state):
            print(f"\n{indent}|--> Action: {action}", end='')
            next_state = self.result(state, action)
            self.print_tree(next_state, depth + 1)

    def player(self, state):
        # NOTE: Keep in mind that by default X starts first
        x_count = o_count = 0
        for row in state:
            x_count += row.count('X')
            o_count += row.count('O')
        
        if x_count <= o_count:
            return 'X'
        return 'O'
    
    def actions(self, state):
        # Reads for empty [x][y] 
        allowed_moves = []
        for x in range(3):
            for y in range(3):
                if state[x][y] == '':
                    allowed_moves.append((x, y))
        
        return allowed_moves
    
    def result(self, state, action):
        # Performm the action
        state_new = copy.deepcopy(state)
        x, y = action

        player = self.player(state)
        state_new[x][y] = player
        return state_new
    
    def terminal(self, state):
        # Diagonal [0][0] [1][1] [2][2] or biceversa
        if state[0][0] != '' and state[0][0] == state[1][1] == state[2][2]:
             return state[0][0]
        if state[0][2] != '' and state[0][2] == state[1][1] == state[2][0]:
             return state[0][2]

        
        for i in range(3):
            # Vertical Line [0][0] [1][0] [2][0]
            if state[0][i] != '' and state[0][i] == state[1][i] == state[2][i]:
                return state[0][i]
            # Horizontal Line [0][1] [0][2] [0][3]
            if state[i][0] != '' and state[i][0] == state[i][1] == state[i][2]:
                return state[i][0]
            
        for row in state:
            if '' in row:
                return None
        return 'Draw' # Draw state
    
    def utility(self, state):
        # Numerical value for terminal state s
        winner = self.terminal(state)
        numerical_value = 0
        if winner == 'X':
            numerical_value = 1
            return numerical_value
        
        elif winner == 'O':
            numerical_value = -1
            return numerical_value
        
        elif winner == 'Draw':
            return numerical_value

        return None
    