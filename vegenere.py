from utilities import getChar, getNum
from Chiffres import cstr
from test import CHALLENGE

def Vegenere(txt: str, cipher: str, quotient: int=1):
    res = cstr("")
    k = 0
    n = len(cipher)
    for c in txt:
        if not c.isalpha(): res += c
        else: 
            shift = getNum(cipher[k])
            res += getChar(getNum(c) + quotient*shift)
        k = (k+1)%n
    return res

def chiffrerVegenere(txt: str, cipher: str):
    return Vegenere(txt, cipher)

def dechiffrerVegenere(txt: str, cipher: str):
    return Vegenere(txt, cipher, -1)





# print(

# getChar(getNum('m') + getNum('v'))

# )

# exit()

if __name__ == "__main__":
    # print(CHALLENGE[0])

    print(
        getChar(getNum("m") + getNum("v"))
    )

    print(dechiffrerVegenere(CHALLENGE[0], "v"))

