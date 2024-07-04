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
        print(f"Nome.........: {self.nome}")
        print(f"Potência.....: {self.potencia}")
        print(f"Veloc. Máxima: {self.velocidade_maxima}")
        print(f"Operação.....: {"Sim" if self.operacao == True else "Não"}")


def Menu():
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informações do Carro")
    print("3 - Excluir o Carro")
    print("4 - Ligar o Carro")
    print("5 - Desligar o Carro")
    print("6 - Listar os Carros")
    print("7 - Sair do Progama")
    print(f"Quantidade de carros {len(carros)}")
    opc = input("Digite uma opção: ")
    return opc

def CriarCarro():
    os.system('cls') or None
    n = input("Nome do carro....: ")
    p = input("Potencia do carro: ")
    car = Carro(n, p)
    carros.append(car)
    print("Novo carro criado!")
    os.system("pause")

def informacoes():
    os.system("cls") or None
    n = input("Informe o número do carro quue deseja ver as informações: ")
    try:
        carros[int(n)].info()
    except:
        print("Carro Inexistente!")

def excluirCarro():
    os.system("cls") or None
    n = input("Informe o número do carro quue deseja excluir: ")
    try:
        del carros[int(n)]
    except:
        print("Carro Inexistente!")
    os.system("pause")

def ligarCarro():
    os.system("cls") or None
    n = input("Informe o número do carro que deseja ligar: ")
    try:
        carros[int(n)].ligar()
    except:
        print("Carro Inexistente!")

def desligarCarro():
    os.system("cls") or None
    n = input("Informe o número do carro que deseja desligar: ")
    try:
        carros[int(n)].desligar()
    except:
        print("Carro Inexistente!")

def listarCarros():
    os.system("cls") or None
    for posicao,carro in enumerate(carros):
        print(f"p{posicao} - {carro.nome} = {carro.potencia}")
    os.system("pause")