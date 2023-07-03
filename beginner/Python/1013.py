a, b, c = [int(x) for x in input().split(' ')]

maior = (a+b+abs(a-b))/2
final = (maior+c+abs(maior-c))/2

print ("{:.0f} eh o maior".format(final))
