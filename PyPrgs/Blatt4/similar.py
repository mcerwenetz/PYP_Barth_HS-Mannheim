from a5 import soundex

def main(word : str, filename : str) -> None:
    ergebnisliste = []

    sWord = soundex(word)

    file = open(filename)
    for x in file:
        sFile = soundex(x)
        if sWord == sFile:
            ergebnisliste.append(sFile)
    
    file.close()

    print(ergebnisliste)


if __name__ == "__main__":
    main("hallo", "a.txt")