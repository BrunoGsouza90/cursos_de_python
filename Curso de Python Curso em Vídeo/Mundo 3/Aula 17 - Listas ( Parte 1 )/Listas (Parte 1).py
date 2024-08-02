#num = (2,5,9,1)
#num[2] = 3
#print(num)     Erro pois as tuplas são imutáveis.
num = [2,5,9,1]
num[2] = 3
print(num)
#num [4] = 7
#print(num)     Erro pois não é dessa maneira que se adicionam valores em uma lista.
num.append(7)
num.sort()
print(num)
num = sorted(num)
print(num)
num = list(reversed(num))
print(num)
num.sort()
print(num)
num.reverse()
print(num)
num.sort(reverse=True)
print(num)
print('')
num.insert(0,9)
print(num)
print('')
num.pop()
print(num)
num.pop(0)
print(num)
del num[0]
print(num)
num.insert(0,2)
print(num)
num.remove(2)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4!')
input('\n\033[1:34mDigite "sair" para sair: \033[m')