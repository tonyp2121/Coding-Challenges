import string
digs = string.digits + string.letters

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
    listOfZ = [n]
    var5 = n
    length = len(n)
    Found = False
    Count = 0
    while not False:
        values = map(int, var5)
        descending = list(values)
        ascending = list(values)
        descending.sort(reverse=True)
        descending = "".join(str(x) for x in descending)
        ascending.sort()
        ascending = "".join(str(x) for x in ascending)
        var1 = int(var5,b)     #in our code X = descending Y = ascending z = var2 = x -y
        var2 = int(ascending,b)
        var3 = int(descending,b)
        var4 = var3-var2  #var 4 is our z now now we need to do it forever.
        var5 = int2base(var4,b)
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
