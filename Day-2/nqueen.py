import random

# -----------------------------------------
# Cost Function: Count attacking pairs
# -----------------------------------------
def compute_cost(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # same row
            if state[i] == state[j]:
                attacks += 1
            # same diagonal
            if abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

# -----------------------------------------
# Generate all neighbors by moving each queen
# -----------------------------------------
def get_neighbors(state):
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = list(state)
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

# -----------------------------------------
# Hill Climbing Algorithm
# -----------------------------------------
def hill_climbing(initial_state):
    current = initial_state
    current_cost = compute_cost(current)

    while True:
        neighbors = get_neighbors(current)
        # Calculating cost for neighbors
        costs = [compute_cost(n) for n in neighbors]

        # Best neighbor
        best_cost = min(costs)
        best_neighbor = neighbors[costs.index(best_cost)]

        # Move if strictly better
        if best_cost < current_cost:
            current = best_neighbor
            current_cost = best_cost
        else:
            break  # No better neighbor → local optimum

    return current, current_cost

# -----------------------------------------
# Random Restart Hill Climbing
# -----------------------------------------
def random_restart_hill_climbing(n, max_restarts=50):
    for i in range(max_restarts):
        initial_state = [random.randint(0, n - 1) for _ in range(n)]
        final_state, cost = hill_climbing(initial_state)

        if cost == 0:
            print("Solution found using random restarts:", i, "restart(s)\n")
            return final_state, cost

    return final_state, cost  # return last attempt if no perfect one

# -----------------------------------------
# Print Chess Board
# -----------------------------------------
def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print()

# -----------------------------------------
# MAIN
# -----------------------------------------
N = 8
final_state, final_cost = random_restart_hill_climbing(N)

print("Final State:", final_state)
print("Final Cost:", final_cost)
print("Valid Solution?", final_cost == 0)
print("\nBoard Configuration:")
print_board(final_state)
