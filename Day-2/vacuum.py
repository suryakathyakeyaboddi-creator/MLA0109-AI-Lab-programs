from collections import deque

# Define the grid (0 = clean, 1 = dirty)
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

rows, cols = len(grid), len(grid[0])

# Initial position of vacuum cleaner
vacuum_pos = (0, 0)

# Directions for Up, Down, Left, Right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def print_grid():
    for r in range(rows):
        for c in range(cols):
            if (r, c) == vacuum_pos:
                print("V", end=" ")
            elif grid[r][c] == 1:
                print("D", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def bfs(start, target):
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == target:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                queue.append(((nr, nc), path + [(nr, nc)]))
                visited.add((nr, nc))
    return None

def find_nearest_dirty(pos):
    dirty_cells = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 1]
    if not dirty_cells:
        return None

    # Find nearest dirty cell by BFS distance
    shortest_path = None
    best_target = None

    for d in dirty_cells:
        path = bfs(pos, d)
        if shortest_path is None or len(path) < len(shortest_path):
            shortest_path = path
            best_target = d
    return best_target, shortest_path

# Main Loop
print("Initial Grid:")
print_grid()

total_moves = 0

while True:
    target = find_nearest_dirty(vacuum_pos)
    if not target:
        print("All dirt cleaned!")
        break

    dirty_cell, path = target

    for step in path:
        vacuum_pos = step
        total_moves += 1
        print_grid()

    # Clean the dirty cell
    grid[dirty_cell[0]][dirty_cell[1]] = 0
    print(f"Cleaned cell at {dirty_cell}\n")

print(f"Total Moves Made: {total_moves}")
