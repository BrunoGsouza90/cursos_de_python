import re

texto = 'Curso de Python do CFB Cursos, canal do Youtube'

resultado = re.split(' ', texto)

print(resultado)
print(resultado[0])
print(resultado[1])
print(resultado[2])

for palavra in resultado:
    print(palavra, end=' ')