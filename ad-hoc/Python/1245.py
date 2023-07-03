# Problem: https://www.beecrowd.com.br/repository/UOJ_1245.html | Made by: Vitor Góes

while True:

#
# Input Logic
#

    try: line_amount = int(input())
    except EOFError: break

    lines = []
    for index in range(line_amount):
        a, b = map(str, input().split())
        a = int(a)

        lines.append([a, b])

#
# Output Logic
#

    total = 0
    found_pair = True
    while len(lines) > 0:
        first_pair = lines[0]
        lines.pop(0)
        for index, line in enumerate(lines):
            if line[0] == first_pair[0] and line[1] != first_pair[1]:
                found_pair = True
                lines.pop(index)
                total += 1
                break
            else:
                found_pair = False

    print(total)