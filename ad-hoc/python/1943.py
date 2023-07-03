num = int(input())

if num == 1:
    print("Top 1")
elif num <= 3:
    print("Top 3")
elif num <= 5:
    print("Top 5")
elif num <= 10:
    print("Top 10")
elif num <= 25:
    print("Top 25")
elif num <= 50:
    print("Top 50")
else:
    print("Top 100")
