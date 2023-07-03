# Problem: https://www.beecrowd.com.br/repository/UOJ_1162.html | Made by: Vitor Góes

#
# Input Logic
#

item_amount = int(input())
item = []
for x in range(item_amount):
    array_max = int(input())
    array = [int(x) for x in input().split(' ')]
    item.append(array)

#
# Output Logic
#

for line in item:
    steps = 0
    i = 1
    while(i < len(line)):
        currentIndex = i
        while (currentIndex > 0 and line[currentIndex - 1] > line[currentIndex]):
            temp = line[currentIndex]
            line[currentIndex] = line[currentIndex - 1]
            line[currentIndex - 1] = temp
            currentIndex -= 1
            steps += 1
        i += 1
    print(f"Optimal train swapping takes {steps} swaps.")