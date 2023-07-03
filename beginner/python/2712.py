# Problem: https://www.beecrowd.com.br/repository/UOJ_2712.html | Made by: Vitor Góes

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
    string_size = len(string)

    if string_size < 8 or string_size > 8:
        print("FAILURE") # Error case: is smaller or greater than 8
    elif string[3] != "-":
        print("FAILURE") # Error case: char in index = 3 is different than "-"
    elif not string[0:3].isupper():
        print("FAILURE") # Error case: char in index = 0 to 2 is not Uppercase
    elif not string[4:9].isnumeric():
        print("FAILURE") # Error case: char in index = 4 to 8 is not Numeric
    else:
        if string[-1] == "1" or string[-1] == "2": print("MONDAY")
        if string[-1] == "3" or string[-1] == "4": print("TUESDAY")
        if string[-1] == "5" or string[-1] == "6": print("WEDNESDAY")
        if string[-1] == "7" or string[-1] == "8": print("THURSDAY")
        if string[-1] == "9" or string[-1] == "0": print("FRIDAY")