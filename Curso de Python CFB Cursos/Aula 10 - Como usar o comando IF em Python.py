a = True
if a is True:
    print('CFB Cursos')
print('Fim do Progama')

a = False
if a is True:
    print('CFB Cursos')
print('Fim do Progama')

a = 10
b = 5
if a > b:
    print("CFB Cursos")
print('Fim do Progama')
if a < b:
    print("CFB Cursos")
print('Fim do Progama')

a = 10
b = 5
res = 0
operacao = "+"
if operacao == "+":
    res = a + b
print("Operacao " + operacao + " : " + str(res))

a = 10
b = 5
res = 0
operacao = "-"
if operacao == "+":
    res = a + b
print("Operacao " + operacao + " : " + str(res))


a = 10
b = 5
res = 0
operacao = "/"
if operacao == "+":
    res = a + b

if operacao == "-":
    res = a - b

if operacao == "*":
    res = a * b

if operacao == "/":
    res = a / b

print(str(a) + operacao + str(b) + ' = ' + str(res))