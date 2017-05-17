# In this Google foobar problem we are tasked with finding the maximum value of
# the power from the solar rays that we can get. However if were given only one item
# we must return that one item only even if its a negative number.
# ----------------------------------------------------------------
# -Tony Pallone

import random

def answer(xs):
    Set = False
    Max = 1
    neg = []
    if len(xs) == 1:
        return str(xs[0])
    while 0 in xs:
        xs.remove(0)
    for i in range(len(xs)):
        if(xs[i] < 0):
            neg.append(xs[i])
    for i in range(len(neg)):
        xs.remove(neg[i])
    neg.sort()
    if len(neg) % 2 == 0 and len(neg) > 0:
        Max = 1
        Set = True
        for i in range(len(neg)):
            Max *= neg[i]
    if len(neg) % 2 == 1 and len(neg) > 1:
        neg.remove(max(neg))
        Max = 1
        Set = True
        for i in range(len(neg)):
            Max *= neg[i]
    Max = 1
    for i in range(len(xs)):
        if xs[i] > 0 and Set == False:
            Max *= xs[i]
            Set = True
        elif xs[i] > 0 and Set == True:
            Max *= xs[i]
    if len(xs) == 0:
        return str(0)
    return(str(Max))


xs = [-1]
print(answer(xs))
xs = [0,0]
print(answer(xs))
for j in range(5):
    for i in range(j+5):
        xs.append(random.randint(-9,9))
    print (xs)
    print(answer(xs)+ "\n")
    xs = []
    
