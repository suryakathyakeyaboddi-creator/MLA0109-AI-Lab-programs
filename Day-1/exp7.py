from collections import deque

def water_jug_bfs():
    start = (0, 0)   # both jugs empty initially
    goal = 2         # We want 2 gallons in 4-gallon jug

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (jug4, jug3), path = queue.popleft()

        # If goal is reached
        if jug4 == goal:
            return path + [(jug4, jug3)]

        # If already visited skip
        if (jug4, jug3) in visited:
            continue

        visited.add((jug4, jug3))
        next_states = []

        # Possible operations:

        next_states.append((4, jug3))  # Fill 4-gallon jug
        next_states.append((jug4, 3))  # Fill 3-gallon jug

        next_states.append((0, jug3))  # Empty 4-gallon jug
        next_states.append((jug4, 0))  # Empty 3-gallon jug

        # Pour 3 -> 4
        transfer = min(jug3, 4 - jug4)
        next_states.append((jug4 + transfer, jug3 - transfer))

        # Pour 4 -> 3
        transfer = min(jug4, 3 - jug3)
        next_states.append((jug4 - transfer, jug3 + transfer))

        # Add all valid states to queue
        for state in next_states:
            queue.append((state, path + [(jug4, jug3)]))

    return None


solution = water_jug_bfs()

print("Steps to get 2 gallons in 4-gallon jug:")
for step in solution:
    print(step)
