class Carro:
    velMax = 0
    ligado = False
    cor = ""
    def __init__(self,v,l,c):
        self.velMax = v
        self.ligado = l
        self.cor = c
    def mostrar(self):
        print("Velocidade Máxima = " + str(self.velMax) + ".")
        print("Ligado ou Desliga = " + ("Desligado." if self.ligado == False else "Ligado."))
        print("Cor.............. = " + str(self.cor) + ".")
        print("...................................")
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def andar(self):
        if (self.ligado):
            print('Andando!')
        else:
            print('Carro desligado!')

c1 = Carro(200,False,"Preto")
c2 = Carro(120,False,"Branco")
c3 = Carro(350,False,"Vermelho")

c2.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()
c3.andar()