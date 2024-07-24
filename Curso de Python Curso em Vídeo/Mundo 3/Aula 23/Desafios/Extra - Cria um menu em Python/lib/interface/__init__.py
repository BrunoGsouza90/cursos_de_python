def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return numero

def linha(tamanho = 42):
    return '-' * tamanho

def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for contador, item in enumerate(lista):
        print(f'\033[33m{contador + 1}\033[m - \033[34m{item}\033[m')
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc