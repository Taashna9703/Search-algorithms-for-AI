import random

def objective_function(x):
    return -(x ** 2) + 10 * x + 5

def hill_climbing(initial_solution, step_size, max_iterations):
    current_solution = initial_solution
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        neighbor_solution = current_solution + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor_solution)

        if neighbor_value > current_value:
            current_solution = neighbor_solution
            current_value = neighbor_value

    return current_solution, current_value

initial_solution = 0  
step_size = 0.1       
max_iterations = 100  

best_solution, best_value = hill_climbing(initial_solution, step_size, max_iterations)
print("Best Solution:", best_solution)
print("Best Value:", best_value)

