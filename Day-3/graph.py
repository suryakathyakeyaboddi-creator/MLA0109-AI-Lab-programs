# Map Coloring Problem using Backtracking

# Graph representing adjacent regions (Australia map)
graph = {
    "Western Australia": ["Northern Territory", "South Australia"],
    "Northern Territory": ["Western Australia", "South Australia", "Queensland"],
    "South Australia": ["Western Australia", "Northern Territory", "Queensland", "New South Wales", "Victoria"],
    "Queensland": ["Northern Territory", "South Australia", "New South Wales"],
    "New South Wales": ["Queensland", "South Australia", "Victoria"],
    "Victoria": ["South Australia", "New South Wales", "Tasmania"],
    "Tasmania": ["Victoria"]
}

# Available colors
colors = ["Red", "Green", "Blue", "Yellow"]

# Store assigned colors
solution = {}

def is_valid(region, color):
    for neighbor in graph[region]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

def solve(region_index=0):
    regions = list(graph.keys())

    # If all regions are colored
    if region_index == len(regions):
        return True

    region = regions[region_index]

    # Try each color
    for color in colors:
        if is_valid(region, color):
            solution[region] = color

            if solve(region_index + 1):
                return True

            # Backtrack
            solution.pop(region)

    return False


# Run the solver
if solve():
    print("Valid Map Coloring:")
    for region, color in solution.items():
        print(region, ":", color)
else:
    print("No solution found.")
