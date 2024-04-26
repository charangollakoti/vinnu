# import numpy as np
matrixrows = int(input("Enter the no of rows of matrix :"))
matrixcols = int(input("Enter the no of cols of matrix :"))
matrix = []
for i in range(matrixrows):
    rows = list(map(int,input().split()[:matrixcols]))
    matrix.append(rows)
# matrix = np.array(matrix)
# print(matrix)
for i in matrix:
    print(*i)
