from scipy.optimize import linprog

profit_coeff = [-20, -30]
constraints = [
    [1, 5],
    [3, 1]
]
resources = [125, 80]

result = linprog(c=profit_coeff, A_ub=constraints, b_ub=resources, bounds=[(0, None), (0, None)], method="highs")

optimal_chairs = result.x[0]
optimal_tables = result.x[1]
max_profit = -result.fun

print(f"Optimal number of chairs: {optimal_chairs:.0f}")
print(f"Optimal number of tables: {optimal_tables:.0f}")
print(f"Maximum profit: {max_profit:.2f}")
