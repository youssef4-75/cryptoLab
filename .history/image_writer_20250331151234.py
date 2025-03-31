from utilities import getChar, getNum, translate, lastBitSetter



def writeIn(img, i, j, k, value):
    assert value in [0, 1], "Value must be either 0 or 1"
    img[i, j, k] = lastBitSetter(img[i, j, k], value)


def image_stigno(img, text):
    ``
    return None