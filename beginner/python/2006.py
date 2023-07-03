real = int(input())
escolha = [int(x) for x in input().split(' ')]
result = 0

for x in range(5):
    if escolha[x] == real:
        result += 1
        
print(result)
