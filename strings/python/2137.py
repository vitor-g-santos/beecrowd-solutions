# Problem: https://www.beecrowd.com.br/repository/UOJ_1169.html | Made by: Vitor Góes

# This code should run until the user cancel the input (ctrl+c, etc)
while True:

#
# Input Logic
#
    try:
        line_amount = int(input())
    except:
        break

    lines = []
    for x in range(line_amount):
        lines.append(input())

#
# Output Logic
#

    lines.sort()
    for string in lines:
        print(string)