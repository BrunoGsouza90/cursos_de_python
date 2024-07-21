resposta = str(input('Quer criar um Banco de Dados? [S/N] ')).strip().upper()[0]
while resposta not in 'SN':
    print('Resposta Inválida!')
    resposta = str(input('Quer criar um Banco de Dados? [S/N] ')).strip().upper()[0]
if resposta == 'S':
    arquivo = str(input('Digite o nome do Banco de Dados: ')).strip().capitalize()
    try:
        f = open("Curso de Python CFB Cursos/Banco de Dados/" + arquivo + '.txt' , 'x')
        print(f'Banco de Dados "{arquivo}" criado com sucesso!')
    except FileExistsError:
        print(f'Banco de Dadps "{arquivo}" já existe!')
else:
    arquivo = str(input('Digite o nome do Banco de Dados: ')).strip().capitalize()


resposta = str(input('Quer adicionar texto ao arquivo? [S/N] ')).strip().upper()[0]
while resposta not in 'SN':
    print('Resposta Inválida!')
    resposta = str(input('Quer adicionar texto ao arquivo? [S/N] ')).strip().upper()[0]
if resposta == 'S':
    f = open("Curso de Python CFB Cursos/Banco de Dados/" + arquivo + '.txt' , 'at')
    texto = str(input('Digite o texto que deseja armazenar: ')).strip()
    f.write(f'\n{texto}')
    f.close()

resposta = str(input('Quer ler o arquivo? [S/N] ')).strip().upper()[0]
while resposta not in 'SN':
    print('Resposta Inválida!')
    resposta = str(input('Quer ler o arquivo? [S/N] ')).strip().upper()[0]
if resposta == 'S':
    f = open("Curso de Python CFB Cursos/Banco de Dados/" + arquivo + '.txt' , 'rt')
    linhas = f.readlines()
    for contador, linha in enumerate(linhas):
        print(f'{contador + 1}ª Linha = {linha}')


# Operações:
# 'r' = read (Leitura). = Faz a leitura do arquivo.
# 'a' = append (Anexar ou Adicionar) = Adiciona contéudo ao arquivo.
# 'w' = write (Escrita) = Troca todo o contéudo do arquivo por algo novo.
# 'x' = create (Criar). = Cria um novo arquivo.

# Modos:
# 't' = texto. = Acompanham as operações. São arquivos do tipo texto.
# 'b' = binário. = Acompanham as operações. São arquivos do tipo binário.

# Comandos:
# VARIÁVEL.write('') = Texto a ser armazenado.
# VARIÁVEL.close() = Fechar o arquivo.