import sys
from PIL import Image

def gamma():
    pass

def heller():
    pass
def spreizen():
    pass
def binarisieren(cols, rows, img, zahl):
    for y in range(rows-1):
        for x in range(cols-1):
            v = img.getpixel((x, y))
            if v >= zahl:
                img.putpixel((x, y), 255)
            else:
                img.putpixel((x, y), 0)
    return img


def main(argv):
    manipulation=argv[0]
    zahl = float(argv[1])
    pfad = argv[2]
    ausgabedatei=argv[3]

    img =Image.open(r'D:\Nextcloud\Studium\6TIB\PYP\Repo\20pyth06\PyPrgs\Blatt2\bilder\a.pgm')
    cols, rows = img.size
    img.show()
    img = binarisieren(cols,rows,img,zahl)
    img.show()
    img.save(ausgabedatei)


if __name__ == "__main__":
    main(sys.argv[1:])