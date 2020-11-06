lis = [1,2,3]
while lis:
    print(lis.pop(0))


dict = {1:"eins", 2:"zwei",3:"drei"}
liste = list(dict.keys())
for key in liste:
    print(key, dict[key])