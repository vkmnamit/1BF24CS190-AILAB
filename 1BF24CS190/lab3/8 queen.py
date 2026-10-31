import random

def get_attacks(state):
    """Calculates the total number of attacking pairs of queens."""
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Same row
            if state[i] == state[j]:
                attacks += 1
            # Same diagonal
            elif abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_best_neighbor(state):
    """Finds the best neighboring state by moving one queen at a time within its column."""
    n = len(state)
    current_attacks = get_attacks(state)
    best_state = list(state)
    best_attacks = current_attacks
    
    # Store all neighbors that match the best score to choose randomly among ties
    best_neighbors = [best_state] 

    for col in range(n):
        original_row = state[col]
        for row in range(n):
            if row == original_row:
                continue
            
            # Create a neighbor state by moving the queen in 'col' to 'row'
            neighbor = list(state)
            neighbor[col] = row
            neighbor_attacks = get_attacks(neighbor)
            
            if neighbor_attacks < best_attacks:
                best_attacks = neighbor_attacks
                best_neighbors = [neighbor]
            elif neighbor_attacks == best_attacks and neighbor_attacks < current_attacks:
                best_neighbors.append(neighbor)
                
        state[col] = original_row  # Reset

    # Return a random pick from the best evaluated states
    return random.choice(best_neighbors), best_attacks

def hill_climbing_8_queens():
    """Runs the hill climbing algorithm with random restarts until a solution is found."""
    n = 8
    restarts = 0
    
    while True:
        # Generate a random initial state (one queen per column)
        # index = column, value = row
        state = [random.randint(0, n - 1) for _ in range(n)]
        current_attacks = get_attacks(state)
        
        while True:
            neighbor, neighbor_attacks = get_best_neighbor(state)
            
            # If no neighbor is strictly better, we hit a local minimum or a solution
            if neighbor_attacks >= current_attacks:
                break
                
            state = neighbor
            current_attacks = neighbor_attacks
            
        # If we reached 0 attacks, it's a global optimum (solution found)
        if current_attacks == 0:
            return state, restarts
            
        restarts += 1

def print_board(state):
    """Prints the board layout nicely."""
    n = len(state)
    for row in range(n):
        line = []
        for col in range(n):
            if state[col] == row:
                line.append("Q")
            else:
                line.append(".")
        print(" ".join(line))

# Execute the algorithm
solution, total_restarts = hill_climbing_8_queens()

print(f"Solution found after {total_restarts} random restarts:\n")
print_board(solution)
print(f"\nState Array (Row index per Column): {solution}")
