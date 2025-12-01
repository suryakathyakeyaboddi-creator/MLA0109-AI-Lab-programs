from collections import deque
start_state = ("Door", "Window", False, False)  # Initial state
goal_state = ("Middle", "Middle", True, True)   # Goal state

# Actions
def get_next_states(state):
    monkey, box, on_box, have_banana = state
    states = []

    # 1. Monkey walks to another location
    for pos in ["Door", "Window", "Middle"]:
        if pos != monkey and not on_box:  # can walk only if not on the box
            states.append((pos, box, False, have_banana))

    # 2. Monkey pushes box (only if monkey and box are at same place and not on box)
    if monkey == box and not on_box:
        for pos in ["Door", "Window", "Middle"]:
            if pos != box:
                states.append((pos, pos, False, have_banana))

    # 3. Monkey climbs onto the box (only if same position)
    if monkey == box and not on_box:
        states.append((monkey, box, True, have_banana))

    # 4. Monkey gets the bananas (only if on box & at Middle)
    if on_box and monkey == "Middle":
        states.append((monkey, box, True, True))

    return states


def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            return path

        for next_state in get_next_states(state):
            queue.append((next_state, path))

    return None


solution = bfs(start_state, goal_state)

# Display solution path
print("Steps to solve Monkey & Banana problem:")
for s in solution:
    print(s)
