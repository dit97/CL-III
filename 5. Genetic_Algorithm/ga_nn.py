import pandas as pd
import random

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error


# Load Dataset
data = pd.read_csv(
    "coconut_milk_spray_drying_dataset.csv"
)


# Input Features
X = data[
    [
        "Inlet_Temperature_C",
        "Feed_Rate_ml_min",
        "Air_Flow_m3_h",
        "Nozzle_Pressure_bar",
        "Moisture_Content_percent",
        "Particle_Size_microns"
    ]
]


# Output
y = data["Product_Yield_percent"]


# Split Data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Initial Population-- represents no of neurons
population = [10, 20, 30, 40, 50]

best_score = float("inf")
best_neurons = 0
best_model = None


print("Running Genetic Algorithm...\n")


# GA Loop
for generation in range(10):

    print(f"Generation {generation + 1}")

    scores = []

    # Fitness Evaluation-- by mse
    for neurons in population:

        model = MLPRegressor(
            hidden_layer_sizes=(neurons,),
            max_iter=2000,
            random_state=42
        )

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        mse = mean_squared_error(y_test,predictions)

        scores.append((mse, neurons))

        print(
            f"Neurons: {neurons} | MSE: {mse}"
        )

        # Best Solution
        if mse < best_score:
            best_score = mse
            best_neurons = neurons
            best_model = model

    # Selection
    scores.sort()
    #takes neurons value
    parent1 = scores[0][1]
    parent2 = scores[1][1]

    # Mutation
    child = int((parent1 + parent2) / 2)

    child += random.randint(-5, 5)

    # New Population
    population = [
        parent1,
        parent2,
        child,
        random.randint(5, 50),
        random.randint(5, 50)
    ]

    print()


# Final Result
print("\nBest Solution Found")
print("----------------------")

print(
    f"Best Number of Neurons: {best_neurons}"
)

print(
    f"Best MSE: {best_score}"
)


# Final Prediction below optional can delete
final_predictions = best_model.predict(X_test)

print("\nActual vs Predicted Product Yield")
print("----------------------------------")

for actual, predicted in zip(
    y_test.values,
    final_predictions
):

    print(
        f"Actual: {actual:.2f} | Predicted: {predicted:.2f}"
    )