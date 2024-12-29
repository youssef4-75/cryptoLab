from Chiffres import Cipher
from icecream import ic

if __name__ == "__main__":
    # print(translate("i", "o"))

    key = "simple"
    comp = Cipher.complement(key)

    comp.shift_all(key)
    ic(comp)


    