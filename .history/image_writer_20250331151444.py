from utilities import getChar, getNum, translate, lastBitSetter



def writeIn(img, i, j, k, value):
    assert value in [0, 1], "Value must be either 0 or 1"
    img[i, j, k] = lastBitSetter(img[i, j, k], value)


def image_stigno(img, text):
    """
    This function adds steganography to an image using the Least Significant Bit (LSB) method.
    """
    i, j, k = img.shape
    cci = 0
    ccj = 0
    for i, j, k in []: