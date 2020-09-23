import numpy as np 
import random
import math
import time
x = []
while(len(x) <= 1000000):
    x.append(random.randrange(1,100000000000))
x = np.sort(x)
print(x)
target = int(input('What number are you lookin for? '))
startTime = time.time()
for i in x:
    if (target == i):
       print(time.time() - startTime)

found = False
startTime = time.time()
while(len(x) > 1):
    if (x[math.ceil(len(x)/2)] == target):
        print(x[math.ceil(len(x)/2)])
        found = True
        print(time.time()-startTime)
        break
    elif(x[math.ceil(len(x)/2)] > target):
        x = np.array_split(x,2)[0]
    else:
        x = np.array_split(x,2)[1]


if ( not found):    
    print('Number was not in list')