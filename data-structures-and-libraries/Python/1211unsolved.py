# Problem: https://www.beecrowd.com.br/repository/UOJ_1211.html | Made by: Vitor Góes

while True:

#
# Input Logic
#

    try: line_amount = int(input())
    except EOFError: break

    lines = []
    for i in range(line_amount):
        lines.append(input())

#
# Output Logic
#

    duplicated_values = 0
    last_number = lines[-1]

    for number in lines:
        for value in range(len(number)):
            if number[value] == last_number[value]:
                duplicated_values += 1
            else:
                break
        last_number = number

    print(duplicated_values)