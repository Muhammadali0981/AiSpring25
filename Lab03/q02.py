from itertools import permutations

def tsp_bruteforce(distances):
    n = len(distances)
    if n <= 1:
        return 0, [0]
    
    min_path = None
    min_cost = float('inf')
    
  
    for permutation in permutations(range(1, n)):
        current_cost = 0
        current_path = [0] + list(permutation) + [0]
        
        
        for i in range(n):
            current_cost += distances[current_path[i]][current_path[i+1]]
        
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = current_path
    
    return min_cost, min_path

distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cost, path = tsp_bruteforce(distances)
print(f"TSP Solution: Cost={cost}, Path={path}")

