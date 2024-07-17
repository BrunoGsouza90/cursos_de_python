import time

lista = []
lista1 = []
lista_nota = []
cont = 1
while True:
    print('\n' + '\033[1:31:40m-=\033[m' * 7 + '\033[1:32:40m {}° Aluno \033[m'.format(cont) + '\033[1:31:40m-=\033[m' * 8)
    nome = str(input('\n\033[1:34mDigite o {}° nome: \033[m'.format(cont))).strip().title()
    nota1 = float(input('\033[1:34mDigite a primeira nota: \033[m'))
    nota2 = float(input('\033[1:34mDigite a segunda nota: \033[m'))
    media = (nota1 + nota2) / 2
    lista_nota.append(nota1)
    lista_nota.append(nota2)
    lista.append(lista_nota[:])
    lista_nota.clear()
    lista.append(nome)
    lista.append(media)
    lista1.append(lista[:])
    lista.clear()
    resposta = str(input('\n\033[1:34mDeseja cadastras mais um aluno?\033[m \033[1:35m[S/N] \033[m')).strip().upper()[0]
    while resposta not in 'SN':
        print('\n\033[1:31:40mOpção Inválida!\033[m')
        resposta = str(input('\n\033[1:34mDeseja cadastras mais um aluno?\033[m \033[1:35m[S/N] \033[m')).strip().upper()[0]
    if resposta in 'Nn':
        break
    cont += 1
print(lista1)
print('\n' + '\033[1:31m-=\033[m' * 20)
print('\033[1:32mNo.\033[m \033[1:35mNome         MÉDIA\033[m')
print('\033[1:31m-\033[m' * 30)
for numero,lista_pequena in enumerate(lista1):
    print(f'\033[1:32m{numero}\033[m\033[1:33m{lista_pequena[1]:>8}\033[m\033[1:33m{lista_pequena[0][0]:>12}\033[m')
while True:
    print('\n\033[1:31mDigite\033[m \033[1:33m"999"\033[m \033[1:31mpara não cadastrar nenhum cliente!\033[m')
    id = int(input('\033[1:34mDigite o\033[m \033[1:32m"id"\033[m\033[1:34m do aluno que quer ver as notas: \033[m'))

    while id >= len(lista1) and id != 999:
        print('\n\033[1:31:40mOpção Inválida!\033[m')
        print('\n\033[1:31mDigite\033[m \033[1:33m"999"\033[m \033[1:31mpara não cadastrar nenhum cliente!\033[m')
        id = int(input('\033[1:34mDigite o\033[m \033[1:32m"id"\033[m\033[1:34m do aluno que quer ver as notas: \033[m'))
    if id == 999:
        break
    print(f'\n\033[1:31mAs notas do(a) aluno(a) são:\033[m \033[1:33m{lista1[id][0][0]}\033[m\033[1:31m ,\033[m \033[1:33m{lista1[id][0][1]}\033[m \033[1:31m!\033[m')
print('\n\033[1:35mFinalizando...\033[m')
time.sleep(2)
print('\n\033[1:32mVolte sempre!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')