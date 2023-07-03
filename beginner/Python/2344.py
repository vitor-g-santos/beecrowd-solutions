nota = int(input())
result = "E"

if 0 < nota <= 35:
    result = "D"
elif 35 < nota <= 60:
    result = "C"
elif 60 < nota <= 85:
    result = "B"
elif 85 < nota <= 100:
    result = "A"
    
print(result)
