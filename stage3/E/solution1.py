# TL, Тест 7: превышение лимита времени

n, k = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]

def multiply_matrices(A, B):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_power(matrix, k):
    result = [[0 if row != col else 1 for col in range(n)] for row in range(n)]
    while k > 0:
        if k % 2 == 1:
            result = multiply_matrices(result, matrix)
            k -= 1
        else:
            matrix = multiply_matrices(matrix, matrix)
            k //= 2
    for i in range(n):
        for j in range(n):
            result[i][j] = 1 if result[i][j] % 2 == 0 else 0
    return result


for row in matrix_power(matrix, k):
    print(''.join(map(str, row)))
