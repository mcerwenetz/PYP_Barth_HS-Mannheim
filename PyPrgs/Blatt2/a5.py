de2en = {"eins": "one", "zwei":"two", "drei":"three", 1:"one", 2:"two", 3:"three"}
#Lösche alle Elemente
de2en.clear()
#Neue Mappings eintragen
de2en.update({"vier":"four",4:"four",5:"five", "fünf":"five"})
print(de2en)
#Kopie erstellen
de2encopy=de2en.copy()
#Neues dict für die zahl 6 erstellen.
sechsKeys=("sechs", 6)
sechsValues=("six")
sechsDict=dict.fromkeys(sechsKeys, sechsValues)
#Dict für 6 in das große dict einfügen
de2en.update(sechsDict)
#Suche Wert für 5 raus aber lösch ihn nicht
fuenfInEnglisch=de2en.get(5)
#Suche Wert für 5 raus und lösch ihn
fuenfInEnglisch=de2en.pop(5)
#Zeig mir den Inhalt in Tupeln
inhaltInTupeln=de2en.items()
#zeig mir alle keys als liste
schluessel=de2en.keys()
#zeig mir alle werte als liste
werte=de2en.values()
#schmeiß das letzte item raus
lastitem=de2en.popitem()
#Hol mir den Wert für 6 oder setzte ihn falls er nicht drin ist
sechsInEnglisch=de2en.setdefault(6,"six")
#Hol mir den Wert für 8 oder setzte ihn falls er nicht drin ist
achtInEnglisch=de2en.setdefault(8,"eight")