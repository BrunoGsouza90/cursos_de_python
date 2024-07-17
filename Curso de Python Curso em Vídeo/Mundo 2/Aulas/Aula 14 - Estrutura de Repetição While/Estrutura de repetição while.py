print('')
for c in range(1,10):
    print('\033[1:31m',c,'\033[m',end='→')
print(' \033[1:31:40mFim\033[m')

c = 1
while (c < 10):
     print('\033[1:31m',c,'\033[m',end='→')
     c += 1
print(' \033[1:31:40mFim\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')