import numpy as np

# Distance matrix
distances = np.array([
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
])


# Parameters
num_ants = 4
iterations = 10
alpha = 1    # Importance of pheromone
beta = 2     # Importance of distance
rho = 0.5    # Evaporation rate

# Initial pheromone
pheromone = np.ones((num_cities, num_cities))

best_path = None
best_distance = float('inf')

for iteration in range(iterations):
    for ant in range(num_ants):
        current_city = 0
        path = [current_city]
        unvisited_cities = list(range(1, num_cities))

        while unvisited_cities:
            probabilities = []
            
            for next_city in unvisited_cities:
                pheromone_value = pheromone[current_city][next_city]
                distance_value = distances[current_city][next_city]
                heuristic_value = 1 / distance_value
                probability = ( (pheromone_value ** alpha) * (heuristic_value ** beta))

                probabilities.append(probability)

            probabilities = np.array(probabilities)
            probabilities = probabilities / probabilities.sum()

            selected_city = np.random.choice(unvisited_cities, p=probabilities )

            path.append(selected_city)
            unvisited_cities.remove(selected_city)
            current_city = selected_city

        # Return to starting city
        path.append(0)

        # Calculate total distance
        total_distance = 0

        for i in range(len(path) - 1):
            total_distance += distances[path[i]][path[i + 1]]

        # Update best path
        if total_distance < best_distance:
            best_distance = total_distance
            best_path = path

        # Update pheromone
        for i in range(len(path) - 1):
            city1 = path[i]
            city2 = path[i + 1]
            pheromone[city1][city2] += 1 / total_distance

    # Pheromone evaporation
    pheromone = (1 - rho) * pheromone

print("Best Path:", best_path)
print("Shortest Distance:", best_distance)




# 1. Ant starts from one city
# 2. Checks unvisited cities
# 3. Calculates probability using pheromone and distance
# 4. Selects next city probabilistically
# 5. Adds selected city to path
# 6. Repeats until all cities visited
# 7. Returns to starting city
# 8. Calculates total path distance
# 9. Deposits pheromone on travelled path
# 10. Shorter paths get more pheromone, so future ants prefer them