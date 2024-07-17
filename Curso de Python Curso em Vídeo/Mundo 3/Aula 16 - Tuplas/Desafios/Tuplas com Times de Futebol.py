times = ('Athletico-PR','Bahia','Flamengo','Botafogo','São Paulo','Cruzeiro','Atlético - MG','Bragantino','Palmeiras','Internacional','Fortaleza','Grêmio','Vasco da Gama','Criciúma','Juventude','Corinthians','Fluminense','EC Vitória','Atlético - GO','Cuiabá')
print(f'\n\033[1:35mOs times do brasileirão são:\033[m \033[1:33m{times}\033[m')
print(f'\n\033[1:35mOs 5 primeiros colocados no brasileirão foram:\033[m')
for cont,time in enumerate(times):
    if cont < 5:
        print(f'\033[1:33m{cont + 1}° Lugar\033[m - \033[1:31m{time}\033[m')
print(f'\n\033[1:35mOs 4 últimos colocados no brasileirão:\033[m')
for cont,time in enumerate(times):
    if cont > 15:
        print(f'\033[1:33m{cont + 1}° Lugar\033[m - \033[1:31m{time}\033[m')
print(f'\n\033[1:35mOs times em ordem alfabética:\033[m \033[1:33m{sorted(times)}\033[m')
colocacao = str(input('\n\033[1:34mDigite o time que você quer a colocação:\033[m '))
print(f'\033[1:31mO time\033[m \033[1:33m{colocacao}\033[m \033[1:31mestá na\033[m \033[1:33m{times.index(colocacao) + 1}°\033[m \033[1:31mposição!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')