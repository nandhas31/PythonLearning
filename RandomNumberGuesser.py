import random

num = (random.randrange(0,21))
print(num)
userNum = int(input('Enter a number between 0 and 20: '))
found = False
if ((type(userNum) is int) & (num is userNum)):
    print('Wow! First Try!')
else:
    while (not found):
        userNum = int(input('Try Again: '))
        if ((type(userNum) is int) & (num is userNum)):
            print('Good Job!')
            found = True
