from a5 import soundex
import string

def main(word : str, filename : str) -> None:
    ergebnisliste = []

    sWord = soundex(word)

    file = open(filename)
    for x in file:
        x = x.rstrip("\n")
        fileWordAsList = [char for char in x]
        sAscii = [char for char in fileWordAsList if char in string.ascii_letters]
        sAsciistr = ''
        for c in sAscii:
            sAsciistr+=c
        sFile = soundex(sAsciistr)
        if sWord == sFile:
            ergebnisliste.append(x)
    
    file.close()

    print(ergebnisliste)


if __name__ == "__main__":
    main("Hallo", "wordsonlyascii.txt")