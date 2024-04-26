matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows = len(matrix)
cols = len(matrix[0])
for i in range(cols):
    for j in range(rows):
        if j > i:
            print(matrix[j][i], end=" ")
        else:
            print(matrix[j][i], end=" ")
    print()
