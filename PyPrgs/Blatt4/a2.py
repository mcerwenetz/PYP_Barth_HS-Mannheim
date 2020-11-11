
def unique(liste: list) -> list:
    listeRet = []
    for x in liste:
        if x not in listeRet:
            listeRet.append(x)
    return listeRet

g = 30
dic = {}
dic = { (x,y,a,b):sum((pow(x,3),pow(y,3))) 
for x in range(1,g+1) for y in range(1,g+1) for a in range(1,g+1) for b in range(1,g+1) 
if sum((pow(x,3),pow(y,3))) == sum((pow(a,3),pow(b,3))) 
# and x != y and x != a and x != b and y != a and y !=b and b != a}
and x not in [y,a,b]
and y not in [x,a,b]
and a not in [x,y,b]
and b not in [x,y,a]
}

print(dic)

# print unique cabnumbers
print(unique(list(dic.values())))
