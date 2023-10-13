from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = int(nai)
        
    @abstractmethod
    def pay(self):
        pass   
    
    @abstractmethod    
    def data_print(self):
        pass
        
    def irumnai_print(self):
        print('이름 : ' + self.irum, '나이 : ' + str(self.nai), end = ' ')
        
        