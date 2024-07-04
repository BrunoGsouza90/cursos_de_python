print('')
for c in range(1,5):
    n = int(input('\033[1:33mDigite um valor: \033[m'))
print('\n\033[1:31:40mFim\033[m\n')

c = 1
while c < 5:
    n = int(input('\033[1:33mDigite um valor: \033[m'))
    c += 1
print('\n\033[1:31:40mFim\033[m')

input('\n\033[1:34mDigite "sair" para sair: \033[m')