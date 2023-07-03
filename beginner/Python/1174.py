# Problem: https://www.beecrowd.com.br/repository/UOJ_1174.html | Made by: Vitor Góes

#
# Input Logic
#

lines = []
for x in range(100):
    lines.append(float(input()))

#
# Output Logic
#

ten_or_less_array = []

for index, value in enumerate(lines):
    if value <= 10: ten_or_less_array.append([index, value])

for array in ten_or_less_array:
    print(f"A[{int(array[0])}] = {array[1]:.1f}")