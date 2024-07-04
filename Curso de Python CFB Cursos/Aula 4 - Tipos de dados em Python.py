x = 1  #int
x = "CFB Cursos"  #string
x = 15.6  #float
x = True  #bool
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))

x = 0
y = type(x) #type
print(type(y))

n1 = 5;
n2 = 2
x = complex(n1, n2)  #complex
print(x.real)
print(x.imag)
print(type(x))

x = ("Carro", "Avião", "Navio")  #tuple
y = "João", "Lucas", "Maria"  #tuple
print(x)
print(type(x))
print(y)
print(type(y))

x = ["Carro", "Avião", 1, 5.45, True]  #list / Array
x[0] = 'Oníbus'
print(x[0])
print(type(x))
print(type(x[0]))

x = range(0,100,1) #range
print(x)
print(type(x))

x = {
    "canal": "CFB Cursos",
    "curso": "Curso de Python",
    "nome": "Bruno"
} #Dict
print(x)
print(x["canal"])
print(x["curso"])
print(type(x))

x = {5,7,6,3,2,1,5} #set
y = {'Bruno','Lucas','Eduardo'}
print(x)
print(type(x))
print(y)
print(type(y))
x = frozenset({5,7,6,3,2,1,5}) #set bloqueado