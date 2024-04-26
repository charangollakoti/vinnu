matrix = [
    [1, 2, 3, 4],
    [3, 5, 6, 7],
    [2, 2, 8, 9],
    [1, 10, 4, 10]
]

rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        if j < i:
            print(0, end=" ")
        else:
            print(matrix[i][j], end=" ")
    print()
