#!/usr/bin/python3
import sys

# Hier weitere Funktionen


def main(args): # args sind die Kommandozeilen-Argumente
   
    dicti = { 12345: (17,19), 123: (10,)}
    dictineu = {}
    # pro schlüssel in dicti
    for key in dicti:
        # wandle den key in string, kürz ihn auf 3, assigne keynew
        # keyneu heißt neuer gekürzter schlüssel
        keyneu = str(key)[:3]
        # wenn der neue gekürzte key noch nicht in im neuen dictionary ist
        if keyneu not in dictineu.keys():
            # dann schreibe an den wert von keyneu die value von dicti, also vom alten
            dictineu[keyneu] = dicti[key]
        # falls der key schon im neuen dict ist
        else:
            # und der wert an der stelle vom key der schon drin ist ein tupel ist
            if type(dictineu[keyneu]) is tuple:
                # estelle ein tupel aus dem wert der neuen value und der alten value die hinzugefügt werden soll
                # sortiere das tupel
                # mache ein Tupel aus der Liste die sorted zurückgegeben hat
                # und assigne dieses neue sortierte Tupel aus altem und neuen Wert der value an der Stelle des neuen keys
                # der zwar schon ein Value hatte, aber dieses value wurde einfach ergänzt
                dictineu[keyneu] = tuple(sorted((*dictineu[keyneu], *dicti[key])))
                # falls der neue eintrag kein tupel ist erstelle ein Tupel aus neuem und altem wert, sortiere es, 
                # mach aus der liste ein tupel und füge es hinzu
            else:   
                dictineu[keyneu] = tuple(sorted((dictineu[keyneu], dicti[key])))
    print(dictineu)

    # def dictshortstringskeys(dic):
    # dictineu = {}
    # for key in dic:
    #     keyneu = str(key)[:3]
    #     if keyneu not in dictineu.keys():
    #         dictineu[keyneu] = dic[key]
    #     else:
    #         if type(dictineu[keyneu]) is tuple:
    #             dictineu[keyneu] = tuple(sorted((*dictineu[keyneu], dic[key])))
    #         else:   
    #             dictineu[keyneu] = tuple(sorted((dictineu[keyneu], dic[key])))
    # return(dictineu)
    # pass

if __name__ == '__main__':
    main(sys.argv[1:])