# # Taking input
# length, target = map(int, input().split())
# arr = list(map(int, input().split()))
#
# ans = []
# for i in range(length - 1):
#     for j in range(i + 1, length):
#         if arr[i] + arr[j] == target:
#             ans.extend([arr[i], arr[j]])
#
# # Printing output
# if len(ans) == 0:
#     print("No pairs found")
# else:
#     print(*ans)
# length, target = map(int,input().split())
# arr = list(map(int,input().split()))
#
# ans = []
#
# for i in range(length - 1):
#     for j in range(i + 1, length):
#         if arr[i] + arr[j] == target:
#             ans.extend([arr[i], arr[j]])
#
# if len(ans) == 0:
#     print("No pairs found")
# else:
#     print(*ans)


