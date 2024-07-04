teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste) #  O valor salvo na lista "teste" está vinculado a lista "galera".
print(galera)
teste[0] = 'Maria'
teste[1] = 22
print(galera)
pessoas = list()
pessoas = teste[:]  #  O valor salvo na lista "teste" não está vinculado a lista "pessoas".
teste[0] = 'Bruno'
teste[1] = 33
print(pessoas)
print(galera)
input('\n\033[1:34mDigite "sair" para sair: \033[m')