# program to accept 3 distinct numbers and find smallest among them
# check if valid input
input_num1 = int(input('Enter 1st number'))
input_num1 = int(input('Enter 2st number'))
input_num1 = int(input('Enter 3st number'))

if input_num1 < input_num2 and input_num1 < input_num3:
    print(f"{input_num1} is smallest")
elif input_num2 < input_num3:
    print(f'{input_num2}is smallest')
else:
    print(f'{input_num3}is smallest')
