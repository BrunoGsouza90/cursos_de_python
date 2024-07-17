valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c,v in enumerate(valores):
    print(f'{c+1}° posição = {v} ')
print('Cheguei no final da lista!')

a = [2,3,4,7]
b = a
b[2] = 8
c = a[:]
c[2] = 3
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
input('\n\033[1:34mDigite "sair" para sair: \033[m')