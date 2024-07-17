preco=float(input('\nDigite o preço do seu produto: \033[32mR$\033[m '))
print('Avista no débito seu produto custará \033[31mR$ {:.2f}\033[m com \033[33m10%\033[m de desconto, e avista no crédito seu produto custará \033[31mR$ {:.2f}\033[m com \033[33m5%\033[m de desconto.'.format(preco-(preco*10/100),preco-(preco*5/100)))
input('\n\033[1:34mDigite "sair" para sair: \033[m')