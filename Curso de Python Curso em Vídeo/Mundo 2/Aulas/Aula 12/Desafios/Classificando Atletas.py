import datetime

ano = int(input('\nDigite seu ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - ano
if idade <= 9:
    print('Sua classificação é \033[1:31mMirim\033[m!')
elif idade <= 14:
    print('Sua classificação é \033[1:31mInfantil\033[m!')
elif idade <= 19:
    print('Sua classificação é \033[1:31mJunior\033[m!')
elif idade == 20:
    print('Sua classificação é \033[1:31mSênior\033[m!')
else:
    print('Sua classificação é \033[1:31mMaster\033[m!')
input('\n\033[1:34mDigite "sair" para sair: \033[m')