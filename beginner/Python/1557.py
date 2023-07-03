# Problem: https://www.beecrowd.com.br/repository/UOJ_1557.html | Made by: Vitor Góes

#
# Input Logic
#

from math import ceil, log10

values = [] # Declares the Input Array
number = 1 # Declares the Input Buffer

while number != 0:
    number = int(input())
    if number == 0:
        break
    values.append(number)

#
# Output Logic
#

for value in values:
    line_start_value = 1
    for x in range(value): # Amount of Lines
        line = [line_start_value]
        for y in range(value-1):
            line_start_value *= 2
            line.append(line_start_value)

        if x == 0:
            matrix_max_digits = ceil(log10(pow(line_start_value, 2)))
            matrix_max = pow(line_start_value, 2)
        
        index = 1
        for item in line:
            if index == value:
                end_var = ""
            else:
                end_var = " "
            if ceil(log10(item)) < matrix_max_digits and value > 1:
                if item == 1:
                    item = f"{' '*(matrix_max_digits-ceil(log10(item))-1)}{item}"
                else:
                    item = f"{' '*(matrix_max_digits-ceil(log10(item)))}{item}"
            else:
                item = item
            print(item, end=end_var)
            index += 1

        print(end="\n")

        for y in range(value-2):
            line_start_value //= 2
    print(end="\n")