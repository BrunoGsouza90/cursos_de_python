palavras = ('aprender','progamar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','progamador','futuro')
for palavra in palavras:
    print(f'\033[1:31m!\033[m\n\033[1:31mNa palavra\033[m \033[1:33m{palavra}\033[m \033[1:31mtemos as seguintes vogais:\033[m ',end=' ')
    for letra in palavra:
        if letra in 'aeiou':
            print(f'\033[1:33m{letra}\033[m',end=' ')
input('\033[1:31m!\033[m\n\033[1:34mDigite "sair" para sair: \033[m')