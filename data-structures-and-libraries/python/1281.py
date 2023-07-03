# Problem: https://www.beecrowd.com.br/repository/UOJ_1281.html | Made by: Vitor Góes

# ! This program does not use a separate code input and/or output!

#
# Input & Output Logic
#

amount = int(input())
for loop in range(amount):
    
    # START - Retrieve the user input and create a new dictionary. This
    # dictionary will contain the name of something and its value.
    dict_amount = int(input())
    dict_values = {}
    
    for index in range(dict_amount):
        a,b = map(str, input().split(' '))
        dict_values[a] = b
    # END

    # START - Retrieve the user input, which contains all the
    # orders and the amount of each order. Check if the order
    # name exists, and if yes, multiply the order value by the
    # amount, then sum it to total_price.
    total_price = 0
    order_amount = int(input())
    for index in range(order_amount):
        a,b = map(str, input().split(' '))
        total_price += float(dict_values.setdefault(a, 0))*int(b)
    # END

    print(f"R$ {total_price:.2f}")

