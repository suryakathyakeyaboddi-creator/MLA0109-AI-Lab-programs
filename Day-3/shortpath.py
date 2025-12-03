from itertools import permutations

# Cities and distances matrix
cities = ['A', 'B', 'C', 'D']

# Distance matrix
distances = {
    'A': {'A': 0,  'B': 10, 'C': 12, 'D': 8},
    'B': {'A': 10, 'B': 0,  'C': 8,  'D': 12},
    'C': {'A': 12, 'B': 8,  'C': 0,  'D': 10},
    'D': {'A': 8,  'B': 12, 'C': 10, 'D': 0}
}

def tsp(start_city):
    cities_to_visit = cities.copy()
    cities_to_visit.remove(start_city)

    min_cost = float('inf')
    best_path = None

    for perm in permutations(cities_to_visit):
        current_path = [start_city] + list(perm) + [start_city]

        # Calculate route cost
        cost = 0
        for i in range(len(current_path) - 1):
            cost += distances[current_path[i]][current_path[i+1]]

        # Compare cost
        if cost < min_cost:
            min_cost = cost
            best_path = current_path

    return best_path, min_cost


# Run TSP starting from A
path, cost = tsp('A')
print("Shortest Path:", " -> ".join(path))
print("Minimum Cost:", cost)
