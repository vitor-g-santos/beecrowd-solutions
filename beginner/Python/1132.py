# Problem: https://www.beecrowd.com.br/repository/UOJ_1132.html | Made by: Vitor Góes

#
# Input Logic
#

value_min = int(input())
value_max = int(input())

#
# Output Logic
#

calculate = 0

if value_max < value_min:
    value_buffer = value_max
    value_max = value_min
    value_min = value_buffer
for number in range(value_min, value_max+1):
    if number % 13 != 0:
        calculate += number
    
print(calculate)

# Failed: 15 Submissions