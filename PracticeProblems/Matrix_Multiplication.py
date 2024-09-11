def matrix_multiplication(a,b):
    
    row_a, col_a = len(a), len(a[0])
    row_b, col_b = len(b), len(b[0])

    if row_a != col_b:
        print("Error")

    result = [[0 for a in range(col_b)] for b in range(row_a)]

    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                result[i][j] += a[i][k] + b[k][j]

    return result

a = [[1,2], [3,4]]
b = [[4,1], [1,0]]

print(matrix_multiplication(a,b))