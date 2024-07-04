carros = ["HRV","Golf","Argo","Focus"]
print(carros)
print(carros[0])
print(carros[-1])
print(carros[-2])
carros[3] = "Fusion"
print(carros)
carros.append('Fit')
carros.append('Polo')
carros.append('Civic')
carros.append('Celta')
print(carros)
print('A quantidade de carros impressa é igual a ' + str(len(carros)))
carros.remove('Celta')
print(carros)
print('A quantidade de carros impressa é igual a ' + str(len(carros)))
carros.pop()
print(carros)
carros.pop()
print(carros)
del carros[2]
print(carros)
del carros[-1]
print(carros)
carros.clear()
print(carros)
carros = ["HRV","Golf","Argo","Focus"]
print(carros)
carros2 = list(carros)
print(carros2)
carros2 = ["Fusca","Duster","Brasilia","Uno"]
carros3 = carros + carros2
print(carros3)
carros3.remove('Uno')
print(carros3)
del carros3[3]
print(carros3)