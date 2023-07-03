first = [int(x) for x in input().split(' ')]
stamped = [int(x) for x in input().split(' ')]
cards = [int(x) for x in input().split(' ')]
final = first[1]

for x in stamped:
    for y in cards:
        if x == y:
            final -= 1

if final < 0:
    final = 0
    
print(final)

################################ funcional abaixo:

b = input()
c = [int(x) for x in str(input()).split()]
f = [int(x) for x in str(input()).split()]
final = 0

for i in c:
    if not i in f: final += 1
    
print(final)
