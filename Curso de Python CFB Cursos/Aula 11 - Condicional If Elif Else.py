a = 10
b = 5
res = 0
operacao = '$'

if operacao == '+':
    res = a + b
    print(str(a) + operacao + str(b) + ' = ' + str(res))
elif operacao == '-':
    res = a - b
    print(str(a) + operacao + str(b) + ' = ' + str(res))
elif operacao == '*':
    res = a * b
    print(str(a) + operacao + str(b) + ' = ' + str(res))
elif operacao == '/':
    res = a / b
    print(str(a) + operacao + str(b) + ' = ' + str(res))
else:
    print('Operador Inválido!')

clima = 'sol'
dinheiro = 350
lugar = ''

if clima == 'sol' or dinheiro > 300 and dinheiro < 500:
    lugar = 'clube'
else:
    lugar = 'cinema'
print('Vou ao ' + lugar)