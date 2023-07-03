# Problem: https://www.beecrowd.com.br/judge/pt/problems/view/2694 | Made by: Vitor Góes

#
# Input Logic
#

line_amount = int(input())

lines = []
for x in range(line_amount):
    lines.append(input())

#
# Output Logic
#

for string in lines:
    result = 0

    result_buffer = "0"
    for index in range(13):
            if string[index].isnumeric():
                result_buffer += string[index]
                if index == 12: result += int(result_buffer)
            else:
                result += int(result_buffer)
                result_buffer = "0"
    
    print(result)