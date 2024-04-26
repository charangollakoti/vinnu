num_rows = 3 + 2

if num_rows % 2 == 0:
    num_rows += 1
# Make sure it's an odd number of rows

# Upper part of the diamond
for i in range(1, num_rows + 1, 2):
    print(" " * ((num_rows - i) // 1) + "* " * i)

# Lower part of the diamond
for i in range(num_rows - 2, 0, -2):
    print(" " * ((num_rows - i) // 1) + "* " * i)
