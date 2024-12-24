import numpy as np
import random
import math

# تابع محاسبه فاصله بین دو شهر
def distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# تابع محاسبه طول مسیر
def total_distance(route, cities):
    return sum(distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1)) + distance(cities[route[-1]], cities[route[0]])

# تولید نقاط تصادفی برای شهرها
num_cities = 10
cities = np.random.rand(num_cities, 2) * 100  


# تپه نوردی 
def hill_climbing(cities):
    current_route = list(range(len(cities)))
    random.shuffle(current_route)
    current_distance = total_distance(current_route, cities)

    while True:
        neighbors = []
        for i in range(len(current_route)):
            for j in range(i + 1, len(current_route)):
                neighbor = current_route[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # Swap cities
                neighbors.append(neighbor)

        next_route = min(neighbors, key=lambda route: total_distance(route, cities))
        next_distance = total_distance(next_route, cities)

        if next_distance >= current_distance:
            break

        current_route, current_distance = next_route, next_distance

    return current_route, current_distance



# ژنتیک 
def genetic_algorithm(cities, population_size=100, generations=500):
    def create_population(size):
        return [random.sample(range(len(cities)), len(cities)) for _ in range(size)]

    def fitness(route):
        return 1 / total_distance(route, cities)

    def selection(population):
        scores = [(fitness(route), route) for route in population]
        scores.sort(reverse=True)
        return [route for _, route in scores[:population_size // 2]]

    def crossover(parent1, parent2):
        size = len(parent1)
        child = [-1] * size
        start, end = sorted(random.sample(range(size), 2))
        child[start:end] = parent1[start:end]

        pointer = 0
        for gene in parent2:
            if gene not in child:
                while child[pointer] != -1:
                    pointer += 1
                child[pointer] = gene

        return child

    def mutate(route):
        if random.random() < 0.1:  # Mutation chance
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]

    population = create_population(population_size)

    for _ in range(generations):
        selected = selection(population)
        next_generation = selected[:]

        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            child = crossover(parent1, parent2)
            mutate(child)
            next_generation.append(child)

        population = next_generation

    best_route = max(population, key=fitness)
    return best_route, total_distance(best_route, cities)



# تبرید
def simulated_annealing(cities, initial_temp=1000, cooling_rate=0.995):
    current_route = list(range(len(cities)))
    random.shuffle(current_route)
    current_distance = total_distance(current_route, cities)

    temperature = initial_temp

    while temperature > 1:
        i, j = random.sample(range(len(current_route)), 2)
        new_route = current_route[:]
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_distance = total_distance(new_route, cities)

        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_route, current_distance = new_route, new_distance

        temperature *= cooling_rate

    return current_route, current_distance


# مقایسه نتایج
hill_climbing_result = hill_climbing(cities)
genetic_result = genetic_algorithm(cities)
simulated_annealing_result = simulated_annealing(cities)

print("Hill Climbing Result: ", hill_climbing_result)
print("Genetic Algorithm Result: ", genetic_result)
print("Simulated Annealing Result: ", simulated_annealing_result)
