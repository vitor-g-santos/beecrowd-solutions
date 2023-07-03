dias, saldo = map(int, input().split())
menor_saldo = 10000

for position in range(dias):
    saldo += int(input())
    if saldo < menor_saldo: menor_saldo = saldo
print(menor_saldo)
