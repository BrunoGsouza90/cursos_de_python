frase = str(input('\nDigite uma frase: ')).strip().upper()
frase = frase.split()
frase = ''.join(frase)
frase1 = frase[::-1]
frase1 = frase1.split()
frase1 = ''.join(frase1)
if frase1 == frase:
    print('\n\033[1:32mÉ um políndromo!\033[m')
else:
    print('\n\033[1:31mNão é um políndromo!\033[m')
input('\n\033[1:34mPara "sair" digite sair : \033[m')