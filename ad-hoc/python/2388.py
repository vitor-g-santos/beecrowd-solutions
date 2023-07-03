quantidade = int(input())
valores = []
result = 0

for i in range(quantidade):
    valores.append([int(x) for x in input().split(' ')])
    
for line in valores:
    result += (line[0] * line[1])
    
print(result)
