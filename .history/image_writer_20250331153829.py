from utilities import getChar, getNum, translate, lastBitSetter, toBinary
from itertools import product

"""
since there are only 26 letters in English, i will need 5 bits, but that gives me 32 char
so there will be special characters:
    - newline character: "11110"
    - space character: "11111"
    - tab character: "11011"
    - unknown character: "11100"
    - end of text: "11101"
"""




def writeIn(img, i, j, k, value):
    assert value in [0, 1], "Value must be either 0 or 1"
    img[i, j, k] = lastBitSetter(img[i, j, k], value)


    
def textToNumStream(text: str) -> str:
    res = ""
    for char in text:
        match char:
            case "\n":
                res += "11110"
            case " ":
                res += "11111"
            case "\t":
                res += "11011"
            case _:
                res += toBinary(getNum(char))
    return res + "11101"

def numSteamToText(stream: str) -> str:
    res = ""

    for f in range(0, len(stream), 5):
        chunk = stream[f:f+5]
        match chunk:
            case "11110": res += "\n"
            case "11111": res += " "
            case "11011": res += "\t"
            case _: res += getChar(int(chunk, 2))
    
    return res

    


def image_stigno(img, text):
    """
    This function adds steganography to an image using the Least Significant Bit (LSB) method.
    """
    height, width, channels = img.shape
    stream = textToNumStream(text)
    sti = 0

    for i, j, k in product(range(height), range(width), range(channels)):
        if sti >= len(stream):
            break
        writeIn(img, i, j, k, int(stream[sti]))
        sti += 1

    return img

def g