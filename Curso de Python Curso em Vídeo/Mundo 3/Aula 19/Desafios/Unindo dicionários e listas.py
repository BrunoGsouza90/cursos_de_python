dicionario = dict()
lista = list()
lista_mulheres = list()
lista_maiores_idade = list()
cont = 1
total_idade = 0
while True:
    print("\n" + "\033[1:31:40m-=\033[m" * 8 + f"\033[1:33:40m {cont}° Pessoa \033[m" + "\033[1:31:40m-=\033[m" * 9)
    nome = str(input(f"\n\033[1:34mDigite o nome da {cont}° Pessoa: \033[m"))
    sexo = str(input(f"\033[1:34mDigite o sexo da {cont}° Pessoa: \033[m")).strip().upper()[0]
    while sexo not in 'MF':
        print('\n\033[1:31mOpção Inválida!\033[m')
        sexo = str(input(f"\033[1:34mDigite o sexo da {cont}° Pessoa: \033[m")).strip().upper()[0]
    if sexo == 'F':
        lista_mulheres.append(nome)
    idade = int(input(f"\033[1:34mDigite a idade da {cont}° Pessoa: \033[m"))
    total_idade += idade
    dicionario = {'Nome': nome,
                  'Sexo': sexo,
                  'Idade': idade,
                  }
    lista.append(dicionario)
    resposta = str(input("\n\033[1:34mQuer cadastrar outro jogador? \033[m")).strip().upper()[0]
    if resposta not in "SN":
        print("\n\033[1:31:40mOpção Inválida! \033[m")
        resposta = str(input("\n\033[1:34mQuer cadastras outro jogador? \033[m")).strip().upper()[0]
    if resposta == "N":
        break
    cont += 1
media = total_idade / cont
print(f"\n\033[1:31mForam cadastradas\033[m \033[1:33m{cont}\033[m \033[1:31mpessoas!\033[m")
print(f"\033[1:31mA média de idade do grupo é:\033[m \033[1:33m{int(media)} anos\033[m \033[1:31m!\033[m")
if len(lista_mulheres) > 0:
    print("\033[1:31mA lista de todas as mulheres é: \033[m")
    for c in lista_mulheres:
        print(f"\033[1:35m==>\033[m \033[1:33m{c}\033[m")
for c in lista:
    if c['Idade'] > media:
        lista_maiores_idade.append(c['Nome'])
if len(lista_maiores_idade) > 0:
    print(f"\033[1:31mA lista com as pessoas acima da média de idade do grupo é:\033[m \033[1:33m{lista_maiores_idade}\033[m \033[1:31m!\033[m")
input("\n\033[1:34mDigite \"sair\" para sair: ")