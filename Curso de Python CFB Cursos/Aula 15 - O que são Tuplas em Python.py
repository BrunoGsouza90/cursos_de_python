lista_carros = ["HRV","Golf","Argo"]
lista_carros[2] = 'Focus'
print(lista_carros[2])                        #→        Aqui é possível fazer a alteração pois é uma lista.
print('')
for x in lista_carros:
    print(x)

tupla_carros = ("HRV","Golf","Argo")
# tupla_carros[2] = 'Focus'                    →        Erro pois uma tupla não pode ser alterada.
# print(tupla_carros[2])

print('')

tupla_carros = ("HRV","Golf","Argo")
lista_carros = list(tupla_carros)
lista_carros[2] = 'Focus'
tupla_carros = tuple(lista_carros)

for x in tupla_carros:
   print(x)