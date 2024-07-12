import re #RegEx

texto = "Curso de Python do CFB Cursos, canal do youtube"
resultado1 = re.findall("Python", texto)
resultado2 = re.findall("so", texto)
resultado3 = re.findall("o", texto)

print(f'{resultado1[0]} = {len(resultado1)}')
print(f'{resultado2[0]} = {len(resultado2)}')
print(f'{resultado3[0]} = {len(resultado3)}')

print('')

texto = "Estudar é bom... Estudar programação é demais!".upper().strip()
pesquisar = input('Pesquisar: ').upper().strip()
resultado4 = re.findall(pesquisar, texto)

print(f'{resultado4[0].capitalize()} = {len(resultado4)}')

quantidade = len(resultado4)

print(f'Quantidade: {str(quantidade)}')

for palavra in resultado4:
    print(palavra.capitalize())