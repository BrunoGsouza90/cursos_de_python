nome = input ('\nQual é o seu nome? ')
print('Prazer em te conhecer \033[1:31m{:=^20}\033[m!'.format(nome))
n1 = int(input('\nUm valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale \033[31m{}\033[m'.format(n1+n2))
print ('A soma é \033[31m{}\033[m, a multiplicação é \033[31m{}\033[m, a divisão é \033[31m{:.3f}\033[m, a divisão inteira é \033[31m{}\033[m, e a exponenciação é \033[31m{}\033[m!'.format(s,m,d,di,e))
input('\n\033[1:34mDigite "sair" para sair: \033[m')