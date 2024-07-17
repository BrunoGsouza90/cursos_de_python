velocidade = int(input('Digite a velocidade do seu carro: '))
print('A velocidade da via é de 80km/h!')
if velocidade > 80:
    print('Você está multado!')
    multa = (velocidade - 80) * 7
    print('O valor da multa é de R${:.2f}!'.format(multa))
print('Siga em frente! Dirija com segurança!')
input('\nDigite "sair" para sair: ')