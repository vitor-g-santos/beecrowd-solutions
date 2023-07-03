# Problem: https://www.beecrowd.com.br/repository/UOJ_1197.html | Made by: Vitor Góes

while True:

#
# Input Logic
#

    try: time, velocity = map(int, input().split(' '))
    except EOFError: break

#
# Output Logic
#

    print(velocity * time * 2)