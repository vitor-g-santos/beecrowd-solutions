# Problem: https://www.beecrowd.com.br/repository/UOJ_1238.html | Made by: Vitor Góes

#
# Input Logic
#

array_amount = int(input())
arrays = []

for index in range(array_amount):
    lines_amount = int(input())
    lines = []
    for index in range(lines_amount):
        lines.append(input())
    arrays.append(lines)

#
# Output Logic
#

for array in arrays:
    language = array[0]
    for string in array:
        if string != language:
            language = "ingles"
            break
    print(language)