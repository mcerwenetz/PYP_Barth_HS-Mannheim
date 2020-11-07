def ggt(x,y):
    if x is y:
        return x
    elif x > y:
        return ggt(x-y,y)
    else:
        return ggt(y,x)

def ggtIter(x,y):
    while x != y and x%y != 0:
        if x < y:
            x,y = y,x
        if x % y !=  0:
            x %= y
    return y


tupelchen = (3,6)
print(ggtIter(*tupelchen))
