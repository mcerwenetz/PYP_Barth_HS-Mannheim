# sein Beispiel
# print(list(zip((1,2,3,4),(5,6), (7,8))))
eingabeliste = [(1, 5, 7), (2, 6, 8)]

# einfaches Beispiel
# print(list(zip((1,3,5),(2,4,6))))

def unzip(eingabeliste: list) -> list:
    firstTupel = eingabeliste[0]
    secondTupel = eingabeliste[1]
    ergebnisliste=[]
    for x,y in zip(firstTupel,secondTupel):
        ergebnisliste.append((x,y))
    return ergebnisliste



print(unzip(eingabeliste))

