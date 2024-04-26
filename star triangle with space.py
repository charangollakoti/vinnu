# height = 5  # Change the height as needed
#
# for i in range(1, height + 1):
#     spaces = '  ' * (height - i)
#     stars = ' *' * i
#     print(spaces + stars)

height = 7  # Change the height as needed

for i in range(1, height + 1):
    spaces = ' ' * (height - i)
    stars = ' *' * i

    if i > 2 and i < height:
        middle_stars = ' *' + '  ' * (i - 2) + ' *'
    else:
        middle_stars = stars

    print(spaces + middle_stars)
