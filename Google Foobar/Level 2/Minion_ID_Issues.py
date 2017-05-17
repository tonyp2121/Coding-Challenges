# So this issue on foobar was actually called "Hey I Already Did That!"
# But anyways the issue here is how ID numbers are assigned to minions in that there are many cases where the ID number
# will repeat forever and ever. What it does is it takes a number in a given base, sorts each letter in Ascending and Descending order
# and the new ID number will be the number resulting from Descending - Ascending order.
# this depending upon inputs will go in a loop that goes on forever or goes to a constant eventually which cant be worked with anymore.
# -------------------------------------------------------------------------------------------------------------------------------------
# -Tony Pallone

import string
digs = string.digits + string.letters

def int2base(x, base):  #code thanks to stack overflow 
    if x < 0:           #this program takes an integer value and returns it into a string in any base given.
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

def answer(n,b): #where n is minion id and b is base
    listOfZ = [n]
    var5 = n
    length = len(n)
    Count = 0
    while True:
        values = map(int, var5)
        descending = list(values)
        ascending = list(values)
        descending.sort(reverse=True)
        descending = "".join(str(x) for x in descending)
        ascending.sort()
        ascending = "".join(str(x) for x in ascending) #in our code X = descending Y = ascending z = var2 = x -y
        var2 = int(ascending,b)
        var3 = int(descending,b)
        var3 -= var2  #var 4 is our z now now we need to do it forever.
        var5 = int2base(var3,b)
        Count += 1
        if len(var5) == 1:
            return 1
        for i in range(len(listOfZ)):
            if var5 == listOfZ[i]:
                return Count - i
        var5.zfill(length)
        print(var5)
        listOfZ.append(var5)
        
print(answer("210022",3))
