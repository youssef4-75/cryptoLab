from utilities import getChar, getNum, translate
from Chiffres import Cipher
from test import CHALLENGE


def chiffrerVigener(text, key):
    Ctext = Cipher(text)
    Ctext.shift_all(key)
    return Ctext.get_support()

def dechiffrerVigenere(text, key):
    key = Cipher.complement(key)
    return chiffrerVigener(text, key)



if __name__ == "__main__":
    # print(translate("i", "o"))

    key = "vigenere"
    plainText = "here land the mystery"
    res = chiffrerVigener(plainText, key)
    print(res)
    print(dechiffrerVigenere(res, key))

    k = Cipher("here land the mystery")
    k.shift_all(2, 2)
    print(k)
    k.shift_all(24, 4)
    print(k)
