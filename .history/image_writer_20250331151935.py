from utilities import getChar, getNum, translate, lastBitSetter, toBinary
from itertools import product



def writeIn(img, i, j, k, value):
    assert value in [0, 1], "Value must be either 0 or 1"
    img[i, j, k] = lastBitSetter(img[i, j, k], value)


    
    
    


def image_stigno(img, text):
    """
    This function adds steganography to an image using the Least Significant Bit (LSB) method.
    """
    height, width, channels = img.shape
    cci = 0
    ccj = 0
    
    for i, j, k in product(range(height), range(width), range(channels)):
        # Your steganography logic here
        # For example:
        if cci >= len(text):
            break
        char = text[cci]
        bit = toBinary(getNum(char))
        writeIn(img, i, j, k, bit)
        ccj += 1
        if ccj == 5:  # Assuming 5 bits per character
            cci += 1
            ccj = 0

    return img