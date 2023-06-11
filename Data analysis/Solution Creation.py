from sympy import symbols, solve

def solve_equation():
    x = symbols('x')
    equation = x**2 + 3*x - 10
    solution = solve(equation, x)
    return solution

equation_solution = solve_equation()
print("Equation Solution:", equation_solution)
