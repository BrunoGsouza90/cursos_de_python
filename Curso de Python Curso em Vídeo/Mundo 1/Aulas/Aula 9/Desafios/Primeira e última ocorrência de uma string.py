frase = str(input('Digite uma frase: ')).upper().strip()
quantidade = frase.count('A')
print('A letra "A" apareceu {} vezes!'.format(quantidade))
primeiro = frase.find("A")+1
ultimo = frase.rfind("A")+1
print('A posição do primeiro "A" digitado é a posição {}, e a posição do último "A" digitado é a posição {}!'.format(primeiro,ultimo))
input('Digite "sair" para sair: ')