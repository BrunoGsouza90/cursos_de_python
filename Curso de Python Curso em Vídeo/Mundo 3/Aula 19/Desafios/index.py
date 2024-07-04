lista=[
    {'codigo':1, 'nome':'Deivis', 'gols':1, 'total':1},
    {'codigo':20, 'nome':'Pedro Belchior', 'gols':3, 'total':3},
    {'codigo':3, 'nome':'Noah Belchior Lenze de Menezes', 'gols':15, 'total':15},
    ]

print(f'{"Cod.":<10}{"Nome":40}{"Gols":>10}{"Total":>15}')
# Cod.: Alinhado a esquerda preenchido com 10 espaços em branco
# Nome: Alinhado a esquerda preenchido com 40 espaços em branco
# Gols: Alinhado a direita preenchido com 10 espaços em branco
# Total: Alinhado a direita preenchido com 15 espaços em branco

for item in lista:
    print(f'{item["codigo"]:<10}{item["nome"]:<47}{item["gols"]:<15}{item["total"]:<30}')