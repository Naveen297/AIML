import random

def objective_function(x):
    return -1 * (x ** 2)  # A simple quadratic function with maximum at x=0

def hill_climbing(start, step_size, iterations, objective_function):
    current_solution = start
    current_value = objective_function(current_solution)

    for i in range(iterations):
        next_solution = current_solution + step_size * (1 if random.choice([True, False]) else -1)
        next_value = objective_function(next_solution)

        if next_value > current_value:
            current_solution = next_solution
            current_value = next_value

    return current_solution, current_value

if __name__ == "__main__":
    start = random.randint(-10, 10)
    step_size = 0.1
    iterations = 1000

    solution, value = hill_climbing(start, step_size, iterations, objective_function)
    print(f"Found solution: {solution}, with value: {value}")
