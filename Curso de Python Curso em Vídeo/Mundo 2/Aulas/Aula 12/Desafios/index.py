while True:
    print('\n\033[1:31mDigite\033[m \033[1:33m"999"\033[m \033[1:31mpara não cadastrar nenhum cliente!\033[m')
    id = int(input('\033[1:34mDigite o\033[m \033[1:32m"id"\033[m\033[1:34m do aluno que quer ver as notas: \033[m'))

    while id >= len(lista1) and id != 999:
        print('\n\033[1:31:40mOpção Inválida!\033[m')
        print('\n\033[1:31mDigite\033[m \033[1:33m"999"\033[m \033[1:31mpara não cadastrar nenhum cliente!\033[m')
        id = int(input('\033[1:34mDigite o\033[m \033[1:32m"id"\033[m\033[1:34m do aluno que quer ver as notas: \033[m'))
    if id == 999:
        break
    print(f'\n\033[1:31mAs notas do(a) aluno(a) são:\033[m \033[1:33m{lista1[id][1]}\033[m\033[1:31m ,\033[m \033[1:33m{lista1[id][2]}\033[m \033[1:31m!\033[m')
time.sleep(2)
print('\033[1:35mFinalizando...\033[m')