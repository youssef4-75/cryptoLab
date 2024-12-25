from ..utilities import translate

class Cstr:
    def __init__(self, corps):
        self.corps = corps
    
    def append(self, letter):
        self.corps += letter

    def modify(self, char: str, index: int):
        self.corps = self.corps[:index] + char + self.corps[index + 1:]
    
    def shift(self, char: str, index: int = 0):
        self.modify(translate(char, self.corps[index]))


    def __add__(self, other:str):
        new_corps = ""
        for i in self.corps:
            new_corps += i
        




    
    

