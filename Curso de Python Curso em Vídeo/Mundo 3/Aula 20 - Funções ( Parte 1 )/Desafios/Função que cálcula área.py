def area(largura,comprimento):
    area_do_terreno = largura * comprimento
    print(f'\n\033[1:31mA área do terreno é\033[m \033[1:33m{area_do_terreno}m²\033[m\033[1:31m!\033[m')

largura = float(input('\n\033[1:34mDigite a largura do terreno: \033[m'))
comprimento = float(input('\033[1:34mDigite o comprimento do terreno: \033[m'))
area(largura,comprimento)

input('\n\033[1:34mDigite "sair" para sair: \033[')