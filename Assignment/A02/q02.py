import random

TASK_TIMES = [5, 8, 4, 7, 6, 3, 9]
FACILITY_CAPACITIES = [24, 30, 28]
COST_MATRIX = [
    [10, 12, 9],   # Task 1
    [15, 14, 16],  # Task 2
    [8, 9, 7],     # Task 3
    [12, 10, 13],  # Task 4
    [14, 13, 12],  # Task 5
    [9, 8, 10],    # Task 6
    [11, 12, 13],  # Task 7
]
NUM_TASKS = len(TASK_TIMES)
NUM_FACILITIES = len(FACILITY_CAPACITIES)
POP_SIZE = 6
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2
PENALTY = 1000  # Penalty for exceeding capacity


def random_chromosome():
    return [random.randint(0, NUM_FACILITIES - 1) for _ in range(NUM_TASKS)]

def fitness(chromosome):
    total_cost = 0
    facility_times = [0] * NUM_FACILITIES
    for task, facility in enumerate(chromosome):
        facility_times[facility] += TASK_TIMES[task]
        total_cost += COST_MATRIX[task][facility] * TASK_TIMES[task]
    # Penalize if any facility exceeds its capacity
    for i, time in enumerate(facility_times):
        if time > FACILITY_CAPACITIES[i]:
            total_cost += PENALTY * (time - FACILITY_CAPACITIES[i])
    return -total_cost  # Negative because we want to minimize cost

def roulette_wheel_selection(population, fitnesses):
    total_fit = sum(fitnesses)
    pick = random.uniform(0, total_fit)
    current = 0
    for chrom, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return chrom
    return population[-1]

def one_point_crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, NUM_TASKS - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1[:], parent2[:]

def swap_mutation(chromosome):
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, NUM_TASKS - 1)
        new_facility = random.randint(0, NUM_FACILITIES - 1)
        chromosome[idx] = new_facility
    return chromosome

def genetic_algorithm(generations=100):
    population = [random_chromosome() for _ in range(POP_SIZE)]
    for _ in range(generations):
        fitnesses = [fitness(chrom) for chrom in population]
        new_population = []
        while len(new_population) < POP_SIZE:
            parent1 = roulette_wheel_selection(population, fitnesses)
            parent2 = roulette_wheel_selection(population, fitnesses)
            child1, child2 = one_point_crossover(parent1, parent2)
            child1 = swap_mutation(child1)
            child2 = swap_mutation(child2)
            new_population.extend([child1, child2])
        population = new_population[:POP_SIZE]
    # Return the best solution
    fitnesses = [fitness(chrom) for chrom in population]
    best_idx = fitnesses.index(max(fitnesses))
    return population[best_idx], -fitnesses[best_idx]


best_solution, best_cost = genetic_algorithm(generations=100)
print(f'best_solution, best_cost')
 