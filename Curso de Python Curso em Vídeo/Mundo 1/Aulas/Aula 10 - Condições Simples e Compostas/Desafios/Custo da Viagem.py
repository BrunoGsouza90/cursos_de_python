distancia = float(input('Digite a distância da viagem em Km/h: '))
passagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da passagem é de R${:.2f}!'.format(passagem))
input('Digite "sair" para sair: ')