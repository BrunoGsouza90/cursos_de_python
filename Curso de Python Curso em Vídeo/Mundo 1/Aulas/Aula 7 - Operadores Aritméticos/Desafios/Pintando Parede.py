largura=int(input('\nDigite a largura da parede em metros: '))
altura=int(input('Digite a altura da parede em metros: '))
area = largura * altura
print('A área da sua parede é de \033[31m{}m²\033[m,'.format(area),end=' ')
print('e você precisa de \033[31m{}\033[m litros de tinta para pintar toda sua parede!'.format(area//2))
input('\n\033[1:34mDigite "sair" para sair: \033[m')