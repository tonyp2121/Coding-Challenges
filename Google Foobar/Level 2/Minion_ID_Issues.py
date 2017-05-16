import string
digs = string.digits + string.letters

def magic(numList):
    s = ''.join(map(str, numList))
    return int(s)

def int2base(x, base):
    if x < 0:
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
    length = len(n)
    values = map(int, n)
    descending = list(values)
    ascending = list(values)
    descending.sort(reverse=True)
    descending = "".join(str(x) for x in descending)
    ascending.sort()
    ascending = "".join(str(x) for x in ascending)
    var1 = int(n,b)     #in our code X = descending Y = ascending z = var2 = x -y
    var2 = int(ascending,b)
    var3 = int(descending,b)
    var4 = var3-var2  #var 4 is our z now now we need to do it forever.
    var5 = int2base(var4,b)
    
    print(var1)
    print(var2)
    print(descending)
    print(ascending)
    print(var3)
    print(int2base(var4,b))
    count = 0
    
    Found = False;
    #I think its meant to be recursive
    
answer("120",3)
