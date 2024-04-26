
# simplest form of pascals triangle
rows = 5

for i in range(rows):
    num = 1
    for j in range(1, i + 2):
        print(num, end=" ")
        # pascals formula
        num = num * (i + 1 - j) // j
    print()






# num_rows = 6
#
# triangle = []
# for row_num in range(num_rows):
#     row = [None] * (row_num + 1)
#     row[0] = 1
#     row[-1] = 1
#
#     for j in range(1, len(row) - 1):
#         row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
#
#     triangle.append(row)
#
# for row in triangle:
#     print(" ".join(str(num) for num in row).center(80))
