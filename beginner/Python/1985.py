valores = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}
soma = 0.00

for x in range(int(input())):
    a,b = map(int, input().split())
    valor_acres = valores.get(a)
    soma += valor_acres * b
print(f"{soma:.2f}")
