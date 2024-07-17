import requests

def verifica_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print('Consegui acessar o site google com sucesso!')
    except:
        print('O site do google não está acessível no momento.')

url = 'https://www.google.com.br/'
verifica_url(url)

input('Digite "sair" para sair: ')