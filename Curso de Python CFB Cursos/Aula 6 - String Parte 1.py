import random

curso = 'Curso de Python'
print(curso[0])
print(curso[9])
print(curso[9:15])
print("Tamanho: " + str(len(curso)))
curso = '   Curso de Python   '
print("Tamanho: " + str(len(curso)))
curso = curso.strip()
print("Tamanho: " + str(len(curso)))
curso = curso.lower()
print(curso)
curso = curso.upper()
print(curso)
curso = curso.replace('PYTHON','C#')
print(curso)
curso = curso.replace('C#','PYTHON')
print(curso)
curso = curso.split()
print(curso)
print(curso[0])
print(curso[0:3])

