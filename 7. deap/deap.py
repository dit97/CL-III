import random
# for toolbox, custom classes, GA operators, Ready madhe fun or algo
from deap import base, creator, tools, algorithms

# Define the evaluation function x1^2 + x2^2 + x3^2 close to zero 
def eval_func(individual):
    return sum(x ** 2 for x in individual),

# DEAP setup.. custom create fitness class(minimization problem -1.0) and individual class(based on py list)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin) 

#toobox stores functions
toolbox = base.Toolbox()

# Define attributes and individuals
toolbox.register("attr_float", random.uniform, -5.0, 5.0) # generates random uniform no between -5 to 5
# create individual by repeating attr_float 3 times and store in individual  [1.4,2.3,3.4]
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3) 
# generate population by repeating individual and storing in list  -- just template
toolbox.register("population", tools.initRepeat, list, toolbox.individual) 

# Register evaluation and genetic operators
toolbox.register("evaluate", eval_func) # Store fitness evaluation function inside toolbox.
toolbox.register("mate", tools.cxBlend, alpha=0.5) # crossover with 50% mixing of parents 
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2) # Register Gaussian mutation operator with 20% mutation probability.
toolbox.register("select", tools.selTournament, tournsize=3) # choose best individuals

# Create population
population = toolbox.population(n=50)

# Evaluate initial population
for ind in population:
    ind.fitness.values = toolbox.evaluate(ind)

# Number of generations
generations = 20

# Run the algorithm
for gen in range(generations):

    # Generate offspring-- Algorithmm contains redy made ga functions-- cross over probability 50% mutation 10% 
    # varAnd automatic perform cross over and mutation
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

    # Evaluate offspring
    for ind in offspring:
        ind.fitness.values = toolbox.evaluate(ind)

    # Select next generation
    population = toolbox.select(offspring, k=len(population))

# Get best individual
best_ind = tools.selBest(population, k=1)[0]

print("Best Individual:", best_ind)
print("Best Fitness:", best_ind.fitness.values[0])