print("Prim Algorithm")
inf = 1000

w = [
    [0, 1, 3, inf, inf],
    [1, 0, 3, 6, inf],
    [3, 3, 0, 4, 2],
    [inf, 6, 4, 0, 5],
    [inf, inf, 2, 5, 0]
]

n = len(w)  
F = set()   
nearest = [-1] * n  
distance = [inf] * n  


for i in range(1, n):
    nearest[i] = 0
    distance[i] = w[0][i]

included = {0}  

while len(F) < n - 1:
    min_dist = inf
    u = -1
    for i in range(1, n):
        if distance[i] < min_dist and i not in included:
            min_dist = distance[i]
            u = i

    if u != -1: 
        F.add((nearest[u], u))
        included.add(u)

        for v in range(n):
            if w[u][v] < distance[v] and v not in included:
                distance[v] = w[u][v]
                nearest[v] = u

print("Weight Matrix:")
for row in w:
    print(" ".join(f"{x:5}" for x in row))
print("\nEdges in the MST:")
print(F)