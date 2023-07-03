# Problem: https://www.beecrowd.com.br/repository/UOJ_1161.html | Made by: Vitor Góes

while True:

#
# Input Logic
#

    try: a, b = map(int, input().split(' '))
    except EOFError: break

#
# Output Logic
#

    acalc = 1
    bcalc = 1
    for value in range(1, (a if a > b else b)+1):
        if value <= a:
            acalc *= value
        if value <= b:
            bcalc *= value

    print(acalc + bcalc)