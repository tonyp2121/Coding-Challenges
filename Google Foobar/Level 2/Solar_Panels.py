def answer(xs):
    Set = False
    Max = 1
    neg = []
    if len(xs) == 0:
        return str(0)
    for i in range(len(xs)):
        if(xs[i] < 0):
            neg.append(xs[i])
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
    for i in range(len(xs)):
        if xs[i] > 0 and Set == False:
            Max *= xs[i]
            Set = True
        elif xs[i] > 0 and Set == True:
            Max *= xs[i]
    return(str(Max))

xs = [1, 0, 5, -2, -3]
print(answer(xs))
xs = [-1, -4, 2, -2, -3]
print(answer(xs))
xs = []
print(answer(xs))
