expressao = input('\n\033[1:34mDigite a sua expressão: \033[m')
parenteses_aberto = expressao.count('(')
parenteses_fechado = expressao.count(')')
if parenteses_aberto == parenteses_fechado:
    print('\n\033[1:32mSua expressão está correta!\033[m')
else:
    print('\n\033[1:31mSua expressão está errada!\033[m')
input('\n\033[1:34mDigite "sair" para sair: ')