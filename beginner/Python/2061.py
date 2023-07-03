abas = [int(x) for x in input().split(' ')]
result = abas[0]

for i in range(abas[1]):
    user = input()
    if user == "fechou":
        result = (result-1)+2
    else:
        result -= 1
        
print(result)
