# Problem: https://www.beecrowd.com.br/repository/UOJ_2757.html | Made by: Vitor Góes

#
# Input Logic
#

var1 = int(input())
var2 = int(input())
var3 = int(input())

#
# Output Logic
#

def sAmount (value, char):
    return char*(10-len(str(value)))