celsius=int(input('\nDigite a quantidade de graus em °C: '))
print('A quantidade de \033[33m{}°C\033[m em Fahrenheit é de \033[31m{:.0f}°F\033[m!'.format(celsius,((9 * celsius) / 5) + 32))
input('\n\033[1:34mDigite "sair" para sair: \033[m')