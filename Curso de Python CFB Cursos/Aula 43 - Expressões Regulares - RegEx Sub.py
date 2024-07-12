import re

texto = 'Curso de Python do CFB Cursos, canal do Youtube'

resultado = re.sub(',','.', texto)
resultado = re.sub('C','Q', resultado)
resultado = re.sub('e','r', resultado)

print(resultado)