def somar(n1,n2,n3,n4):
    r = n1 + n2 + n3 + n4
    print("Soma " + " = " + str(r))
    print('youtube.com/cfbcursos\n')
somar(5,7,3,2)
somar(12,8,1,20)
somar(1,2,0,0)

print('')

def somar(*n):
    r = n[0] + n[1] + n[2] + n[3]
    print("Soma " + " = " + str(r))
    print('youtube.com/cfbcursos\n')
somar(5,7,3,2)
somar(12,8,1,20)
somar(1,2,0,0)

print('')

def textos(*txt):
    for t in txt:
        print(t)
textos('CFB Cursos','Python','Canal','Curso','Computador')

print('')

def somar(*num):
    r = 0
    for n in num:
        r += n
    print("Soma " + " = " + str(r))
    print('youtube.com/cfbcursos\n')
somar(5,2,3)

print('')

def carros(c = 'Golf'):
    print("Modelo: " + c)
carros()

print('')

valores = [1,5,3,2]
def somar(num):
    r = 0
    for n in num:
        r += n
    print("Soma = " + str(r))
    print("youtube.com/cfbcursos\n")
somar(valores)