""" 
dir() gibt eine liste aller attribute eines Objekts zurück
Diese kann man an Objekten selbst definineren:
def __dir__(self):
    return [attr1, attr2]

oder man kann sie sich von anderen Objekten ausgeben lassen

dir(type)

Dazu gehören einerseits magic methods wie __add__() oder __neg__(),
aber auch normale methoden wie z.B. bei list count() oder clear().

Gibt man dir kein Argument kommen die magic functions von dir + die libs
die man inkludiert hat.

"""

#Test der Listenargumente
#liste erstellen
liste=[1,2,3]
#item anhängen. achtung wenn man hier ne liste einfügt wird diese
#als neues item gezählt, nicht jedes item einzeln
liste.append(4)
#inhalt löschen
liste.clear()
liste.append(1)
#liste kopieren
kopie=liste.copy()
#Anzahl von element 1 zaehlen
anzahl=liste.count(1)
#liste erweitern mit noch einer liste
nocheineliste=[2,3,4]
liste.extend(nocheineliste)
#gibt die position eines items in der liste an
postionDrei=liste.index(3)
#Füge die 5 an die zweite stelle ein
liste.insert(1,5)
#Nimm das letzte Element aus der list
letzesItem=liste.pop()
#Nimm das 1 element aus der liste
erstesItem=liste.pop(0)
#element das '3' ist aus der liste entfernen
liste.remove(3)
#liste wieder aufstocken
liste.extend([1,2,3,4,5])
#liste umdrehen
liste.reverse()
#liste sortieren
liste.sort()