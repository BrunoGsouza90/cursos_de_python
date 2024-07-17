print('\033[1:31:40mNúmeros pares de 1 até 49!\033[m')
num = 0
for c in range(2,49,2):
    num = num + 2
    print('\033[1:31m           {}\033[m'.format(num))
print(('\033[1:32m=-\033[m' * 13))
print('          \033[1:32mFim\033[m')
print(('\033[1:32m=-\033[m' * 13
       ))
input('\n\033[1:34mPara "sair" digite sair : \033[m')