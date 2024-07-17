tupla = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
resposta = 'S'
while resposta == 'S':
    num = int(input('\n\033[1:34mDigite um número: \033[m'))
    while num < 0 or num > 20:
        print('\033[1:31:40mOpção Inválida!\033[m')
        num = int(input('\n\033[1:34mDigite um número: \033[m'))
    print(f'\n\033[1:31mO número digitado foi o \033[m\033[1:33m{tupla[num]}\033[m\033[1:31m!\033[m')
    resposta = str(input('\n\033[1:34mQuer continuar? [S/N] \033[m ')).upper().strip()[0]
    while resposta not in 'SsNn':
        print('\033[1:31:40mOpção Inválida!\033[m')
        resposta = str(input('\n\033[1:34mQuer continuar? [S/N] \033[m ')).upper().strip()[0]
input('\n\033[1:34mDigite "sair" para sair: \033[m')