import math

def tsp(graph, visited, currcity, visitedcity, totcost, mincost):
    if visitedcity == len(graph):
        return totcost + graph[currcity][0] if graph[currcity][0] > 0 else math.inf
    
    for nextcity in range(len(graph)):
        if not visited[nextcity] and graph[currcity][nextcity] > 0:
            visited[nextcity] = True
            mincost = min(
                mincost,
                tsp(graph, visited, nextcity, visitedcity + 1, totcost + graph[currcity][nextcity], mincost)
            )
            visited[nextcity] = False
    return mincost

def findtsp(graph):
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    return tsp(graph, visited, 0, 1, 0, math.inf)

total = int(input("Total no. of cities to visit: "))
cost = []
print("Enter cost of travelling from i to j as arr[i][j]: ")
for i in range(total):
    row = list(map(int, input().split()))
    cost.append(row)

result = findtsp(cost)
print("Minimum cost of TSP is ", result if result != math.inf else "No solution possible")
