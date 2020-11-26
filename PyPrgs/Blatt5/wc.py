DEUTSCH = "deutsch"
ENGLISCH = "englisch"

_sprache = DEUTSCH


def chars(filename):
    count=0
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip("\n")
            for c in line:
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