def matrix_diagonal_sum(matrix: list[list[int]]) -> int:
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]
        sum += matrix[i][::-1][i]
    if len(matrix) % 2 == 1:
        sum -= matrix[len(matrix) // 2][len(matrix) // 2]
    return sum


print(matrix_diagonal_sum(matrix=[[5]]))
