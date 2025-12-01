import heapq

# Goal state of the puzzle
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Directions to move zero (empty tile)
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0
    for i, value in enumerate(state):
        if value != 0:
            target = goal_state.index(value)
            distance += abs(target // 3 - i // 3) + abs(target % 3 - i % 3)
    return distance

# A* search algorithm
def solve_puzzle(start_state):
    pq = []  # priority queue
    heapq.heappush(pq, (0 + heuristic(start_state), 0, start_state, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal_state:
            return path + [state]

        visited.add(state)
        zero_pos = state.index(0)

        for move_to in moves[zero_pos]:
            new_state = list(state)
            new_state[zero_pos], new_state[move_to] = new_state[move_to], new_state[zero_pos]
            new_state = tuple(new_state)

            if new_state not in visited:
                heapq.heappush(pq, (g + 1 + heuristic(new_state), g + 1, new_state, path + [state]))

    return None

# Example Start State (scrambled puzzle)
start = (1, 2, 3,
         5, 0, 6,
         4, 7, 8)

# Run Solver
solution = solve_puzzle(start)

# Display Results
if solution:
    print("Steps to solve the puzzle:")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print("-----")
else:
    print("No solution found")
