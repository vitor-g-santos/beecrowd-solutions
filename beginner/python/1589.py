quant = int(input())
casos = []
result = []

for i in range(quant):
    casos.append([int(x) for x in input().split(' ')])
    
for line in casos:
    result.append(line[0]+line[1])
        
for i in range(quant):
    print(result[i])
