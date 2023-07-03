# Problem: https://www.beecrowd.com.br/repository/UOJ_1478.html | Made by: Vitor Góes

while True:

#
# Input Logic
#

    dimension = int(input())
    if dimension == 0:
        break

#
# Output Logic
#

    x = 1
    for y in range(1, dimension+1):
        x_index = 0

        while x != 1:
            if x_index != 0 and x_index != dimension:
                print(end=" ")
            print(f"{' '*(3-len(str(x)))}{x}", end="")
            x -= 1
            x_index += 1
        while x_index != dimension:
            if x_index != 0 and x_index != dimension:
                print(end=" ")
            print(f"{' '*(3-len(str(x)))}{x}", end="")
            x += 1
            x_index += 1

        x = y+1
        print(end="\n")