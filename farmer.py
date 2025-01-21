from scipy.optimize import linprog

profit_coeff = [-200, -150]
constraints = [
    [20, 10],
    [10, 15]
]
resources = [1200, 600]

result = linprog(c=profit_coeff, A_ub=constraints, b_ub=resources, bounds=[(20, None), (10, None)], method="highs")

optimal_wheat= result.x[0]
optimal_barley = result.x[1]
max_profit = -result.fun

print(f"Optimal number of wheat: {optimal_wheat:.0f}")
print(f"Optimal number of barley: {optimal_barley:.0f}")
print(f"Maximum profit: {max_profit:.2f}")
