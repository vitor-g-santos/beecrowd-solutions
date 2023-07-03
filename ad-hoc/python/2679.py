# Problem: https://www.beecrowd.com.br/repository/UOJ_2679.html | Made by: Vitor Góes

#
# Input Logic
#

number = int(input())

#
# Output Logic
#

if number % 2 == 0:
    print(number+2)
else:
    print(number+1)