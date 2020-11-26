DEUTSCH = "deutsch"
ENGLISCH = "englisch"

_sprache = DEUTSCH


def chars(filename):
    pass

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