nums = [int(x) for x in input().split(' ')]

calc1 = nums[0] * nums[1]
calc2 = nums[2] * nums[3]

if calc1 == calc2:
    print(0)
elif calc1 > calc2:
    print(-1)
else:
    print(1)
    
