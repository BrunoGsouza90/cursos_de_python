def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha():
            print(f'\033[31mErro: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
