#program to find prime number
number = int(input('Enter a number'))
if number>1:
    for i in range(2,int(number//2)+1):
        if (number%i)==0:
            print('Number is not prime number')
        else:
            print('Number is  prime number')