"""
What does this code do?
-----------------------
Basically this script will receive a few numbers, and
return neither the biggest, nor the smallest, but the
middle one.

Example: Input = 3 4 5 6 7 | Output: 5
"""

#Receiving the numbers and spliting them by spaces
num = [int(x) for x in input().split(' ')]

#Keeps removing the biggest and the smallest number until the total amount of numbers is below 3
while len(num) > 2: #len() is used to get the total amount of elements inside a list
    num.remove(max(num)) #Remove the biggest number
    num.remove(min(num)) #Remove the smallest number

#Writes the output (num[0], because it will always be filled with a number)
print(num[0])
