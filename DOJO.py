# PYTHON
# DOJO question 1
# rows = 5
# num = 1

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# for i in range(1, rows + 1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()



# DOJO question 2
# rows = 5
#
# for i in range(rows):
#     num = 1
#     for j in range(1, i + 2):
#         print(num, end=" ")
#         # pascals formula
#         num = num * (i + 1 - j) // j
#     print()


# ----------------------------------------------------------------------------------------------------------------
# JAVASCRIPT

# how to console the array without commas and brackets
# let array = [1, 2, 3, 4, 5, 6, 7, 8]
# console.log(array.join(" "))


# print the vowels in the string
# process.stdin.on('data',(data) => {
#     let x = data.toString().trim()
#     vowels = "aeiouAEIOU"
#     array = []
#     for(let i = 0; i < x.length; i++) {
#         if(vowels.includes(x[i])){
#             array += x[i]
#         }
#     }
#     let string = array.split("").join(" ")
#     console.log(string)
# })


# how to get input by line byline
# process.stdin.on("data",(data) => {
#   let x = data.toString().trim()
#   let w = x.split("\n")
# })

