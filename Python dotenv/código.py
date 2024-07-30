'''
    Importação da biblioteca "dotenv" responsável por carregar
        todas variáveis de ambiente dentro do código python.
'''
from dotenv import load_dotenv

'''
    Biblioteca responsável pelas configurações do sistema.
'''
import os

'''
    Aqui estamos carregando as variáveis de ambiente dentro da
        aplicação python.
'''
load_dotenv()

'''
    Aqui estamos fazendo a importação de algumas variáveis de
        ambiente.
'''
print(os.getenv("DB_NAME"))
print(os.getenv("DB_USER"))
print(os.getenv("DB_PASSWORD"))
print(os.getenv("DB_HOST"))
print(os.getenv("DB_PORT"))