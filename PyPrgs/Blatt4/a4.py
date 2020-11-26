from string import ascii_lowercase
translationTable = {}
ascii_lowercaseAsList = [char for char in ascii_lowercase]

# for i in range(0,26):
#     if i < 13:
#         translationTable[ascii_lowercase[i]] = ascii_lowercase[i+13]
#     else:
#         # janz wichtig! modulo damit er wieder von vorne anfängt
#         translationTable[ascii_lowercase[i]] = ascii_lowercase[(i+13)%len(ascii_lowercase)]
translationTable.update({ascii_lowercaseAsListChar:chr(ord(ascii_lowercaseAsListChar)+13) if ord(ascii_lowercaseAsListChar)+13 <= ord('z') else chr((ord(ascii_lowercaseAsListChar)+13)-26) for ascii_lowercaseAsListChar in ascii_lowercaseAsList  })


def rot13(decoded: str) -> str:
    coded = ""

    for letter in decoded:
        coded += translationTable[letter]

    return coded


print(rot13(rot13("hallo")))

