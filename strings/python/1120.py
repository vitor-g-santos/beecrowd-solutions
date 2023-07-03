# Problem: https://www.beecrowd.com.br/repository/UOJ_2712.html | Made by: Vitor Góes

#
# Input Logic
#

lines = []
while True:
    a, b = map(str, input().split(' '))
    if a == "0" and b == "0":
        break
    lines.append([a, b])

#
# Output Logic
#

for array in lines:
    value = array[0]
    full_number = array[1]

    filtered_full_number = "0"
    for number in full_number:
        if number != value and number.isnumeric:
            filtered_full_number += number
    print(int(filtered_full_number))