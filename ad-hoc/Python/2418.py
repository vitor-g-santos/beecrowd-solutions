val = [float(x) for x in input().split(' ')]
result = 0

val.remove(max(val))
val.remove(min(val))

for item in val:
    result += item
    
print(f"{result:.1f}")
