import sys, os, string, random

def main(arguments):
    # Todo: Alle Dateien öffnen wo kein dat oder u8 hintendran ist
    # wenn mehrere wörter gefunden werden sollen list of args entgegennehmen
    # Alle lines aller dateien einlesen trennung bei \n%\n

    # listOfFiles = []
    # for(dirpath, dirnames, filenames) in  os.walk(r"fortunes"):
    #     listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    with open("beispielfortune.txt") as datei:
        lines = datei.read()
    listOfAllFortunes = lines.split("\n%\n")
    if len(arguments) != 0 and arguments[0] == "-m":
        listOfAllowedFortunes=[]
        search = arguments[1]
        for fortune in listOfAllFortunes:
            if fortune.find(search) != -1:
                listOfAllowedFortunes.append(fortune)
    else:
        listOfAllowedFortunes = listOfAllFortunes
    randomzitat = random.choice(listOfAllowedFortunes)
    print(randomzitat)



if __name__ == "__main__":
    main(sys.argv[1:])