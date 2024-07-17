import datetime
cont = 1
lista = list()
lista1 = list()
dicionario = dict()
while True:
    print('\n' + '\033[1:31:40m-=\033[m' * 6 + f'\033[1:33:40m {cont}° Pessoa \033[m' + '\033[1:31:40m-=\033[m' * 6)
    nome = str(input(f'\n\033[1:34mDigite o nome: \033[m'))
    ano_nascimento = int(input('\033[1:34mDigite o ano de nascimento: \033[m'))
    pis = int(input('\033[1:34mDigite o seu numero PIS: \033[m'))
    dicionario = {'Nome':nome,
                  'Ano de Nascimento':ano_nascimento,
                  'PIS':pis,
                  }
    if pis != 0:
        ano_contratacao = int(input('\033[1:34mDigite o ano de contratação: \033[m'))
        salario = float(input('\033[1:34mDigite o salário atual:\033[m \033[1:32mR$ \033[m'))
        dicionario ['Ano de Contratação'] = ano_contratacao
        dicionario ['Salário'] = f'{salario:.2f}'
    lista.append(dicionario)
    resposta = str(input('\n\033[1:34mDeseja cadastras mais uma pessoa: \033[m')).strip().upper()[0]
    if resposta not in 'SN':
        print('\n\033[1:31:40mOpção Inválida!\033[m')
        resposta = str(input('\n\033[1:34mDeseja cadastras mais uma pessoa: \033[m')).strip().upper()[0]
    if resposta == 'N':
        break
    cont += 1
for c in lista:
    print(f'\n\033[1:31mO\033[m \033[1:33m{c['Nome']}\033[m \033[1:31mtem\033[m \033[1:33m{datetime.date.today().year - c['Ano de Nascimento']}\033[m \033[1:31manos. E vai se aposentar com\033[m \033[1:33m{c['Ano de Contratação'] + 35 - c['Ano de Nascimento']}\033[m \033[1:31manos !\033[m')
    print(f'\033[1:31mNome:\033[m \033[1:33m{c['Nome']}\033[m \033[1:31m.\033[m')
    print(f'\033[1:31mIdade:\033[m \033[1:33m{datetime.date.today().year - c ['Ano de Nascimento']}\033[m \033[1:31m.\033[m')
    print(f'\033[1:31mCTPS:\033[m \033[1:33m{c['PIS']}\033[m \033[1:31m.\033[m')
    print(f'\033[1:31mAno de Contratação:\033[m \033[1:33m{c ['Ano de Contratação']}\033[m \033[1:31m.\033[m')
    print(f'\033[1:31mSalário:\033[m \033[1:33m{'R$ ' + c['Salário']}\033[m \033[1:31m!\033[m')
    print(f'\033[1:31mAno de Aposentadoria:\033[m \033[1:33m{c['Ano de Contratação'] + 35 - c['Ano de Nascimento']}\033[m \033[1:31m.\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')