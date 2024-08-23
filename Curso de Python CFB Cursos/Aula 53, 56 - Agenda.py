import os
import sqlite3
from sqlite3 import Error
import time

'''
    Aqui vemos se o usuário quer criar um Banco de Dados ou se ele
        já quer entrar com um existente.
'''

caminho = 'Curso de Python CFB Cursos/Banco de Dados/'

while True:
    resposta = str(input('Você deseja criar um Banco de Dados? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        print('Resposta Inválida!')
        resposta = str(input('Você deseja criar um Banco de Dados? [S/N] ')).strip().upper()[0]
    if resposta == 'S':
        nome_do_banco = str(input('Digite o nome do novo Banco de Dados: ')).lower()
        nome_do_banco = f'{nome_do_banco}.db'
        caminho_completo = os.path.join(caminho, nome_do_banco)
        while os.path.exists(caminho_completo):
            print('Este Banco de Dados já existe!')
            nome_do_banco = str(input('Digite o nome do novo Banco de Dados: ')).lower()
            nome_do_banco = f'{nome_do_banco}.db'
            caminho_completo = os.path.join(caminho, nome_do_banco)
        with open(caminho_completo, 'w') as arquivo:
            print('Banco de Dados criado com sucesso!')

        '''
            Aqui estabelecemos uma conexão com o Banco de Dados.
        '''
        def ConexaoBanco():
            caminho_completo = (caminho + nome_do_banco)
            conexao = None
            try:
                conexao = sqlite3.connect(caminho_completo)
            except Error as ex:
                print('Ocorreu um erro na Criação do Banco de Dados!\n Leia Atentamente!')
                print(ex)
            return conexao

        vcon = ConexaoBanco()
        
        '''
            Aqui estamos criando nossa tabela no Banco de Dados.
        '''
        vsql = """
            CREATE TABLE IF NOT EXISTS contatos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(30) NOT NULL,
                sobrenome VARCHAR(50),
                empresa VARCHAR(50),
                telefone VARCHAR(15),
                celular VARCHAR(15) NOT NULL,
                email VARCHAR(100),
                marcador VARCHAR(30),
                nascimento DATE
            );
        """

        def CriarTabela(conexao, sql):
            try:
                c = conexao.cursor()
                c.execute(sql)
                print('Banco de Dados Configurado com sucesso!')
            except Error as ex:
                print('Erro na configuração do Banco de Dados.\n Leia o Erro atentamente!')
                print(ex)
        
        CriarTabela(vcon, vsql)

        
        break
    
    
    elif resposta == 'N':
        nome_do_banco = str(input('Digite o nome do Banco de Dados já existente: ')).lower()
        nome_do_banco = f'{nome_do_banco}.db'
        caminho_completo = (caminho + nome_do_banco)
        while not os.path.exists(caminho_completo):
            print('Esse Banco de Dados não existe. Tente Novamente!')
            nome_do_banco = str(input('Digite o nome do Banco de Dados já existente: ')).lower()
            nome_do_banco = f'{nome_do_banco}.db'
            caminho_completo = (caminho + nome_do_banco)
        break



'''
    Aqui estamos criando o nosso menu principal da agenda.
'''
def menuPrincipal():
    print(f'\n{'MENU PRINCIPAL'.center(60)}')
    print('-=' * 30)
    print('1 - Inserir Novo Registro')
    print('2 - Deletar Registro')
    print('3 - Atualizar Registro')
    print('4 - Ver Banco de Dados')
    print('5 - Sair')
    print('-=' * 30)
    opcao = int(input('Digite a opção: '))
    while opcao < 1 or opcao > 5:
        print('Opção Inválida! Tente novamente!')
        opcao = int(input('Digite a opção: '))
    return opcao

opcao = menuPrincipal()

while opcao > 0 or opcao < 6:
    if opcao == 1:
        '''
            Aqui estamos inserindo um novo registro no Banco de Dados.
        '''
        print('Inserindo Novo Contato!')
        nome = str(input('Nome: ')).capitalize()
        while len(nome) > 30:
            print('Nome muito longo! Tente Novamente!')
            nome = input('Nome: ').capitalize()
        while len(nome) < 1:
            print('Nome Obrigatório!')
            nome = input('Nome: ').capitalize()
        sobrenome = str(input('Sobrenome: ')).capitalize()
        while len(sobrenome) > 45:
            print('Sobrenome muito longo! Tente Novamente!')
            sobrenome = str(input('Sobrenome: ')).capitalize()
        empresa = str(input('Empresa: ')).capitalize()
        while len(empresa) > 45:
            print('Nome da empresa muito longo! Tente Novamente!')
            empresa = str(input('Empresa: ')).capitalize()
        telefone = str(input('Telefone: '))
        while len(telefone) > 15:
            print('Telefone muito longo! Tente Novamente!')
            telefone = str(input('Telefone: '))
        celular = str(input('Celular: '))
        while len(celular) > 15:
            print('Celular muito longo! Tente Novamente!')
            celular = str(input('Celular: '))
        while len(celular) < 1:
            print('Celular Obrigatório!')
            celular = str(input('Celular: '))
        email = str(input('Email: '))
        while len(email) > 90:
            print('Email muito longo! Tente Novamente!')
            email = str(input('Email: '))
        marcador = ['Parente', 'Cliente', 'Anônimo', 'Empresas', 'Outros']
        print('\nOpções de Marcador: ')
        print('1 - Parente')
        print('2 - Cliente')
        print('3 - Anônimo')
        print('4 - Empresas')
        print('5 - Outros')
        marcador = int(input('Marcador: '))
        while marcador < 1 or marcador > 5:
            print('Opção Inválida!')
            marcador = int(input('Marcador: '))
        if marcador == 1:
            marcador = 'Parente'
        elif marcador == 2:
            marcador = 'Cliente'
        elif marcador == 3:
            marcador = 'Anônimo'
        elif marcador == 4:
            marcador = 'Empresas'
        elif marcador == 5:
            marcador = 'Outros'
        while True:
            resposta = str(input('Deseja digitar a Data de Nascimento? [S/N] ')).strip().upper()
            while resposta not in 'SN':
                print('Opção Inválida!')
                resposta = str(input('Deseja digitar a Data de Nascimento? [S/N] ')).strip().upper()
            if resposta == 'S':
                ano_de_nascimento = int(input('Ano de Nascimento: '))
                ano_de_nascimento = str(ano_de_nascimento)
                while len(ano_de_nascimento) > 4:
                    print('O Ano de Nascimento deve ter 4 dígitos!')
                    ano_de_nascimento = int(input('Ano de Nascimento: '))
                    ano_de_nascimento = str(ano_de_nascimento)
                dia_do_nascimento = int(input('Dia do Nascimento: '))
                dia_do_nascimento = str(dia_do_nascimento)
                while len(dia_do_nascimento) > 2:
                    print('O Dia do Nascimento deve ter no máximo 2 dígitos!')
                    dia_do_nascimento = int(input('Dia do Nascimento: '))
                    dia_do_nascimento = str(dia_do_nascimento)
                if len(dia_do_nascimento) == 1:
                    dia_do_nascimento = f'0{dia_do_nascimento}'
                mes_do_nascimento = int(input('Mês do Nascimento: '))
                mes_do_nascimento = str(mes_do_nascimento)
                if len(mes_do_nascimento) == 1:
                    mes_do_nascimento = f'0{mes_do_nascimento}'
                while len(mes_do_nascimento) > 2:
                    print('O Mês de Nascimento deve ter no máximo 2 dígitos!')
                    mes_do_nascimento = int(input('Mês do Nascimento: '))
                    mes_do_nascimento = str(mes_do_nascimento)
                nascimento = f'{ano_de_nascimento}-{mes_do_nascimento}-{dia_do_nascimento}'
                break
            
            if resposta == 'N':
                nascimento = ''
                break

        def ConexaoBanco():
            caminho_completo = (caminho + nome_do_banco)
            conexao = None
            try:
                conexao = sqlite3.connect(caminho_completo)
            except Error as ex:
                print('Ocorreu um erro na Criação do Banco de Dados!\n Leia Atentamente!')
                print(ex)
            return conexao

        vcon = ConexaoBanco()

        vsql = f"""
            INSERT INTO contatos
            (nome, sobrenome, empresa, telefone, celular, email, marcador, nascimento)
            VALUES
            ('{nome}', '{sobrenome}', '{empresa}', '{telefone}', '{celular}', '{email}', '{marcador}', '{nascimento}')
        """

        def InserirDados(conexao, sql):
            try:
                c = conexao.cursor()
                c.execute(sql)
                conexao.commit()
                print('Contato salvo com sucesso!')
            except Error as ex:
                print('Erro ao Cadastrar o Novo Contato!\n Leia atentamente!')
                print(ex)
        
        InserirDados(vcon, vsql)
        opcao = menuPrincipal()

    elif opcao == 2:
        def ConexaoBanco():
            caminho_completo = (caminho + nome_do_banco)
            conexao = None
            try:
                conexao = sqlite3.connect(caminho_completo)
            except Error as ex:
                print('Erro ao Conectar com o Banco de Dados!\n Leia Atentamente!')
                print(ex)
            return conexao
        
        vcon = ConexaoBanco()
        
        id = int(input('Digite o "ID" do contato que deseja deletar: '))
        
        vsql = f"""
            DELETE FROM contatos
            where id = {id};
        """

        '''
            Aqui estamos deletando um registro do Banco de Dados.
        '''
        def deletarDados(conexao, sql):
            try:
                c = conexao.cursor()
                c.execute(sql)
                conexao.commit()
                print('Registro deletado com sucesso!')
            except Error as ex:
                print('Erro ao deletar o registro!\n Leia Atentamente!')
                print(ex)

        deletarDados(vcon, vsql)
        opcao = menuPrincipal()

    elif opcao == 3:
        def ConexaoBanco():
            caminho_completo = (caminho + nome_do_banco)
            conexao = None
            try:
                conexao = sqlite3.connect(caminho_completo)
            except Error as ex:
                print('Erro na conexão com o Banco de Dados!\n Leia atentamente!')
                print(ex)
            return conexao
        
        vcon = ConexaoBanco()

        id = int(input('\nDigite o "ID" que deseja alterar: '))

        vsql = f"""
            SELECT * FROM contatos
            WHERE id = {id};
        """

        cursor = vcon.cursor()
        cursor.execute(vsql)
        resultado = cursor.fetchone()
        
        while resultado == None:
            print('"ID" Invalido! Tente Novamente!')
            id = int(input('\nDigite o "ID" que deseja alterar: '))
            vsql = f"""
                SELECT * FROM contatos
                WHERE id = {id};
            """

            cursor = vcon.cursor()
            cursor.execute(vsql)
            resultado = cursor.fetchone()
        
        print('')
        print('-=' * 90)
        print(f"{'ID':<15} {'Nome':<15} {'Sobrenome':<15} {'Empresa':<15} {'Telefone':<15} {'Celular':<15} {'Email':<30} {'Marcador':<15} {'Data de Nascimento':<15}")
        print('-=' * 90)
        print(f"{resultado[0]:<15} {resultado[1]:<15} {resultado[2]:<15} {resultado[3]:<15} {resultado[4]:<15} {resultado[5]:<15} {resultado[6]:<30} {resultado[7]:<15} {resultado[8]:<15}")
        print('-=' * 90)
            

        print('\nDados para Alteração: ')
        print('1 - Nome')
        print('2 - Sobrenome')
        print('3 - Empresa')
        print('4 - Telefone')
        print('5 - Celular')
        print('6 - Email')
        print('7 - Marcador')
        print('8 - Data de Nascimento')
        opcao = int(input('Digite a Opção: '))
        while opcao < 1 or opcao > 8:
            print('Opção Inválida!')
            opcao = int(input('Digite a Opção: '))

        if opcao == 1:
            nome = str(input('Digite o novo nome: ')).capitalize()
            while len(nome) > 30:
                print('Nome muito longo! Tente Novamente!')
                nome = str(input('Digite o novo nome: ')).capitalize()
            
            vsql = f"""
                UPDATE contatos
                SET nome = '{nome}'
                WHERE id = {id};
            """
        elif opcao == 2:
            sobrenome = str(input('Digite o novo sobrenome: ')).capitalize()
            while len(sobrenome) > 45:
                print('Sobrenome muito longo! Tente novamente!')
                sobrenome = str(input('Digite o novo sobrenome: ')).capitalize()
            
            vsql = f"""
                UPDATE contatos
                SET sobrenome = '{sobrenome}'
                WHERE id = {id};
            """
        elif opcao == 3:
            empresa = str(input('Digite o novo nome da empresa: ')).capitalize()
            while len(empresa) > 45:
                print('Nome da empresa muito longo! Tente novamente!')
                empresa = str(input('Digite o novo nome da empresa: ')).capitalize()

            vsql = f"""
                UPDATE contatos
                SET empresa = '{empresa}'
                WHERE id = {id};
            """
        elif opcao == 4:
            telefone = str(input('Digite o novo número de telefone: '))
            while len(telefone) > 15:
                print('Telefone muito longo! Tente novamente!')
                telefone = str(input('Digite o novo número de telefone: '))
            vsql = f"""
                UPDATE contatos
                SET telefone = '{telefone}'
                WHERE id = {id};
            """
        elif opcao == 5:
            celular = str(input('Digite o novo número de celular: '))
            while len(celular) > 15:
                print('Número de celular muito longo! Tente novamente!')
                celular = str(input('Digite o novo número de celular: '))
            vsql = f"""
                UPDATE contatos
                SET celular = '{celular}'
                WHERE id = {id};
            """
        elif opcao == 6:
            email = str(input('Digite o novo email: '))
            while len(email) > 95:
                print('Email muito longo! Tente novamente!')
                email = str(input('Digite o novo email: '))
            vsql = f"""
                UPDATE contatos
                SET email = '{email}'
                WHERE id = {id};
            """
        elif opcao == 7:
            marcador = ['Parente', 'Cliente', 'Anônimo', 'Empresas', 'Outros']
            print('\nOpções de Marcador: ')
            print('1 - Parente')
            print('2 - Cliente')
            print('3 - Anônimo')
            print('4 - Empresas')
            print('5 - Outros')
            marcador = int(input('Digite o novo marcador: '))
            while marcador < 1 or marcador > 5:
                print('Opção Inválida!')
                marcador = int(input('Digite o novo marcador: '))
            if marcador == 1:
                marcador = 'Parente'
            elif marcador == 2:
                marcador = 'Cliente'
            elif marcador == 3:
                marcador = 'Anônimo'
            elif marcador == 4:
                marcador = 'Empresas'
            elif marcador == 5:
                marcador = 'Outros'

            vsql = f"""
                UPDATE contatos
                SET marcador = '{marcador}'
                WHERE id = {id};
            """
        else:
            print('Vamos alterar a Data de Nascimento!')
            ano_de_nascimento = int(input('Ano de Nascimento: '))
            ano_de_nascimento = str(ano_de_nascimento)
            while len(ano_de_nascimento) > 4:
                print('O Ano de Nascimento deve ter 4 dígitos!')
                ano_de_nascimento = int(input('Ano de Nascimento: '))
                ano_de_nascimento = str(ano_de_nascimento)
            dia_do_nascimento = int(input('Dia do Nascimento: '))
            dia_do_nascimento = str(dia_do_nascimento)
            while len(dia_do_nascimento) > 2:
                print('O Dia do Nascimento deve ter no máximo 2 dígitos!')
                dia_do_nascimento = int(input('Dia do Nascimento: '))
                dia_do_nascimento = str(dia_do_nascimento)
            if len(dia_do_nascimento) == 1:
                dia_do_nascimento = f'0{dia_do_nascimento}'
            mes_do_nascimento = int(input('Mês do Nascimento: '))
            mes_do_nascimento = str(mes_do_nascimento)
            if len(mes_do_nascimento) == 1:
                mes_do_nascimento = f'0{mes_do_nascimento}'
            while len(mes_do_nascimento) > 2:
                print('O Mês de Nascimento deve ter no máximo 2 dígitos!')
                mes_do_nascimento = int(input('Mês do Nascimento: '))
                mes_do_nascimento = str(mes_do_nascimento)
            nascimento = f'{ano_de_nascimento}-{mes_do_nascimento}-{dia_do_nascimento}'

            vsql = f"""
                UPDATE contatos
                SET email = '{nascimento}'
                WHERE id = {id};
            """

        '''
            Aqui estamos atualizando o registro no Banco de Dados.
        '''
        
        def atualizarDados(conexao, sql):
            try:
                c = conexao.cursor()
                c.execute(sql)
                conexao.commit()
                print('Informações do contato atualizados com sucesso!')
            except Error as ex:
                print('Erro ao atualizar o Banco de Dados!\n Leia atentamente!')
                print(ex)
        
        atualizarDados(vcon, vsql)
        opcao = menuPrincipal()
        
    elif opcao == 4:
        def ConexaoBanco():
            caminho_completo = (caminho + nome_do_banco)
            conexao = None
            try:
                conexao = sqlite3.connect(caminho_completo)
            except Error as ex:
                print('Erro ao conectar com o Banco de Dados!\n Leia atentamente!')
                print(ex)
            return conexao
        
        vcon = ConexaoBanco()

        vsql = """
            SELECT * FROM contatos;
        """

        '''
            Aqui estamos consultando o Banco de Dados.
        '''
        def ConsultarDados(conexao, sql):
            c = conexao.cursor()
            c.execute(sql)
            resultado = c.fetchall()
            return resultado
        
        resultados = ConsultarDados(vcon, vsql)
        print('')
        print('-=' * 90)
        print(f"{'ID':<15} {'Nome':<15} {'Sobrenome':<15} {'Empresa':<15} {'Telefone':<15} {'Celular':<15} {'Email':<30} {'Marcador':<15} {'Data de Nascimento':<15}")
        for resultado in resultados:
            print('-=' * 90)
            print(f"{resultado[0]:<15} {resultado[1]:<15} {resultado[2]:<15} {resultado[3]:<15} {resultado[4]:<15} {resultado[5]:<15} {resultado[6]:<30} {resultado[7]:<15} {resultado[8]:<15}")
        print('-=' * 90)
        print('')
        resultados = []
        opcao = 0
        opcao = menuPrincipal()

    else:
        print('Saindo do Programa...')
        time.sleep(2)
        print('Volte Sempre!')
        print('Programa Finalizado!')
        break
