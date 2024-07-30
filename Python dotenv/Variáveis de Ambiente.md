# Variáveis de Ambiente

## O que são variáveis de ambiente:  
São espaços na memória que armazenam informações que os programas e 
sistemas operacionais vão utilizar.
Assim é possível mudar o comportamento dos programas sem alterar o
código deles, armazenando informações sensíveis como senhas de maneira
segura; ajustando também rotas se necessário para encontrar executáveis.

___

> Exemplo:  
  set MY_VARIABLE=valor  
  set NOME = Bruno

___
* Configuração de Aplicações: Muitas aplicações e serviços usam variáveis de ambiente para definir parâmetros de configuração, como credenciais de banco de dados, chaves de API e caminhos de diretórios. Isso permite que você altere a configuração sem modificar o código do aplicativo.

* Personalização do Ambiente: Variáveis de ambiente podem ser usadas para definir o comportamento do shell ou terminal. Por exemplo, a variável PATH determina onde o sistema procura executáveis, e a variável HOME aponta para o diretório home do usuário.

* Segurança: Usar variáveis de ambiente para armazenar informações sensíveis (como senhas e tokens) é uma prática comum porque evita a necessidade de incluir essas informações diretamente no código-fonte, que pode ser compartilhado ou versionado.

* Configuração de Sessão: Quando você inicia uma nova sessão de terminal ou um novo processo, variáveis de ambiente específicas para essa sessão podem ser definidas para ajustar o comportamento do ambiente de execução.

O primeiro passo para utilizar a biblioteca é importar ela no Ambiente Virtual da sua aplicação usando o pip:
```python
pip install python-dotenv
```
Agora precisamos criar um arquivo ".env" que será o responsável por armazenar os dados sensíveis que não serão apresentados dentro do projeto.  
Abaixo estamos fazemos a configuração de um Banco de Dados MySQL como exemplo:

``` .env
DB_NAME=nome_do_banco_de_dados
DB_USER=nome_do_usuaro_do_banco_de_dados
DB_PASSWORD=senha_do_banco_de_dados
DB_HOST=nome_do_host
DB_PORT=numero_da_porta
```

Agora na nossa aplicação faremos as seguintes configurações:

```python
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
```

E obteremos o seguinte resultado:

```plaintext
nome_do_banco_de_dados
nome_do_usuaro_do_banco_de_dados
senha_do_banco_de_dados
nome_do_host
```

No arquivo "env" também podemos importar variáveis dentro variáveis basta usarmos as seguintes configurações:

```.env
NOME = Bruno
IDADE = 25
NOME_IDADE = ${NAME} tem ${IDADE} anos.
```
O resultado será:
```plaintext
Bruno tem 25 anos.
```

**Aviso importante:**  
O arquivo ".env" deve ser inclúido no arquivo ".gitignore", pois é neste que seus dados estaram visíveis.
