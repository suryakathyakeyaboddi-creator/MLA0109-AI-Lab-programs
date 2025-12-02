import heapq

# Graph representation
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3, 'E': 5},
    'C': {'F': 2},
    'D': {'F': 1, 'E': 1},
    'E': {'F': 2},
    'F': {}
}

# Heuristic values (h)
heuristic = {
    'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 3, 'F': 0
}

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], start))  # f = g + h

    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    parent = {node: None for node in graph}
    expanded_order = []

    while open_list:
        f_cost, current = heapq.heappop(open_list)
        expanded_order.append(current)

        if current == goal:
            break
        
        for neighbor, weight in graph[current].items():
            new_g = g_cost[current] + weight

            if new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                total_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (total_f, neighbor))
                parent[neighbor] = current

    # Construct path
    path = []
    node = goal
    while node is not None:
        path.insert(0, node)
        node = parent[node]

    return path, g_cost[goal], expanded_order

# Run A*
path, total_cost, order = a_star('A', 'F')

print("Order of Node Expansion:", order)
print("Optimal Path:", " -> ".join(path))
print("Total Cost:", total_cost)
