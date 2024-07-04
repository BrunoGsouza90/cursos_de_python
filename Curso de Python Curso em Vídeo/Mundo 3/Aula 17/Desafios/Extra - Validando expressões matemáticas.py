lista = list()
expressao = str(input('\n\033[1:34mDigite a sua expressão: \033[m'))
for c in expressao:
    if c == '(':
        lista.append('(')
    else:
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('\n\033[1:32mSua expressão está válida!\033[m')
else:
    print('\n\033[1:31mSua expressão está incorreta!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')