import random
erros = 1
sorteado = random.randrange(0,100)
jogador = int(input("Digite seu número: "))
while sorteado != jogador:
    if sorteado > jogador:
        print("Erro, número é maior.")
    elif sorteado < jogador:
        print("Erro, número é menor.")
    erros += 1
    jogador = int(input("Digite seu número: "))
print("Número " + str(jogador) + ", você acertou em " + str(erros) + " tentativas.")