max_value = int(input())
value = 1
for x in range(1, max_value+1):
    for y in range(2):
        print("{0} {1} {2}".format(value, value*value+y, value*(value*value)+y))
    value += 1
