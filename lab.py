from vigenere import chiffrerVigener as chv, dechiffrerVigenere as dcv
from caesar import chiffrerCaesar as chc
from multi_layer import chiffrerMultilayer as chm, deChiffrerMultilayer as dcm


# remember that if you wrote your 
# text in the second line the first 
# caracter is the \n that you used to 
# go to the second line

"""
-\+ 1: to use the vigenere method, 
-\+ 2: to use the caesar method, 
-\+ 3: to use the multilayer method

negative sign to decrypt it

see the function documentation to know how it work
"""


text = """
"""

crypto_mode = 0

param = [
]

kwds = {

}


match crypto_mode:
    case 1:
        print(chv(text, *param, **kwds))
    case -1:
        print(dcv(text, *param, **kwds))
    case 2:
        print(chc(text, *param, **kwds))
    case -2:
        print(chc(text, 26-param[0], **kwds))
    case 3:
        print(chm(text, *param, **kwds))
    case -3:
        print(dcm(text, *param, **kwds))