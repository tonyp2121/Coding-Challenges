def answer(n,b): #where n is minion id and b is base
    length = len(n)
    values = map(int, n)
    descending = list(values)
    ascending = list(values)
    descending.sort()
    ascending.sort(reverse=True)
    var1 = int(n,b)
    var2 = []
    for i in range (len(descending)):
        var2.append(descending[i] - ascending[i])
    print(var1)
    
answer("11",2)
