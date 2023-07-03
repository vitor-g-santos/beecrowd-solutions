linha_verificar = int(input())
tipo_calculus = input()

matrix = [] # Initialize the Matrix

#
# Input Logic
#

for row in range(12):
    row_holder = []
    for column in range(12):
        row_holder.append(float(input()))
    matrix.append(row_holder)

#
# Output Logic
#

result = 0

for value in matrix[linha_verificar]:
    result += value

if tipo_calculus == "M":
    result /= 12

print(result)
