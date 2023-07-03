dados = [int(x) for x in input().split(' ')]

calc = dados[1]-dados[0]*dados[2]

if calc >= 0:
    print("S")
else:
    print("N")
