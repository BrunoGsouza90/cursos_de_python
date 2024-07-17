aluno = dict()
aluno['Nome'] = str(input('\n\033[1:34mDigite o nome do aluno: \033[m'))
aluno['Média'] = float(input('\033[1:34mDigite a média do aluno: \033[m'))
print(f'\n\033[1:31mO nome do(a) aluno(a) é\033[m \033[1:33m{aluno['Nome']}\033[m \033[1:31m!\033[m')
print(f'\033[1:31mA média do(a)\033[m \033[1:33m{aluno['Nome']}\033[m \033[1:31m é igual a \033[m \033[1:33m{aluno['Média']:.1f}\033[m \033[1:31m!\033[m')
if aluno['Média'] > 7:
    aluno['Situação'] = '\033[1:32mAprovado\033[m'
elif aluno['Média'] == 7:
    aluno['Situação'] = '\033[1:35mem\033[m' + ' \033[1:33mRecuperação\033[m'
else:
    aluno['Situação'] = '\033[1:31mReprovado\033[m'
print(f'\033[1:35mO aluno está\033[m {aluno['Situação']}\033[1:35m!\033[m')
input('\n\033[1:34mDigite "sair" para sair: \033[m')