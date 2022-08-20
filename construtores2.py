from msilib.schema import _Validation_records


class ControleRemoto:
    def __init__(self, valor_cor, valor_altura, valor_profundidade, valor_largura):
        self.cor = valor_cor
        self.altura = valor_altura
        self.profundidade = valor_profundidade
        self.largura = valor_largura
    def ligar(self, botao):
        if botao == 'ligar':
            print('dispositivo ligado')
        elif botao == 'desligar':
            print('dispositivo desligado')
    def trocar_volume(self, botao):
        if botao == '+':
            print('volume aumentado')
        elif botao == '-':
            print('volume abaixado')
    def propriedades(self):
        print('A cor do controle é')
        print('As dimensoes sao ', self.altura, self.largura, self.profundidade)
    


controle1 = ControleRemoto('Preto', '10cm', '2cm', '4cm')
print(controle1.cor, controle1.altura, controle1.largura, controle1.profundidade)
#Esse metodo printa as propriedades ele só necessida do objeto
#para dar o retorno
#def propriedades(self)
controle1.propriedades()

#Esses metodos precisam do objeto mais o parametro de botao
#que esta dentro do ()
controle1.trocar_volume('-')
controle1.ligar('desligar')

#É importante lembrar que:
#   --> controle1.trocar_volume('-') retorna o print 
#   --> controle1.trocar_volume não retorna nada, pois ele é um metodo
#       e caso coloque esse método dentro de um print o retorno sera que
#       controle1.trocar_volume é um método
#       Exemplo:
print(controle1.trocar_volume)