def leiaInt():
    while True:
        try:
            num_inteiro = int(input('Digite um número inteiro: '))
            break
        except ValueError:
            print('ERRO: por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
    return num_inteiro

def leiaFloat():
    while True:
        try:
            num_real = float(input('Digite um número real: '))
            break
        except ValueError:
            print('ERRO: por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
    return num_real

print(f'O valor inteiro digitado foi {leiaInt()} e o real foi {leiaFloat()}!')

input('Digite "sair" para sair: ')