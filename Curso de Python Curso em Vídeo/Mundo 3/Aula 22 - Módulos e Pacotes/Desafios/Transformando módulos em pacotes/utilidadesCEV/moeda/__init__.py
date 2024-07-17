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


def resumo(preco=0, taxa_aumento=10, taxa_reducao=5):
    print('\n' + '-=' * 15)
    print('RESUMO DO VALOR'.center(30))
    print('-=' * 15)
    print(f'Preço analisado: {moeda(preco)}')
    print('-=' * 15)
    print(f'Dobro do preço: {dobro(preco)}')
    print('-=' * 15)
    print(f'Metade do preço: {metade(preco)}')
    print('-=' * 15)
    print(f'Com {taxa_aumento}% de aumento: {aumentar(preco, taxa_aumento, True)}')
    print('-=' * 15)
    print(f'Com {taxa_reducao}% de aumento: {diminuir(preco, taxa_reducao, True)}\n')