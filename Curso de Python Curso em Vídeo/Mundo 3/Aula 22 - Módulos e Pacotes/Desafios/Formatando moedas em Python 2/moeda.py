def aumentar(preco=0, taxa=0, formato=True):
   resultado = preco + (preco * taxa / 100)
   return resultado if formato is False else moeda(resultado)


def diminuir(preco=0, taxa=0, formato=True):
    resultado = preco - (preco * taxa / 100)
    return resultado if not formato else moeda(resultado)


def dobro(preco=0, formato=True):
    resultado = preco * 2
    return resultado if formato is False else moeda(resultado)


def metade(preco=0, formato=True):
    resultado = preco / 2
    return resultado if formato is False else moeda(resultado)

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.',',')
