funcionarios = list()
class pessoas:
    def __init__(self,nome,idade,telefone,cidade,salario,horario):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = cidade
        self.salario = salario
        self.horario = horario
    def mostrar(self):
        print(f'\nNome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Telefone: {self.telefone}')
        print(f'Cidade: {self.cidade}')
        print(f'Salario: {self.salario}')
        print(f'Horário: {self.horario}')

class Proprietario(pessoas):
    def __init__(self, nome, idade, telefone, cidade):
        self.salario = 40000
        self.horario = 14
        super().__init__(nome,idade,telefone,cidade,self.salario,self.horario)
class Gerente(pessoas):
    def __init__(self, nome, idade, telefone, cidade):
        self.salario = 20000
        self.horario = 4
        super().__init__(nome,idade,telefone,cidade,self.salario,self.horario)
class Mecanico(pessoas):
    def __init__(self, nome, idade, telefone, cidade):
        self.salario = 4000
        self.horario = 6
        super().__init__(nome,idade,telefone,cidade,self.salario,self.horario)
class Operador(pessoas):
    def __init__(self, nome, idade, telefone, cidade):
        self.salario = 2000
        self.horario = 8
        super().__init__(nome,idade,telefone,cidade,self.salario,self.horario)
class Ajudante(pessoas):
    def __init__(self, nome, idade, telefone, cidade):
        self.salario = 1400
        self.horario = 8
        super().__init__(nome,idade,telefone,cidade,self.salario,self.horario)

def menu():
    print('\n1 - Cadastrar Empregado.')
    print('2 - Ver Lista de Empregados.')
    print('3 - Excluir Empregado.')
    print('4 - Sair do Programa.')
    print(f'\nNúmero de Funcionários cadastrados: {len(funcionarios)}')
    opcao = int(input('\nDigite sua opcão: '))
    while opcao not in (1, 2, 3, 4):
        print('\nOpcao Inválida!')
        opcao = int(input('\nDigite sua Opcão: '))
    return opcao

def cadastro():
    nome = str(input('\nDigite o nome: '))
    while len(nome) > 20:
        print('\nNome muito longo...')
        nome = str(input('\nDigite o nome: '))
    idade = int(input('Digite a idade: '))
    telefone = int(input('Digite o telefone: '))
    cidade = str(input('Digite o cidade: '))
    print('\nEscolha um cargo: ')
    print('\n1 - Propietário.\n2 - Gerente.\n3 - Mecânico.\n4 - Operador.\n5 - Ajudante.')
    profissao = str(input('\nDigite o cargo aqui: ')).strip().upper()[0]
    while profissao not in "12345":
        print('\nProfissão Inexistente!')
        profissao = str(input('Digite o cargo aqui: ')).strip().upper()[0]
    if profissao == "1":
        novo_cadastro = Proprietario(nome,idade,telefone,cidade)
    elif profissao == "2":
        novo_cadastro = Gerente(nome,idade,telefone,cidade)
    elif profissao == "3":
        novo_cadastro = Mecanico(nome,idade,telefone,cidade)
    elif profissao == "4":
        novo_cadastro = Operador(nome,idade,telefone,cidade)
    elif profissao == "5":
        novo_cadastro = Ajudante(nome,idade,telefone,cidade)
    funcionarios.append(novo_cadastro)

def listar_empregados():
    for posicao,pessoa in enumerate(funcionarios):
        print(f'\n{posicao+1}° Funcionário:')
        funcionarios[posicao].mostrar()

def excluir_empregados():
    for posicao,funcionario in enumerate(funcionarios):
        print(f'{posicao + 1} - {funcionario.nome}')
    excluir = int(input('\nDigite o empregado que deseja excuir: '))
    try:
        del funcionarios[excluir - 1]
    except IndexError:
        print('\nFuncionario não existe!')
loop_menu = menu()
while loop_menu < 7 and loop_menu > 0:
    if loop_menu == 1:
        cadastro()
    elif loop_menu == 2:
        listar_empregados()
    elif loop_menu == 3:
        excluir_empregados()
    elif loop_menu == 4:
        break
    loop_menu = menu()