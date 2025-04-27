import random
import math
import numpy as np

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_total_distance(route, points):
    total = 0
    for i in range(len(route)):
        total += calculate_distance(points[route[i]], points[route[(i + 1) % len(route)]])
    return total

def create_initial_population(size, n_cities):
    return [random.sample(range(n_cities), n_cities) for _ in range(size)]

def fitness(route, points):
    return 1 / (1 + calculate_total_distance(route, points))

def select_parents(population, points, n_parents):
    fitness_scores = [fitness(route, points) for route in population]
    total_fitness = sum(fitness_scores)
    probabilities = [score/total_fitness for score in fitness_scores]
    
    return random.choices(population, weights=probabilities, k=n_parents)

def crossover(parent1, parent2):
    n = len(parent1)
    start, end = sorted(random.sample(range(n), 2))
    
    child = [-1] * n
    child[start:end] = parent1[start:end]
    
    remaining = [x for x in parent2 if x not in child[start:end]]
    j = 0
    for i in range(n):
        if child[i] == -1:
            child[i] = remaining[j]
            j += 1
    
    return child

def mutate(route, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route

def genetic_algorithm(points, pop_size=100, n_generations=100):
    n_cities = len(points)
    population = create_initial_population(pop_size, n_cities)
    
    for _ in range(n_generations):
        new_population = []
        
        for _ in range(pop_size // 2):
            parents = select_parents(population, points, 2)
            child1 = crossover(parents[0], parents[1])
            child2 = crossover(parents[1], parents[0])
            
            child1 = mutate(child1)
            child2 = mutate(child2)
            
            new_population.extend([child1, child2])
        
        population = new_population
    
    best_route = max(population, key=lambda x: fitness(x, points))
    return best_route, calculate_total_distance(best_route, points)

def main():
    points = [
        (0, 0), (1, 2), (3, 1), (4, 3), (2, 4),
        (5, 2), (6, 4), (7, 1), (8, 3), (9, 0)
    ]
    
    best_route, best_distance = genetic_algorithm(points)
    print(f"Best route: {best_route}")
    print(f"Total distance: {best_distance:.2f}")

if __name__ == "__main__":
    main() 