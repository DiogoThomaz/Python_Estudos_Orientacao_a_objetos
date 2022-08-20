
from __future__ import print_function
from ast import arg


class DidaticaTech3():
    
    def __init__(self, v = 10, i = 1):
        self.valor = v
        self.incremento = i

    def Incrementa3(self):
         self.valor = self.incremento + self.valor
         self.exibir
        
    def dobro(self):
        self.Incrementa3()
    
    def exibir(self):
        print_function(self.Incrementa3)

conta = DidaticaTech3(3,2)
print(conta.valor)




