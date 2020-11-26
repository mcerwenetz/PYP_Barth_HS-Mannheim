DEUTSCH = "deutsch"
ENGLISCH = "englisch"

_sprache = DEUTSCH

def removeBackslashesNewLine(lines):
    newlines = []
    for line in lines:
            line = line.strip("\n")
            newlines.append(line)
    return newlines

def chars(filename):
    count=0
    with open(filename) as file:
        lines = file.readlines()
        lines = removeBackslashesNewLine(lines)
        for line in lines:
            for char in line:
                count+=1
    return count


def words(filename):
    pass

def lines(filename):
    pass

def wc(filename):
    pass

def wc_show(filename):
    pass

def set_lang(sprache):
    if sprache not in(DEUTSCH, ENGLISCH):
        raise Exception("Sprache nicht unterstützt")
    else:
        _sprache = sprache

if __name__ == "__main__":
    print(chars("a.txt"))