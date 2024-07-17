import emoji
nome = str(input('Digite o seu primeiro nome: '))
if nome == 'Bruno':
    print('Seu nome é top meu parceiro {}'.format(emoji.emojize('\U0001f4aa',language='pt')))
if nome == 'Raiani':
    print('Bom dia só se for pra você, pra mim é só dia, o bom já se foi {}'.format(emoji.emojize('\U0001f642', language='pt')))
else:
    print('Bom dia {} {}'.format(nome,emoji.emojize('\u2600\uFE0F',language='pt')))
idade = int(input('Qual é a sua idade? '))
print('Você é maior de idade!' if idade >= 18 else 'Você é menor de idade!')
input('Digite "sair" para sair: ')