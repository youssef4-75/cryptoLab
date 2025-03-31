from utilities import getChar, getNum, translate, lastBitSetter



def writeIn(img, i, j, k, value):
    assert value in [0, 1], "Value must be either 0 or 1"
    img[i, j, k] = lastBitSetter(img[i, j, k], value)


def image_stigno(img, text):
    """
    This function adds steganography to an image using the Least Significant Bit (LSB) method.
    """
    n, m, l = img.shape
    cci = 0
    ccj = 0
    
    


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
        if cci < len(text):
            char = text[cci]
            bit = int(char[ccj])
            writeIn(img, i, j, k, bit)
            ccj += 1
            if ccj == 8:  # Assuming 8 bits per character
                cci += 1
                ccj = 0
        else:
            break  # Exit the loop if we've processed all the text

    return img