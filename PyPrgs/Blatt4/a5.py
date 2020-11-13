dictionary = {x:1 for x in "bfpv"}
dictionary.update({x:2 for x in "cgjkqsxz"})
dictionary.update({x:3 for x in "dt"})
dictionary.update({x:4 for x in "l"})
dictionary.update({x:5 for x in "mn"})
dictionary.update({x:6 for x in "r"})
dictionary.update({x:"" for x in "aeiouwyh"})


def soundex(zeichenkette : str) -> str:
    output = zeichenkette[0]
    for letter in zeichenkette[1:]:
        if dictionary[letter] != output[-1]:
            output = output + str(dictionary[letter])
        if len(output) >= 6:
            break
    while len(output) <6:
        output += str(0)
    return output


def main(inputs):
    ergebnisse = []

    for word in inputs:
        lowerword = word.lower()
        ergebnisse.append(soundex(lowerword))

    print(ergebnisse)

if __name__ == "__main__":
    main(["soundex", "soundeggs", "flurbel"])