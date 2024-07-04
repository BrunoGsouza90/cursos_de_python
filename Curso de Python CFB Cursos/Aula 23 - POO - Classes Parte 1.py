class Carro:
    velMax = 0
    ligado = False
    cor = ""

c1 = Carro()

c1.velMax = 200
c1.ligado = False
c1.cor = 'Preto'''

print("Velocidade Máxima = " + str(c1.velMax) + ".")
print("Cor = " + str(c1.cor) + ".")
print("O carro está " + ("Desligado." if c1.ligado == False else "Ligado."))

print('')