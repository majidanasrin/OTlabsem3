def knapsack(W, w, v, n):
    DP = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if w[i - 1] <= j:
                DP[i][j] = max(DP[i - 1][j], v[i - 1] + DP[i - 1][j - w[i - 1]])
            else:
                DP[i][j] = DP[i - 1][j]

    return DP[n][W]

n = 4
W = 7
w = [1, 3, 4, 5]
v = [1, 4, 5, 7]

max_value = knapsack(W, w, v, n)
print("Maximum value of knapsack: ", max_value)


