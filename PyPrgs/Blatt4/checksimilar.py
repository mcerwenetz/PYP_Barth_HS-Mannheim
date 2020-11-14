#!/usr/bin/python3
import sys
from a5 import soundex
import string

def main():
    file = open("a.txt")
    filelines = file.readlines();
    dic = {}

    for line in filelines:
        line = line.rstrip("\n")
        fileWordAsList = [char for char in line]
        sAscii = [char for char in fileWordAsList if char in string.ascii_letters]
        sAsciistr = ''
        for c in sAscii:
            sAsciistr+=c
        lineAsSoundex = soundex(line)
        
        if not lineAsSoundex in dic:
            dic[lineAsSoundex] = [line]
        else:
            dic[lineAsSoundex] = dic[lineAsSoundex] + [line]

    values = list(dic.values())
    print(max([len(liste) for liste in values]))
    
    file.close()


if __name__ == "__main__":
    main()