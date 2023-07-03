valores = [int(input()) for x in range(5)]
result = 0

valores[0] *= 300
valores[1] *= 1500
valores[2] *= 600
valores[3] *= 1000
valores[4] *= 150

for i in range(5):
    result += valores[i]
    
print(result+225)
