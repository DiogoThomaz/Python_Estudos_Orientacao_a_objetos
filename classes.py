##Códigos criados para estudar conceitos de pyhon


##Função
#Funcao que solicita dois valores e retorna o resultado de uma soma
#As variáveis valor, incremento e resultado são de escopo local
#Dica: É uma boa prática escrever as funções com letras minusculas e separar elas com _

print('----------------------------------------')
print('Aula de funcao')
def teste_valor(v,i):
    valor = v
    incremento = i
    resultado = valor + incremento
    return resultado

print(teste_valor(1,1))
print('----------------------------------------')

##Classes e métodos
#Dica: É uma boa prática escrever o nome da classe com a primeira letra
#em maiúsculo e separar as palavras por letras em maiúsculo

#Método é o nome dado a função dentro da classe
#Toda função dentro da classe tem que ter o parâmetro self

#instanciar é dizer que a variável é igual a classe
#apartir da instância a variável pode usar os métodos da classe

print('Aula de Classes e metodos')

class DidaticaTech:
    #método incrementa requer dois atributos --> v, i
    #atributo é uma variável dentro dentro da função
    def incrementa(self, v, i):
        valor = v
        incremento = i
        resultado = valor + incremento
        return resultado

#Instancia a classe na variável a
a = DidaticaTech()
#Chama o método incrementa da classe DidaticaTech e atribui a variavel b
b = a.incrementa(4,5)

#Esse print diz que a é um objeto
print(a) 
#Esse print diz o valor de b, que recebeu o retorno do metodo incrementa
print(b)

#Instancia a classe na variavel e utiliza o metodo com apenas uma linha de codigo
a = DidaticaTech().incrementa(9,9)
print(a)



class DidaticaTech2:
    #self. --> utilizado para fazer referencia ao objeto instanciado
    def incrementa2(self, v, i):
        self.valor = v
        self.incremento = i
        self.resultado = self.valor + self.incremento
        return self.resultado


a = DidaticaTech2()
b = DidaticaTech2().incrementa2(15, 15)
print(b)

print('----------------------------------------')

##Construtores
#É um método que define os atributos da classe de inicio
#para usar um construtor def __init__(self, ...):

#O construtor permite que todos os atributos sejam acessados 
#pelos métodos, desde de que sejam declarados no instanciamento



print('Aula de construtores')

class DidaticaTech3:
    def __init__(self, v: int, i: int):
        self.valor = v
        self.incremento = i
    def Incrementa3(self):
         self.valor = self.incremento + self.valor
         print(self.valor)
    def dobro(self):
        self.Incrementa3()
        

operador = DidaticaTech3(3, 2)
print(operador.valor, ' +', operador.incremento)

x = operador.Incrementa3()




