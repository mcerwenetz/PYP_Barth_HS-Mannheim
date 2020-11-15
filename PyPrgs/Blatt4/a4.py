from string import ascii_lowercase
translationTable = {}

for i in range(0,26):
    if i < 13:
        translationTable[ascii_lowercase[i]] = ascii_lowercase[i+13]
    else:
        translationTable[ascii_lowercase[i]] = ascii_lowercase[(i+13)%len(ascii_lowercase)]


def rot13(decoded: str) -> str:
    coded = ""

    for letter in decoded:
        coded += translationTable[letter]

    return coded


print(rot13(rot13("hallo")))

