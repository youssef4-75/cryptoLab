

class Cipher:
    def __init__(self, key):
        self.__cipher = key
        self.__n = len(key)

    def __iter__(self):
        self.k = -1
        return self 

    def __next__(self):
        self.k = (self.k+1)%self.__n
        return self.__cipher[self.k]
    
    