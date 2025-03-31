from GLOBAL import ALPHAMAJ, ALPHAMIN
from icecream import ic
from typing import Literal

def getNum(char: str):
    """
    get the number of a letter in the ALPHA constant
    """
    
    global ALPHAMAJ, ALPHAMIN

    assert len(char) <= 1
    if len(char) == 0: return -1
    if char.islower():
        ALPHA = ALPHAMIN
    else: ALPHA = ALPHAMAJ
    for i, c in enumerate(ALPHA):
        if char == c: return i
    return -1


def getChar(i: int, maj: bool=False):
    """
    get the letter of a letter in the ALPHA constant
    """

    global ALPHAMAJ, ALPHAMIN
    mod = len(ALPHAMAJ)
    if i == -1: return " "
    if maj: return ALPHAMAJ[i%mod]
    return ALPHAMIN[i%mod]


def translate(letter:str, cipher:str|int):
    if not letter.isalpha(): 
        return letter
    elif isinstance(cipher, int):
        i = cipher
    else:
        i = getNum(cipher)
    return getChar(getNum(letter) + i)


def toBinary(n: int) -> str:
    if n == -1: return "11111"
    return bin(n)[2:]

def fromBinary(b: str) -> int:
    if b == "11111": return -1
    return int(b, 2)

def lastBitSetter(n: int, bit: Literal[1, 0]) -> int:
    res = n ^ bit  
    # fill the first bits with 0 to get 5 bits in total.
    re



print(toBinary(2))