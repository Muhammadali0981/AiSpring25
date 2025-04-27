import random
import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_total_distance(route, points):
    total = 0
    for i in range(len(route)):
        total += calculate_distance(points[route[i]], points[route[(i + 1) % len(route)]])
    return total

def hill_climbing(points, max_iterations=1000):
    n = len(points)
    current_route = list(range(n))
    random.shuffle(current_route)
    current_distance = calculate_total_distance(current_route, points)
    
    for _ in range(max_iterations):
        i, j = random.sample(range(n), 2)
        new_route = current_route.copy()
        new_route[i], new_route[j] = new_route[j], new_route[i]
        
        new_distance = calculate_total_distance(new_route, points)
        
        if new_distance < current_distance:
            current_route = new_route
            current_distance = new_distance
    
    return current_route, current_distance

points = [
    (0, 0), (1, 2), (3, 1), (4, 3), (2, 4),
    (5, 2), (6, 4), (7, 1), (8, 3), (9, 0)
]

best_route, best_distance = hill_climbing(points)
print(f"Best route: {best_route}")
print(f"Total distance: {best_distance:.2f}")
