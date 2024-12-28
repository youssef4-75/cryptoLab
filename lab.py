from vigenere import chiffrerVigener as chv, dechiffrerVigenere as dcv
from caesar import chiffrerCaesar as chc
from multi_layer import chiffrerMultilayer as chm, deChiffrerMultilayer as dcm

text = """c un text test, drto bach njareb cryptoLab, next key howa crypto, ila drti next key o dechiffriti had l hadra ta hiya mzn, wsalti l lvl2, next key hiya 23, kyn github diali fih cryptoLab howa li knkhdem bih bach nchiffri o ndechiffri dkchi li knkteb, next howa llm, ghatban lik hadi m3a9da cwiya mais hadi ghir tjriba
"""

crypto_mode = 3

param = [
    ["aseds", "crypto", 23],
    [[0, 800], [70, 2400], [20, 2301]]
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