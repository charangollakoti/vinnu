array = list(map(int, input().split()))
x = int(input("Enter the element to search: "))

def binarysearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

result = binarysearch(array, x, 0, len(array) - 1)
print(result)
