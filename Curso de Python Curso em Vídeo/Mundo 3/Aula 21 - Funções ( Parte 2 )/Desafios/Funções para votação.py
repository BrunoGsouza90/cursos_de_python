def voto(ano_de_nascimento=0):
    import datetime
    idade = datetime.date.today().year - ano_de_nascimento
    print(f'\n\033[1:31mVocê tem\033[m \033[1:33m{idade}\033[m \033[1:31manos! \033[m')
    if idade < 16:
        print('\n\033[1:31mVocê ainda não pode votar! \033[m')
    elif (idade > 15 and idade < 18) or idade > 65:
        print('\n\033[1:33mVoto Opcional! \033[m')
    elif idade > 18 and idade < 65:
        print('\n\033[1:32mVoto Obrigatório! \033[m')


ano_de_nascimento = int(input('\n\033[1:34mDigite seu ano de nascimento: \033[m'))
voto(ano_de_nascimento)

input('\n\033[1:34mDigite "sair" para sair: \033[m')