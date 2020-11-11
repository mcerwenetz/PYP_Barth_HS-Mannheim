# sein Beispiel
# print(list(zip((1,2,3,4),(5,6), (7,8))))
eingabeliste = [(1, 5, 7), (2, 6, 8), (3,1,5), (81, 6 ,37, 5)]

# einfaches Beispiel
# print(list(zip((1,3,5),(2,4,6))))
# Todo: Macht es überhaupt das was es soll?
# Todo: Was ist wenn die Eingabetupel unterschiedliche Dimensionen haben
# Todo: Warum range von tupelanzahl nicht tupelanzahl +1

def unzip(eingabeliste: list) -> list:
    tupelanzahl =len(eingabeliste)
    # minimum aller längen aller tupel
    n = min(map(len,eingabeliste))
    endliste = []
    for i in range(tupelanzahl):
        # nimm von jedem tupel 0..tupelanzahl die stelle 0..n
        # aber nur wenn i < n.
        # es kann passieren dass ein tupel länger ist als die anderen
        # erstelle anhand der liste aller eingabewerte an stelle i nochmal ein tupel.
        # dieses tupel ist dann ein element in der ergebnisliste
        endliste.append(tuple([tup[i] for tup in eingabeliste if i < n ]))
    
    # wunderschön. wenn t = True was es nur ist wenn's nicht leer ist, dann drinne lassen.
    endliste=[t for t in endliste if t]
    return endliste



print(unzip(eingabeliste))

