# simple matrix multiplication syntax
matrixrow = int(input())
matrixcol = int(input())
matrix1row = int(input())
matrix1col = int(input())

# first matrix
matrix = []
for i in range(matrixrow):
    rows = list(map(int,input().split()[:matrixcol]))
    matrix.append(rows)
# second matrix
matrix1 = []
for i in range(matrix1row):
    rows = list(map(int,input().split()[:matrix1col]))
    matrix1.append(rows)
# multi statement

result = [[sum(x * y for x, y in zip(i, j)) for j in zip(*matrix1)] for i in matrix]
for i in result:
    print(*i)
result = [[sum(x * y for x, y in zip(i, j)) for j in zip(*matrix1)] for i in matrix]
#
#
# # second method
# firstmatrixrows = 3
# firstmatrixcols = 3
# secondmatrixrows = 3
# secondmatrixcols = 3
# firstmatrix = []
# secondmatrix = []
#
# for i in range(firstmatrixrows):
#     rows = list(map(int,input().split()[:firstmatrixrows]))
#     firstmatrix.append(rows)
# for i in range(secondmatrixrows):
#     rows = list(map(int,input().split()[:secondmatrixcols]))
#     secondmatrix.append(rows)
#
# result = [[sum(x * y for x, y in zip(row, col)) for col in zip(*secondmatrix)] for row in firstmatrix]
#
# for row in result:
#     print(row)
#
#
#
#
# # third method
# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]
#
# if len(matrix1[0]) != len(matrix2):
#     raise ValueError()
#
# result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
#
# for i in range(len(matrix1)):
#     for j in range(len(matrix2[0])):
#         for k in range(len(matrix2)):
#             result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
#
# for row in result_matrix:
#     print(row)
