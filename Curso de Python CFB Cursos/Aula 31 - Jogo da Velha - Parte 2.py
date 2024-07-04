import random
from colorama import Back, Fore, Style


jogarNovamente = "S"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vitoria = 'N'
velha = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    global velha
    global jogadas
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogador_Joga():
        global jogadas
        global quemJoga
        global maxJogadas
        if quemJoga == 2 and jogadas < maxJogadas:
            try:
                linha = int(input('Linha..:'))
                coluna = int(input('Coluna.:'))
                while velha[linha][coluna] != " ":
                    linha = int(input('Linha..:'))
                    coluna = int(input('Coluna.:'))
                velha[linha][coluna] = "X"
                quemJoga = 1
                jogadas += 1
            except:
                print('\nLinha e ou Coluna Inválida\n')

def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        linha = random.randrange(0,3)
        coluna = random.randrange(0,3)
        while velha[linha][coluna] != " ":
            linha = random.randrange(0, 3)
            coluna = random.randrange(0, 3)
        velha[linha][coluna]  = "O"
        jogadas += 1
        quemJoga = 2

def verificarVitoria():
    global velha
    vitoria = "N"
    simbolos = ["X","O"]
    for s in simbolos:
        vitoria = 'N'
        #Verificar Linhas.
        indice_linha = indice_coluna = 0
        while indice_linha < 3:
            soma = 0
            indice_coluna = 0
            while indice_coluna >= 0 and indice_coluna < 3:
                if velha[indice_linha][indice_coluna] == s:
                    soma += 1
                indice_coluna += 1
            indice_linha += 1
            if soma == 3:
                vitoria = s
                break
        if vitoria != "N":
            break
        #Verificar Colunas.
        indice_linha = indice_coluna = 0
        while indice_coluna < 3:
            soma = 0
            indice_linha = 0
            while indice_linha < 3:
                if velha[indice_linha][indice_coluna] == s:
                    soma += 1
                indice_linha += 1
            indice_coluna += 1
            if soma == 3:
                vitoria = s
                break
        if vitoria != "N":
            break
        #Verificar Diagonal 1.
        soma = 0
        indice_diagonal = 0
        while indice_diagonal < 3:
            if velha[indice_diagonal][indice_diagonal] == s:
                soma += 1
            indice_diagonal += 1
            if soma == 3:
                vitoria = s
                break
        #Verificar Diagonal 2.
        soma = 0
        indice_diagonal_linha = 0
        indice_diagonal_coluna = 2
        while indice_diagonal_coluna >= 0:
            if velha[indice_diagonal_linha][indice_diagonal_coluna] == s:
                soma += 1
            indice_diagonal_linha += 1
            indice_diagonal_coluna -= 1
            if soma == 3:
                vitoria = s
                break
    return(vitoria)

def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    jogarNovamente = "S"
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

while jogarNovamente == "S":
    while True:
        tela()
        jogador_Joga()
        cpuJoga()
        tela()
        vitoria = verificarVitoria()
        if vitoria != "N" or jogadas >= maxJogadas:
            break
    print(Fore.RED +  "Fim de Jogo" + Fore.YELLOW)
    if vitoria == "X" or vitoria == "O":
        print("Resultado: Jogador " + vitoria + "  Venceu!")
    else:
        print("Resultado: Empate!")
    jogarNovamente = input(Fore.BLUE + "Jogar Novamente? [S/N] " + Fore.RESET)
    redefinir()