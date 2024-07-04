preco=float(input('\nDigite o preço do seu produto:\033[32mR$\033[m '))
print('O preço do seu produto com \033[33m5%\033[m de desconto é de \033[31mR$ {:.2f}\033[m'
      '!'.format(preco-(5*preco/100)))
input('\n\033[1:34'
      'mDigite "sair" para sair: \033[m')