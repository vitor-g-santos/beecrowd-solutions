seg = int(input())

h= seg//3600
seg%= 3600
m= seg//60
seg%= 60

print (f"{h}:{m}:{seg}")
