inp = [int(x) for x in input().split(' ')]

if inp[0] == 1:
    calc = 4 * inp[1]
elif inp[0] == 2:
    calc = 4.50 * inp[1]
elif inp[0] == 3:
    calc = 5 * inp[1]
elif inp[0] == 4:
    calc = 2 * inp[1]
elif inp[0] == 5:
    calc = 1.50 * inp[1]
    
calc = float(calc)
print (f"Total: R$ {calc:.2f}")
