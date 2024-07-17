import emoji

peso = float(input('\nDigite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('\n\033[1:31mVocê está abaixo do peso!\033[m')
elif imc == 18.5 or imc < 25:
    print('\n\033[1:32mSeu peso é ideal!\033[m')
elif imc == 25 or imc < 30:
    print('\n\033[1:33mVocê está sobre o peso! Cuidado!\033[m')
elif imc == 30 or imc <= 40:
    print('\n\033[1:31mVocê está em obesidade!\033[m')
else:
    print('\n\033[1:31m{}Você está em Obesidade Mórbida!{}\n\033[31m'.format(emoji.emojize('\u274C\u274C\u274C\u274C',language='pt'),emoji.emojize('\u274C\u274C\u274C\u274C',language='pt')))
input('\n\033[1:34mDigite "sair" para sair: \033[m')