try:
    print(x)
except:
    print("Erro no progama!")
else:
    print("Tudo certo!")
finally:
    print("Fim do tratamento! ")

print('')

try:
    print(x)
except NameError:
    print("Erro no progama!")
else:
    print("Tudo certo!")
finally:
    print("Fim do tratamento! ")

print('')

x = 2
try:
    print(x)
except:
    print("Erro no progama!")
else:
    print("Tudo certo!")
finally:
    print("Fim do tratamento! ")

print('')

num = "Bruno"
if not type(num) is int:
    raise Exception("Somente números permitidos!")
else:
    print(num)