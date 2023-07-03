# Problem: https://www.beecrowd.com.br/repository/UOJ_2714.html | Made by: Vitor Góes

#
# Input Logic
#

input_amount = int(input())

lines = []
for index in range(input_amount):
    lines.append(input())

#
# Output Logic
#

for string in lines:
    result=""

    string_size = len(string) # Save some memory (and some micro-seconds hehe) by using len only one time (Also, for "purity", i will not use any libraries to make it better)
    if string_size < 20 or string_size > 20:
        print("INVALID DATA") # Error case: is smaller or greater than 20
    elif string[0] != "R" and string[1] != "A":
        print("INVALID DATA") # Error case: Does not begin with "RA"
    else:
        for index in range(2, 20):
            if string[index].isnumeric():
                result += string[index]
            else:
                print("INVALID DATA") # Error case: is not numeric
                break
        if len(result) == 18: # Yes, i used len again, srry
            print(int(result)) # This will remove all zeros before a number