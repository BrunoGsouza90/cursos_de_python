valor = soma = cont = 0
while True:
    valor = int(input('\n\033[1:34mDigite um valor:\033[m '))
    if valor == 999:
        break
    soma += valor
    cont += 1
print(f'\033[1:31mForam digitados\033[m \033[1:33m{cont}\033[m \033[1:31mnúmeros e a soma de todos eles é\033[m \033[1:33m{soma}\033[m\033[1:31m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')