from constraint import Problem, AllDifferentConstrain
def four_queens_problem():
    problem=Problem()
    queens=range(4)
    problem.addVariable("q0",queens)
    problem.addVariable("q1",queens)
    problem.addVariable("q2",queens)
    problem.addVariable("q3",queens)
    problem.addConstraint(AllDifferentConstraint(),{"q0","q1","q2","q3"})
    solutions=problem.getSolutions()
    return solutions

def print_solution(solution):
    for row in range(4):
        for col in range(4):
            if col == solution[f'q{row}']:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


if __name__ == "__main":
    solutions = four_queens_problem()

    if solutions:
        print("Solutions to the 4-Queens problem:")
        for solution in solutions:
            print_solution(solution)
    else:
        print("No solutions found.")
