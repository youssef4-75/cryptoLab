from utilities import getChar, getNum, translate, lastBitSetter



def writeIn(img, i, j, k, value):
    img[i, j, k] = lastBitSetter(img[i, j, k], value)


def image_stigno(filename, text): 
    return None