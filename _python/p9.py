 #Program to create a multiplication table of a number 

number= int(input('Enter the number to create multiplication table '))
print('multiplication table of', number)
for i in range(1,11):
    print(number,"X",i,"=", number*i)