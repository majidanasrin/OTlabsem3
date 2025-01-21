from scipy.optimize import linprog

profit_coeff = [-5, -3]
constraints = [
    [2,1],
    [1, 1]
]
resources = [500, 400]

result = linprog(c=profit_coeff, A_ub=constraints, b_ub=resources, bounds=[(100, None), (50, None)], method="highs")

optimal_choco = result.x[0]
optimal_vanilla = result.x[1]
max_profit = -result.fun

print(f"Optimal number of chocolate cakes: {optimal_choco:.0f}")
print(f"Optimal number of vanilla cakes: {optimal_vanilla:.0f}")
print(f"Maximum profit: {max_profit:.2f}")
