try:
    numerador = int(input('Numerador: '))
    denominador = int(input('Denominador: '))
    resposta = numerador / denominador
except (ValueError, TypeError):
    print(f'Tivemos problemas com os tipos e valores de todos que foram digitados!')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as error:
    print(f'O erro foi {error.__cause__}')
else:
    print(f'O resultado é {resposta:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')