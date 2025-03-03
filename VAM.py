import numpy as np

def vam(cost_matrix, supply, demand):
    cost_matrix = np.array(cost_matrix)
    supply = np.array(supply)
    demand = np.array(demand)
    allocation = np.zeros_like(cost_matrix)

    while np.any(supply > 0) and np.any(demand > 0):
        row_penalties = []
        for row in range(len(supply)):
            if supply[row] > 0:
                available_costs = cost_matrix[row][demand > 0]
                if len(available_costs) > 1:
                    sorted_costs = np.sort(available_costs)
                    row_penalties.append(sorted_costs[1] - sorted_costs[0])
                else:
                    row_penalties.append(available_costs[0])
            else:
                row_penalties.append(float('-inf'))

        col_penalties = []
        for col in range(len(demand)):
            if demand[col] > 0:
                available_costs = cost_matrix[supply > 0, col]
                if len(available_costs) > 1:
                    sorted_costs = np.sort(available_costs)
                    col_penalties.append(sorted_costs[1] - sorted_costs[0])
                else:
                    col_penalties.append(available_costs[0])
            else:
                col_penalties.append(float('-inf'))

        max_row_penalty = max(row_penalties)
        max_col_penalty = max(col_penalties)

        if max_row_penalty >= max_col_penalty:
            row = row_penalties.index(max_row_penalty)
            col = np.argmin(cost_matrix[row][demand > 0])
        else:
            col = col_penalties.index(max_col_penalty)
            row = np.argmin(cost_matrix[supply > 0, col])

        allocation_amount = min(supply[row], demand[col])
        allocation[row][col] = allocation_amount
        supply[row] -= allocation_amount
        demand[col] -= allocation_amount

    return allocation

cost_matrix = [[19, 30, 50], [70, 30, 40], [40, 8, 70]]
supply = [50, 60, 50]
demand = [30, 90, 40]

allocation = vam(cost_matrix, supply, demand)

print("Optimal Transportation plan:")
print(allocation)
