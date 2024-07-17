primeiro_termo = int(input('\n\033[1:34mDigite o primeiro termo da P.A:\033[m '))
termo_final = primeiro_termo + 10
razao = str(input('''\n    \033[1:33:40mClassificações da P.A\033[m
      \033[1:31m[1]\033[m \033[1:34mCrescente\033[m
      \033[1:31m[2]\033[m \033[1:34mDecrescente\033[m
      \033[1:31m[3]\033[m \033[1:34mConstante\033[m
      \033[1:34mReposta:\033[m ''')).strip().upper()
if razao == '1':
    pular = int(input('\n\033[1:34mVocê deseja pular de quantos em quantos números? \033[m'))
    for c in range(primeiro_termo,termo_final):
        print('\033[1:31m                   {}\033[m'.format(primeiro_termo))
        primeiro_termo = primeiro_termo + pular
elif razao == '2':
    pular = int(input('\n\033[1:34mVocê deseja pular de quantos em quantos números? \033[m'))
    for c in range(primeiro_termo,termo_final):
        print('\033[1:31m                   {}\033[m'.format(primeiro_termo))
        primeiro_termo = primeiro_termo - pular
elif razao == '3':
    for c in range(primeiro_termo,termo_final):
        print('\033[1:31m                   {}\033[m'.format(primeiro_termo))
input('\n\033[1:34mPara "sair" digite sair : \033[m')