import emoji,pygame,random,time

print('''
Digite a música que deseja...

1 - É tudo sobre você.
2 - Sacramento da comunhão.
3 - Lindo céu.

Obs.: Para não tocar nada digite "0" !
Bom Jogo!!! {} '''.format(emoji.emojize('\U0001f3ae',language='pt')))

musica = int(input('\nDigite a opção que deseja: '))

if musica >= 1:
    print('\nPROCESSANDO O LOUVOR!\nAGUARDE... {}\n'.format(emoji.emojize('\u270B\u270B\u270B',language='pt')))
    time.sleep(2)
    if musica == 1:
        pygame.init()
        pygame.mixer_music.load('É tudo sobre você.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
    elif musica == 2:
        pygame.init()
        pygame.mixer_music.load('Sacramento da Comunhão - Diácono Nelsinho Corrêa.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
    elif musica == 3:
        pygame.init()
        pygame.mixer_music.load('Lindo céu.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
    else:
        print('Nenhuma música foi encontrada! Nada será reproduzido!\nPara tentar tocar algo rode o progama novamente!')
else:
    print('Nenhuma música serra reproduzida!')

print('\nJogo de Adivinhação v1.0\nCriado por Bruno Gonçalves de Souza')
print('\nVocê pode jogar com... 1 ou 2 Jogadores!')
quantidade_de_jogadores = int(input('Digite a quantidade de jogadores: '))
if quantidade_de_jogadores == 1:
    nome = str(input('Digite seu nome jogador: ')).strip().title()
    print('É um prazer {}! {} '.format(nome,emoji.emojize('\u263A\uFE0F',language='pt')))
    num = random.randint(1,5)
    escolhido = int(input('Digite um número de 1 até 5: '))
    print('\nPROCESSANDO A REPOSTA!\nAGUARDE... {}\n'.format(emoji.emojize('\U0001f440',language='pt')))
    time.sleep(2)
    if escolhido == num:
        print('Você venceu! '+ emoji.emojize('\U0001f4af',language='pt'))
        print('O número sorteado é o {}!'.format(num))
    elif escolhido != num and escolhido > 1 and escolhido < 6:
        print('Você perdeu! ' + emoji.emojize('\U0001f623', language='pt'))
        print('O número sorteado é o {}!'.format(num))
    else:
        print('Você digitou um Número Inválido! {}'.format(emoji.emojize('\u274C',language='pt')))
elif quantidade_de_jogadores == 2:
    print('Vamos lá jogadores {}\n'.format(emoji.emojize('\U0001f93e\u200D\u2642\uFE0F',language='pt')))
    nome = str(input('Digite seu nome Jogador 1: '))
    print('É um prazer {} {}!\n'.format(nome,emoji.emojize('\U0001f91d\U0001f609',language='pt')))
    nome1 = str(input('Digite seu nome Jogador 2: '))
    print('É um prazer {} {}!\n'.format(nome1, emoji.emojize('\U0001f91d\U0001f609', language='pt')))
    sim_nao = str(input('''    Bem vindo ao jogo de Adivinhação 1.0 {}
    Nesse Jogo teremos algumas regras:
    
    Regra 1: Enquanto o jogador estiver digitando o outro precisa fechar seus olhos!
    Regra 2: O jogador que for digitar deve ser bem específico para a adivinhação!
    Regra 3: Sem brigas! Isso é uma brincadeira não faça apostas!
    
    Vamos lá {}? '''.format(emoji.emojize('\U0001f973',language='pt'),emoji.emojize('\U0001f44f',language='pt')))).strip().title()
    if sim_nao == 'Sim':
        print('\nPROCESSANDO O JOGO!\nAGUARDE... {}\n'.format(emoji.emojize('\u270B\u270B\u270B', language='pt')))
        time.sleep(2)
        quem_comeca = random.randint(1,2)
        if quem_comeca == 1:
            print('Vamos começar por você {} {}: '.format(nome,emoji.emojize('\U0001f917',language='pt')))
            adivinhacao = str(input('Digite a adivinhação {}: '.format(nome))).strip().capitalize()
            dica = str(input('Digite a primeira dica {}: '.format(nome))).strip().capitalize()
            dica1 = str(input('Digite a segunda dica {}: '.format(nome))).strip().capitalize()
            dica2 = str(input('Digite a terceira dica {}: '.format(nome))).strip().capitalize()
            resposta = str(input('''
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    


A primeira dica é: {}!
A segunda dica é: {}!
A terceira dica é: {}!

É sua vez {}... Adivinhe {}:  '''.format(dica,dica1,dica2,nome1,emoji.emojize('\U0001f52e',language='pt')))).strip().capitalize()
            print('\nPROCESSANDO A REPOSTA!\nAGUARDE... {}\n'.format(emoji.emojize('\U0001f440', language='pt')))
            time.sleep(2)
            if adivinhacao == resposta:
                print('Você venceu {} {}'.format(nome1,emoji.emojize('\U0001f4af',language='pt')))
            else:
                print('Você perdeu {} {}'.format(nome1,emoji.emojize('\U0001f623',language='pt')))
                print('A Adivinhação é: {}!'.format(adivinhacao))
        else:
            print('Vamos começar por você {} {}'.format(nome1,emoji.emojize('\U0001f917',language='pt')))
            adivinhacao = str(input('Digite a adivinhação {}: '.format(nome1)))
            dica = str(input('Digite a primeira dica {}: '.format(nome1))).strip().capitalize()
            dica1 = str(input('Digite a segunda dica {}: '.format(nome1))).strip().capitalize()
            dica2 = str(input('Digite a terceira dica {}: '.format(nome1))).strip().capitalize()
            resposta = str(input('''
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            



A primeira dica é: {}!
A segunda dica é: {}!
A terceira dica é: {}!       

É sua vez {}... Adivinhe {}: '''.format(dica,dica1,dica2,nome,emoji.emojize('\U0001f52e', language='pt')))).strip().capitalize()
            print('\nPROCESSANDO A REPOSTA!\nAGUARDE... {}\n'.format(emoji.emojize('\U0001f440', language='pt')))
            time.sleep(2)
            if adivinhacao == resposta:
                print('Você venceu {} {}'.format(nome,emoji.emojize('\U0001f4af',language='pt')))
            else:
                print('Você perdeu {} {}'.format(nome,emoji.emojize('\U0001f623',language='pt')))
                print('A Adivinhação é: {}!'.format(adivinhacao))
    elif sim_nao == 'Não':
        print('Quem sabe na próxima! \n Caso deseje rode o progama novamente e jogue com 1 jogador apenas! {}'.format(emoji.emojize('\U0001f947',language='pt')))
    else:
        print('Opção inválida! {}'.format(emoji.emojize('\u274C', language='pt')))
else:
    print('Opção inválida! {}'.format(emoji.emojize('\u274C',language='pt')))
input('\nDigite "sair" para sair: ')