import emoji

sexo = ''
print('\n\033[1:31mDigite o sexo\033[m \033[1:33m"M"\033[m \033[1:31mpara Masculino ou\033[m \033[1:33m"F"\033[m \033[1:31mpara Feminino...\033[m')
vezes = 1
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\n\033[1:34mDigite pela\033[m \033[1:31m{}º\033[m \033[1:34mvez o sexo:\033[m '.format(vezes))).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
        print('\n\033[1:31mDigite o sexo\033[m \033[1:33m"M"\033[m \033[1:31mpara Masculino ou\033[m \033[1:33m"F"\033[m \033[1:31mpara Feminino...\033[m')
    vezes += 1
if sexo == 'M':
    print('\n\033[1:31mO sexo digitado é\033[m \033[1:33mMasculino\033[m\033[1:31m!\033[m')
else:
    print('\n\033[1:31mO sexo digitado é\033[m \033[1:33mFeminino\033[m\033[1:31m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')