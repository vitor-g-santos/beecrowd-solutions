quant = int(input())
nums = []
last = 0
result = 0

for i in range(quant):
    nums.append(int(input()))

for i in range(len(nums)):
    if nums[i] != last:
        result += 1
        last = nums[i]
    else:
        continue
        
print(result)
