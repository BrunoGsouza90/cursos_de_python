km=int(input('\nQual a quantidade de kilômetro percorrido pelo carro? '))
dias=int(input('Qual a quantidade de dias que o carro foi alugado? '))
print('A quantidade a pagar pelo carro alugado é de \033[31mR$ {:.2f}\033[m!'.format(km*0.15+dias*60))
input('\n\033[1:34mDigite "sair" para sair: \033[m')