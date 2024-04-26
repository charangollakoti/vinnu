rows = int(input())
cols = int(input())
rows1 = int(input())
cols1 = int(input())
matrix = []

for i in range(rows):
    rows = list(map(int,input().split()[:cols]))
    matrix.append(rows)
# first matrix completed
matrix1 = []
for i in range(rows1):
    rows = list(map(int,input().split()[:cols1]))
    matrix1.append(rows)
# second matrix comepleted

# main statement
result = [[matrix[i][j] + matrix1[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

for i in result:
    print(*i)
