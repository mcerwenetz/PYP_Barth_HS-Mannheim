import sys
from PIL import Image
import os

def gamma(cols,rows,img, zahl):
    if not 0.0 <= zahl <= 10:
        raise ValueError("wrong value for gamma. 0 <= gamma <= 10")
    for y in range(rows):
        for x in range(cols):
            v = img.getpixel((x, y))
            newvalue = int(255*pow((v/255),zahl))
            tupelKoordinate=(x,y)
            img.putpixel(tupelKoordinate, newvalue)
    return img

def heller(cols, rows, img, zahl):
    if not -100 <= zahl <= 100:
        raise ValueError("wrong brightness value -100 <= brightness <= 100")
    for y in range(rows):
        for x in range(cols):
            v = img.getpixel((x, y))
            newvalue = int((v + (255.0*zahl)))
            tupelKoordinate=(x,y)
            img.putpixel(tupelKoordinate, newvalue)
    return img

def spreizen(cols,rows,img,zahl):
    if not 0 <= zahl <= 100:
        raise ValueError("wrong p value 0 <= p <= 100")
    min=255
    max=0
    for y in range(rows):
        for x in range(cols):
            v = img.getpixel((x, y))
            if v > max:
                max=v
            if v < min:
                min=v
    if zahl == 100:
        for y in range(rows):
            for x in range(cols):
                v = img.getpixel((x, y))
                newvalue = int(255*((v-min)/(max-min)))
                img.putpixel((x,y), newvalue)
    else:
        min=min*(1-(zahl/100))
        max=max+((255-max)*(zahl/100))
        for y in range(rows):
            for x in range(cols):
                v = img.getpixel((x, y))
                newvalue = int(255*((v-min)/(max-min)))
                img.putpixel((x,y), newvalue)

    return img

def binarisieren(cols, rows, img, zahl):
    if not 0 <= zahl <= 255:
        raise ValueError("wrong threshold value 0 <= p <= 255")        
    for y in range(rows):
        for x in range(cols):
            v = img.getpixel((x, y))
            if v >= zahl:
                img.putpixel((x, y), 255)
            else:
                img.putpixel((x, y), 0)
    return img


def main(argv):
    if len(argv) != 4:
        print("wrong number of arguments")
        return
    elif (argv[0] not in ["heller", "spreizen", "gamma", "binarisieren"]):
        print("function " + argv[0]+" not found")
        return
    manipulation=argv[0]
    zahl = float(argv[1])
    pfad = argv[2]
    workingdirectory = os.getcwd()
    pfad = os.path.join(workingdirectory, pfad)
    ausgabedatei=argv[3]

    img =Image.open(pfad)
    img.show()
    cols, rows = img.size

    try:
        if manipulation == "heller":
            img = heller(cols,rows,img,zahl)
        elif manipulation == "gamma":
            img = gamma(cols,rows,img,zahl)
        elif manipulation == "spreizen":
            img = spreizen(cols,rows,img,zahl)
        elif manipulation == "binarisieren":
            img = binarisieren(cols,rows,img,zahl)    
    except Exception as e:
        print(e)
        return

    img.save(ausgabedatei)
    img.show()

if __name__ == "__main__":
    main(sys.argv[1:])