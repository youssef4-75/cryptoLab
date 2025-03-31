from utilities import getChar, getNum, lastBitSetter, toBinary
from itertools import product
from PIL import Image
import numpy as np

"""
since there are only 26 letters in English, i will need 5 bits, but that gives me 32 char
so there will be special characters:
    - newline character: "11110"
    - space character: "11111"
    - tab character: "11011"
    - unknown character: "11100"
    - end of text: "11101"
"""

pileCheck = ""


SPECIAL_CODE = {
    "\n": "11110",
    " ": "11111",
    "\t": "11011",
    "": "11100",
    "\x00": "11101"
}



def writeIn(img, i, j, k, value):
    assert value in [0, 1], "Value must be either 0 or 1"
    img[i, j, k] = lastBitSetter(img[i, j, k], value)


    
def textToNumStream(text: str) -> str:
    global pileCheck 
    res = ""
    for char in text:
        r = SPECIAL_CODE.get(char, toBinary(getNum(char)))
        res += r
        pileCheck += r
        pileCheck += "|"
    pileCheck += SPECIAL_CODE["\x00"]
    return res + SPECIAL_CODE["\x00"]

def numSteamToText(stream: str) -> str:
    res = ""

    for f in range(0, len(stream), 5):
        chunk = stream[f:f+5]
        # depiler la pile et si le bit depiler est differnt du bit du stream, raise une erreur 

        match chunk:
            case SPECIAL_CODE["\n"]: res += "\n"
            case SPECIAL_CODE[" "]: res += " "
            case SPECIAL_CODE["\t"]"11011": res += "\t"
            case _: res += getChar(int(chunk, 2))
    
    return res

    

def image_stigno(img_Image, text):
    """
    This function adds steganography to an image using the Least Significant Bit (LSB) method.
    """
    img = np.array(img_Image)
    height, width, channels = img.shape
    stream = textToNumStream(text)
    print(f"input stream: {stream}")
    sti = 0

    for i, j, k in product(range(height), range(width), range(channels)):
        if sti >= len(stream):
            break
        writeIn(img, i, j, k, int(stream[sti]))
        sti += 1
        if sti%5 == 4 and stream[sti-4:sti+1] == SPECIAL_CODE["\x00"]:
            break

    return Image.fromarray(img)

def image_reveal(img_Image):
    """
    This function reveals the hidden text from an image using the LSB method.
    """
    img = np.array(img_Image)
    height, width, channels = img.shape
    stream = ""
    c = 0
    for i, j, k in product(range(height), range(width), range(channels)):
        c = (c+1) % 5        
        if c == 0 and stream[-5:] == "11101":
            break
        stream += str(1 - (img[i, j, k] % 2))
    print(f"output stream: {stream}")
    return numSteamToText(stream)

if __name__ == "__main__":
    # Create an image
    
    img = Image.new("RGB", (100, 100), "white")
    text = "Hello steganographr"
    img = image_stigno(img, text)
    print(f"pile: {pileCheck}, {len(pileCheck)}")
    
    img.save("output.png")
    
    
    img = Image.open("output.png")
    hidden_text = image_reveal(img)
    print(f"Revealed text: {hidden_text}")