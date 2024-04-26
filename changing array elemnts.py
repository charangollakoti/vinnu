n, k = map(int, input("Enter the length of the list and the number of positions to rotate: ").split())
lst = list(map(int, input("Enter the elements of the list: ").split()))

k = k % n
rotated_lst = lst[-k:] + lst[:-k]

print("The rotated list is:", end=" ")
for num in rotated_lst:
    print(num, end=" ")

