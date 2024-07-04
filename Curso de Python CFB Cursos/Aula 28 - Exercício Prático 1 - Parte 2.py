import os
carros = list()
class Carro:
    nome = ""
    potencia = 0
    velocidade_maxima = 0
    operacao = False
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.velocidade_maxima = potencia * 2
        self.operacao = False
    def ligar(self):
        self.operacao = True
    def desligar(self):
        self.operacao = False
    def info(self):
        print(f"\nNome.........: {self.nome}")
        print(f"Potência.....: {self.potencia}")
        print(f"Veloc. Máxima: {self.velocidade_maxima}")
        print(f"Operação.....: {"Sim" if self.operacao == True else "Não"}")


def Menu():
    print("\nMenu:")
    print("\n1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir o Carro")
    print("4 - Ligar o Carro")
    print("5 - Desligar o Carro")
    print("6 - Listar os Carros")
    print("7 - Sair do Progama")
    print(f"\nQuantidade de carros: {len(carros)}")
    opcao = int(input("\nDigite uma opção: "))
    return opcao

def CriarCarro():
    n = str(input("\nNome do carro....: "))
    p = int(input("Potência do carro: "))
    car = Carro(n, p)
    carros.append(car)
    print("Novo carro criado!")

def informacoes():
    n = int(input("\nInforme o número do carro que deseja ver as informações: "))
    try:
        carros[n].info()
    except:
        print("Carro Inexistente!")
def excluirCarro():
    n = int(input("\nInforme o número do carro quue deseja excluir: "))
    try:
        del carros[n]
    except:
        print("Carro Inexistente!")
def ligarCarro():
    n = int(input("\nInforme o número do carro que deseja ligar: "))
    try:
        carros[n].ligar()
    except:
        print("Carro Inexistente!")
def desligarCarro():
    n = int(input("\nInforme o número do carro que deseja desligar: "))
    try:
        carros[n].desligar()
    except:
        print("Carro Inexistente!")
def listarCarros():
    for posicao,carro in enumerate(carros):
        print(f"{posicao} - {carro.nome} = {carro.potencia}")
ret = Menu()
while ret < 7 and ret > 0:
    if ret == 1:
        CriarCarro()
    elif ret == 2:
        informacoes()
    elif ret == 3:
        excluirCarro()
    elif ret == 4:
        ligarCarro()
    elif ret == 5:
        desligarCarro()
    elif ret == 6:
        listarCarros()
    ret = Menu()
print("\nFim do progama!")