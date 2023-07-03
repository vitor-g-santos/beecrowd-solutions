dia = int(input())

ano= dia//365
dia%= 365
mes= dia//60
dia%= 60

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
