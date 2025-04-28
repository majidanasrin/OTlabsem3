def hungarian_algorithm(cost_matrix):
    n = len(cost_matrix)

    # Step 1: Row reduction
    for i in range(n):
        min_val = min(cost_matrix[i])
        for j in range(n):
            cost_matrix[i][j] -= min_val

    # Step 2: Column reduction
    for j in range(n):
        min_val = min(cost_matrix[i][j] for i in range(n))
        for i in range(n):
            cost_matrix[i][j] -= min_val

    # Step 3: Assignment
    assigned = [-1] * n
    taken = [False] * n

    for i in range(n):
        for j in range(n):
            if cost_matrix[i][j] == 0 and not taken[j]:
                assigned[i] = j
                taken[j] = True
                break

    return assigned

# --- Example usage (directly without if __name__ == "__main__") ---

cost_matrix = [
    [4, 2, 8],
    [2, 3, 7],
    [3, 1, 6]
]

assignment = hungarian_algorithm([row[:] for row in cost_matrix])  # pass a copy
total_cost = 0

print("Task -> Worker assignments:")
for task, worker in enumerate(assignment):
    print(f"Task {task} assigned to Worker {worker}")
    total_cost += cost_matrix[task][worker]

print(f"\nTotal minimum cost: {total_cost}")
