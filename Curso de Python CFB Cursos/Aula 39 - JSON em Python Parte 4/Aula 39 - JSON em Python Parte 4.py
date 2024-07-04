import json

with open('jogador.json') as f:
    jogador = json.load(f)

def linha():
    print('-=' * 20)

linha()

for c in jogador:
    print(c)

linha()

for c,v in jogador.items():
    print(f'{c} = {v}')

linha()