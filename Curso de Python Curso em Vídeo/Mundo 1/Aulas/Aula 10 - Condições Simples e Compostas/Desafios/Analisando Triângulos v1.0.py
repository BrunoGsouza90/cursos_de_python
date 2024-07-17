reta1 = float(input('Digite o valor do primeiro seguimento em reta: '))
reta2 = float(input('Digite o valor do segundo seguimento em reta: '))
reta3 = float(input('Digite o valor do terceiro seguimento em reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('É possível formar o triângulo!')
else:
    print('Não é possível formar um triângulo!')
input('Digite "sair" para sair: ')