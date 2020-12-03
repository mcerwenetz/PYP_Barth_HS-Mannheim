import sys, os, string

def main():
    # Todo: Alle Dateien öffnen wo kein dat oder u8 hintendran ist
    # Alle lines aller dateien einlesen trennung bei \n%\n
    # random eins ausgeben
    # teil 2:
    # auch all das machen aber checken ob -m "wörter" in den args stehen
    # liste erstellen für alle zitate in der fetten liste die das wort enthalten
    # liste aussortieren, wenn's vorkommt in die liste für das wort
    # liste ausgeben  

    # listOfFiles = []
    # for(dirpath, dirnames, filenames) in  os.walk(r"fortunes"):
    #     listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    listOfAllFortunes=[]
    with open("beispielfortune.txt") as datei:
        lines = datei.readlines()



if __name__ == "__main__":
    main()