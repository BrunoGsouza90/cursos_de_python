reta1 = float(input('\nDigite o valor do primeiro seguimento em reta: '))
reta2 = float(input('Digite o valor do segundo seguimento em reta: '))
reta3 = float(input('Digite o valor do terceiro seguimento em reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('\n\033[1:32mÉ possível formar o triângulo!\033[m')
    if reta1 == reta2 and reta2 == reta3:
        print('O triângulo formado é um \033[1:33mEquilátero\033[m!')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('O triângulo formado é um \033[1:33mIsósceles\033[m!')
    else:
        print('O triângulo formado é um \033[1:33mEscaleno\033[m!')
else:
    print('\n\033[1:31mNão é possível formar um triângulo!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')