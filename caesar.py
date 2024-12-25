from utilities import getChar, getNum


def chiffrerCaesar(txt: str, code:int):
    res = ""
    for c in txt:
        if not c.isalpha(): res += c
        else: res += getChar(getNum(c)+ code)
    return res

if __name__ == "__main__":
    print(chiffrerCaesar("hello world!", 1))


