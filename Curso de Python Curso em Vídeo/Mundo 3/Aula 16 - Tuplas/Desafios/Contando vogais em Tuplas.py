palavras = ('aprender','progamar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','progamador','futuro')
consoantes = ('bcdfghjklmnpqrstvwxyz')

for palavra in palavras:
    p = palavra
    for vogal in consoantes:
        palavra = palavra.replace(vogal,'')
    print(f'\033[1:31mAs vogais na palavra\033[m \033[1:33m{p.upper()}\033[m \033[1:31msão:\033[m \033[1:33m{' '.join(palavra)}\033[m \033[1:31m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')