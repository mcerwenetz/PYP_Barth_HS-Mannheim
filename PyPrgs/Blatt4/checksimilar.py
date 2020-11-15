#!/usr/bin/python3
import sys
from a5 import soundex
import string

def main():
    file = open("wordsonlyascii.txt")
    filelines = file.readlines()
    dic = {}

    for line in filelines:
        line = line.rstrip("\n")
        fileWordAsList = [char for char in line]
        sAscii = [char for char in fileWordAsList if char in string.ascii_letters]
        sAsciistr = ''
        for c in sAscii:
            sAsciistr+=c
        lineAsSoundex = soundex(sAsciistr)
        
        if not lineAsSoundex in dic:
            dic[lineAsSoundex] = [line]
        else:
            dic[lineAsSoundex] = dic[lineAsSoundex] + [line]

    values = list(dic.values())
    biggestGroup = max([len(liste) for liste in values])
    allWords = len(filelines)
    allNotInBiggestGroup = allWords - biggestGroup
    print("größte gruppe hat %3d wörter " % biggestGroup)
    print("Alle wörter %d" % len(filelines))
    print("Alle Wörter die nicht zur größten gruppe gehören %d" % allNotInBiggestGroup)


    
    file.close()


if __name__ == "__main__":
    main()