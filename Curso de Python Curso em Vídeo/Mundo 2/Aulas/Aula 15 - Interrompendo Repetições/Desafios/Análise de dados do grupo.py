idade = sexo = maior_idade = homens = mulher_menor_idade = continuar = pessoa = 0
while True:
    pessoa += 1
    print(f'\n   \033[1:35:40m{pessoa}° PESSOA\033[m')
    idade = int(input('\n\033[1:34mDigite sua idade:\033[m '))
    sexo = str(input('\033[1:34mQual seu sexo?\033[m \033[1:35m[M/F]\033[m ')).strip().title()
    while not 'MmFf':
        print('\033[1:31:40mOpção Inválida!\033[m')
        sexo = str(input('\033[1:34mQual seu sexo?\033[m \033[1:35m[M/F]\033[m ')).strip().title()
    if idade > 18:
        maior_idade += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulher_menor_idade += 1
    continuar = str(input('\033[1:34mQuer continuar?\033[m \033[1:35m[S/N]\033[m ')).strip().title()
    while continuar not in 'SsNn':
        print('\033[1:31:40mOpção Inválida!\033[m')
        continuar = str(input('\033[1:34mQuer continuar?\033[m \033[1:35m[S/N]\033[m ')).strip().title()
    if continuar in 'Nn':
        break
print(f'\n\033[1:33m{maior_idade}\033[m \033[1:31mpessoas são maiores de 18 anos!\033[m')
print(f'\033[1:33m{homens}\033[m \033[1:31mhomens foram cadastrados!\033[m')
print(f'\033[1:33m{mulher_menor_idade}\033[m \033[1:31mmulheres são menores de idade!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')