from GLOBAL import ALPHAMAJ, ALPHAMIN

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


def translate(letter:str, cipher:str):
    return getChar(getNum(letter) + getNum(cipher))
