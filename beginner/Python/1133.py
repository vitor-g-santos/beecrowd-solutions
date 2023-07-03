# Problem: https://www.beecrowd.com.br/repository/UOJ_1133.html | Made by: Vitor Góes

#
# Input Logic
#

value_min = abs(int(input()))
value_max = abs(int(input()))

#
# Output Logic
#

if value_min > value_max:
    value_buffer = value_min
    value_min = value_max
    value_max = value_buffer
for index in range(value_min+1, value_max):
    if index % 5 == 2 or index % 5 == 3:
        print(index)