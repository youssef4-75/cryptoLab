from typing import Iterable
from random import randint

from Chiffres import Cipher

def chiffrerMultilayer(text:str, 
        ciphers: Iterable[str|int|Iterable[int]|Cipher],
        partition: Iterable[Iterable[int]]=None):
    """
    this is a personal cipher algorithm,
    it encrypt the message many times,
    so that it be too hard to decode it
    it may be encoded by different ciphers or the same one
    """
    n = len(text)
    if partition is None:
        partition = randint(0, 10)
    if isinstance(partition, int): 
        partition = [((start := randint(0, n)), 
                    randint(start, n)) 
            for _ in range(partition)]
    res: Cipher = Cipher(text)
    for cipher, (start, end, *_) in zip(ciphers, partition):
        res.shift_all(cipher, start, end)
    return res.get_support()


def deChiffrerMultilayer(text:str, 
        ciphers: Iterable[str|int|Iterable[int]|Cipher],
        partition: Iterable[Iterable[int]]):
    """
    
    """

    assert len(partition) == len(ciphers)

    anti_ciphers = [
        Cipher.complement(k).get_support()
            for k in ciphers
    ]
    anti_partition = [part for part in partition]
    anti_ciphers.reverse()
    anti_partition.reverse()

    return chiffrerMultilayer(text, anti_ciphers, anti_partition)

    






if __name__ == "__main__":
    # print(translate("i", "o"))

    key = "vigenere"
    plainText = "here land the mystery"
    res = chiffrerMultilayer(plainText, [key, "vip"], [[0, 300], [3, 122]])
    print(res)
    h = deChiffrerMultilayer(res, [key, "vip"], [[0, 300], [3, 122]])
    print(h)



