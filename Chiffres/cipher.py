from utilities import translate, getChar, getNum
from GLOBAL import ALPHAMAJ as ALPHA
from icecream import ic
from typing import Iterable, Any

class Cipher:
    def __init__(self, main:str):
        self.__support = main
        self.__in_processing = 0
    
    def __str__(self):
        return self.__support

    def __repr__(self):
        return self.__support
    
    def __len__(self):
        return len(self.__support)
    
    def __next__(self):
        return next(self.__support)

    def __getitem__(self, index):
        return self.__support[index]
    
    def __add__(self, other):
        assert isinstance(other, Cipher)
        self.shift_all(other.get_support())
    
    def __sub__(self, other):
        assert isinstance(other, Cipher)
        self.shift_all(Cipher.complement(other.get_support()))
    
    def lower(self):
        self.__support = self.__support.lower()
        return self
    
    def upper(self):
        self.__support = self.__support.upper()
        return self

    def get_support(self):
        return self.__support

    def append(self, letter: str):
        assert len(letter) == 1
        self.__support += letter

    # these are the methods that are related to cryptography

    def shift(self, cipher: str|int):
        
        r = translate(self.__support[self.__in_processing], cipher)

        self.__support = (self.__support[:self.__in_processing]
                            + r
                            + self.__support[self.__in_processing+1:])

    def __next(self):
        self.__in_processing += 1

    def shift_all(self, code:str|int|Iterable[int]|Any):
        if isinstance(code, int):
            code = [code]
        
        n = len(code)
        m = len(self.__support)
        for i in range(self.__in_processing, m):
            self.shift(code[i%n])
            self.__next()

    @staticmethod
    def complement(key: str|Any):
        res = Cipher("")
        key = key.lower()
        for i in key:
            res.append(getChar(26 - getNum(i)))
        return res




