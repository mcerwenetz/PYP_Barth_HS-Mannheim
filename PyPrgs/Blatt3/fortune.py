import sys, os, string, random, io

def main(arguments):
    # Todo: Alle Dateien öffnen wo kein dat oder u8 hintendran ist
    # wenn mehrere wörter gefunden werden sollen list of args entgegennehmen
    # Alle lines aller dateien einlesen trennung bei \n%\n

    listOfFiles = []
    listOfAllowedFiles=[]
    listOfAllFortunes=[]
    for(dirpath, _, filenames) in  os.walk("fortunes"):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    relevantFiles=filter(lambda x: not x.endswith(".dat"), listOfFiles)
    for relevantFile in relevantFiles:
        listOfAllowedFiles.append(relevantFile)

    for allowedFile in listOfAllowedFiles:
        with open(allowedFile,"r", encoding="utf-8") as datei:
            lines = datei.read()
        listOfAllFortunes += lines.split("\n%\n")
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