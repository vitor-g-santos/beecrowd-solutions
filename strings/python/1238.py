# Problem: https://www.beecrowd.com.br/repository/UOJ_1238.html | Made by: Vitor Góes

#
# Input Logic
#

input_amount = int(input())

lines = []
for index in range(input_amount):
    a, b = map(str, input().split(' '))
    lines.append([a, b])

#
# Output Logic
#

for string in lines:
    string_buffer = ""
    min_string = min(string, key=len)
    min_string_size = len(min_string)
    max_string = max(string, key=len)
    max_string_index = string.index(max_string)

    for index in range(len(min_string)):
        string_buffer += string[0][index]
        string_buffer += string[1][index]
    
    if (len(max_string)-len(min_string)) != 0:
        string_buffer += string[max_string_index][min_string_size:]

    print(string_buffer)