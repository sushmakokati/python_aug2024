import math

input_num = int(input('Enter a number to check if it is Perfect Square: '))
root_number = input_num ** 0.5
# root_number = math.sqrt(input_number)
root_number = math.floor(root_number) # int(root_number)
if root_number * root_number == input_num:
    print(f'{input_num} is a Perfect Square')
else:
    print(f'{input_num} is not a Perfect Square')