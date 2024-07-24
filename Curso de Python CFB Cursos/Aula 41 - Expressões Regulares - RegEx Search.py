import re

texto = 'Curso de Python do CFB Cursos, canal do youtube'

try:
    resultado = re.search('o', texto)
    print(resultado.start())
    print(resultado.end())
except AttributeError:
    print('Atributo não existe!')