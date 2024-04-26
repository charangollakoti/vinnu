matrixrows = int(input())
matrixcols = matrixrows
matrix = []
for i in range(matrixrows):
    rows = list(map(int,input().split()[:matrixcols]))
    matrix.append(rows)

for i in range(matrixcols):
    matrix[i][i], matrix[i][matrixcols -1 -i] = matrix[i][matrixcols -1 -i], matrix[i][i]

for row in matrix:
    print(*row)
