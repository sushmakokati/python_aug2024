# read a number from the user and check if it is an even number or not
my_number = int(input('enter a number to check if it is Even or not:'))

print(type(my_number))

if my_number % 2==0:
    print(my_number,'is an even number')
else:
    print(f'{my_number}is an Even number')