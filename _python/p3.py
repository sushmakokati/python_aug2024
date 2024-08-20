# Accept a number as input,say X and define a logic to get the output sayy.the input can be only 0 or 1 and the output must be 1 if input is 0 and viceverse
X = int(input('enter the input numbner(0 or 1 only):'))
if X!=0 or X!=1:
    print('Invalid input')
else:
    Y = 1-X
    print(f'input number={X},output number ={Y}')   