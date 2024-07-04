curso = 'Curso de Python'
res = 'Python' in curso
print(res)
res = 'Python' not in curso
print(res)
res = 'python' in curso
print(res)

texto = 'Curso de Python'
palavra = 'python'
res = palavra in texto
print(res)
res = palavra.upper() in texto.upper()
print(res)
curso = 'Curso de Python'
canal = 'CFB Cursos'

res = curso + ' do canal ' + canal
print(res)
cidade = 'Belo Horizonte'
dia = 15
mes = 'Dezembro'
ano = 2019
print(cidade + ', ' + str(dia) + ' de ' + mes + ' de ' + str(ano))

data = '{}, {} de {} de {}'.format(cidade,dia,mes,ano)
print(data)
data = '{}, {} de {} de {}'
print(data.format(cidade,dia,mes,ano))

print('Itamonte \nItanhandu \nPassa Quatro')
print('O gato de \'Botas\'!')
print('O gato de \"Botas\"!')
print('Lucas')
print('Bruno Gonçalves de Souza \rItamonte-MG')
print('\tBruno Gonçalves de Souzaa\b')