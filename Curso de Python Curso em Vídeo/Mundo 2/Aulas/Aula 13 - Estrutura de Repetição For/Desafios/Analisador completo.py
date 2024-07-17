nome1 = str(input('\nDigite o primeiro nome: ')).strip().title()
idade1 = int(input('Digite a primeira idade: '))
sexo1 = str(input('Digite o primeiro Sexo: ')).upper()
nome2 = str(input('\nDigite o segundo nome: ')).strip().title()
idade2 = int(input('Digite a segunda idade: '))
sexo2 = str(input('Digite o segundo Sexo: ')).upper()
nome3 = str(input('\nDigite o terceiro nome: ')).strip().title()
idade3 = int(input('Digite a terceira idade: '))
sexo3 = str(input('Digite o terceiro Sexo: ')).upper()
nome4 = str(input('\nDigite o quarto nome: ')).strip().title()
idade4 = int(input('Digite a quarta idade: '))
sexo4 = str(input('Digite o quarto Sexo: ')).upper()
idades = [idade1,idade2,idade3,idade4]
nomes = [nome1,nome2,nome3,nome4]
sexos = [sexo1,sexo2,sexo3,sexo4]
posicao1 = 0
posicao2 = 1
maioridade = 0
for c in range(0,3):
    if sexos[posicao1] == 'M' and idades[posicao2] == 'M':
        if idades[posicao1] > idades[posicao2]:
            maioridade = nomes[posicao1]
            posicao2 += 1
        else:
            maioridade = nomes[posicao2]
            posicao1 = posicao2
            posicao2 += 1
    else:
        if sexos[posicao1] == 'M':
            maioridade = nomes[posicao1]
            posicao2 += 1
        else:
            maioridade = nomes[posicao2]
            posicao1 = posicao2
            posicao2 += 1
posicao = 0
menoridade = 0
for c in range(0,4):
    if sexos[posicao] == 'F':
        if idades[posicao] < 20:
            menoridade += 1
        posicao += 1
    else:
        posicao += 1
media_idade = (idade1 + idade2 + idade3 + idade4) / 4
print('\033[1:31m\nA média de idade do grupo é\033[m \033[1:33m {:.0f}\033[m\033[1:31m!\033[m'.format(media_idade))
print('\033[1:31mO homem mais velho do grupo é o\033[m \033[1:33m{}\033[m\033[1:31m!\033[m'.format(maioridade))
print('\033[1:31mNo grupo há\033[m \033[1:33m{}\033[m \033[1:31mmulhere(s) de menoridade!\033[m'.format(menoridade))
input('\n\033[1:34mPara "sair" digite sair : \033[m')