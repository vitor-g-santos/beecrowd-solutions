# Problem: https://www.beecrowd.com.br/repository/UOJ_1140.html | Made by: Vitor Góes

while True:

#
# Input Logic
#

    quote = input()
    if quote == "*": break
    else: quote = quote.split(' ')
#
# Output Logic
#

    initial_letter = quote[0][0].upper()
    is_Tautograms = True
    for index in range(len(quote)):
        if quote[index][0].upper() != initial_letter:
            is_Tautograms = False
            break

    print("Y" if is_Tautograms else "N")