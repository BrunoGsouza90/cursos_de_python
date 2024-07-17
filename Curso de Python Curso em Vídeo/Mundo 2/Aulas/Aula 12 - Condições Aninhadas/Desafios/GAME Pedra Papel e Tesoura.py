import emoji,pygame,random,time

print('''
\033[1:32:40m                                         {}Digite a música que deseja{}                                                                 \033[m
\033[1:32:40m                                                                                                                                         \033[m
\033[0::40m                                          \033[m\033[4:31:40m1\033[m\033[::40m - \033[m\033[1:33:40mJulia Vitoria - De Dentro Pra Fora.                                                         \033[m
\033[0::40m                                          \033[m\033[4:31:40m2\033[m\033[::40m - \033[m\033[1:33:40mHeloisa Rosa - Há um Lugar.                                                                 \033[m
\033[0::40m                                          \033[m\033[4:31:40m4\033[m\033[::40m - \033[m\033[1:33:40mNelsinho Correa - Sacramento da Comunhão.                                                   \033[m
\033[0::40m                                          \033[m\033[4:31:40m5\033[m\033[::40m - \033[m\033[1:33:40mAdriana Arydes - Lindo Céu.                                                                 \033[m
\033[0::40m                                          \033[m\033[4:31:40m6\033[m\033[::40m - \033[m\033[1:33:40mMORADA - É Tudo Sobre Você.                                                                 \033[m
\033[0::40m                                          \033[m\033[4:31:40m0\033[m\033[0::40m -\033[m\033[1:33:40m Não Tocar Nada.                                                                                             \033[m
\033[1:32:40m                                                                                                                                         \033[m                                        
\033[0::40m                                               \033[m\033[1:31:40m{}Bom Jogo{}\033[m\033[0::40m                                                               \033[m'''.format(emoji.emojize('\U0001f3b5\U0001f3b5\U0001f3b5',language='pt'),emoji.emojize('\U0001f3b5\U0001f3b5\U0001f3b5',language='pt'),emoji.emojize('\U0001f3ae\U0001f3ae\U0001f3ae',language='pt'),emoji.emojize('\U0001f3ae\U0001f3ae\U0001f3ae',language='pt')))
print('\033[0::40m                                                                                                                                                                                        \033[m')
musica = int(input('\033[1:34mDigite a opção que deseja:\033[m '))

if musica >= 1:
    print('\n\033[1:35mPROCESSANDO O LOUVOR!\nAGUARDE... {}\033[m\n'.format(emoji.emojize('\u270B\u270B\u270B',language='pt')))
    time.sleep(2)
    if musica == 1:
        pygame.init()
        pygame.mixer_music.load('Julia Vitoria - De Dentro Pra Fora.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
    elif musica == 2:
        pygame.init()
        pygame.mixer_music.load('Heloisa Rosa - Há um Lugar.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
    elif musica == 3:
        pygame.init()
        pygame.mixer_music.load('Maria Marçal - Deserto.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
    elif musica == 4:
        pygame.init()
        pygame.mixer_music.load('Sacramento da Comunhão - Diácono Nelsinho Corrêa.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
    elif musica == 5:
        pygame.init()
        pygame.mixer_music.load('Lindo céu.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
    elif musica == 6:
        pygame.init()
        pygame.mixer_music.load('É tudo sobre você.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
    else:
        print('Nenhuma música foi encontrada! Nada será reproduzido!\nPara tentar tocar algo rode o progama novamente!')
else:
    print('Nenhuma música serra reproduzida!')

print('\n\033[1:36:40m=-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-Bem-vindo ao Jogo de Pedra, Papel e Tesoura-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-=\033[m')
print('                                                             {}'.format(emoji.emojize('\u270C\uFE0F\u270B\U0001f44a',language='pt')))
print('                                             Criado por: \033[4:31mBruno Gonçalves de Souza\033[m\033[31m.\033[m')
print('\n                                               Com quantos jogadores deseja jogar?')
print('                                                          {}'.format(emoji.emojize('\U0001f93e\u200D\u2642\uFE0F\U0001f93e\u200D\u2642\uFE0F\U0001f93e\u200D\u2642\uFE0F\U0001f93e\u200D\u2642\uFE0F',language='pt')))
print('                                                       \033[4:31:40m1\033[1::40m - \033[1:33:40mSinglePlayer\033[m\n'
      '                                                       \033[4:31:40m2\033[m\033[1::40m - \033[m\033[1:33:40mMultiplayer \033[m')
quantidade_jogadores = (int(input('                                                       \033[1:34:40m  Digite aqui:\033[m ')))
if quantidade_jogadores == 1:
    nome = str(input('\n\033[1:34mDigite o seu nome jogador {}: \033[m'.format(emoji.emojize('\U0001f601',language='pt')))).strip().title()
    print('\033[1:31mÉ um prazer {}\033[m\033[34m!\033[m'.format(nome))
    escolha_computador = ['PEDRA','PAPEL','TESOURA']
    escolha_computador = random.choice(escolha_computador)
    escolha_jogador = str(input('''
\033[1:31mEscolha sua opção...\033[m
 
\033[1:31:40mPara "Tesoura" digite {}:\033[m\033[1:34:40m TESOURA !\033[m
\033[1:31:40mPara "Papel" digite {}:\033[m\033[1:34:40m PAPEL !\033[m
\033[1:31:40mPara "Pedra" digite {}:\033[m\033[1:34:40m PEDRA !\033[m
\033[1:31:40mDigite aqui: \033[m'''.format(emoji.emojize('\u270C\uFE0F',language='pt'),emoji.emojize('\u270B',language='pt'),emoji.emojize('\U0001f44a',language='pt')))).strip().upper()
    print('\033[1:35m\nPROCESSANDO...\n\033[m')
    time.sleep(2)
    print('       \033[1:32:40m{}JO{}\033[m'.format(emoji.emojize('\u270C\uFE0F\u270C\uFE0F\u270C\uFE0F',language='pt'),emoji.emojize('\u270C\uFE0F\u270C\uFE0F\u270C\uFE0F',language='pt')))
    time.sleep(1)
    print('     \033[1:32:40m{}KEN{}\033[m'.format(emoji.emojize('\u270B\u270B\u270B',language='pt'),emoji.emojize('\u270B\u270B\u270B',language='pt')))
    time.sleep(1)
    print('     \033[1:32:40m{}PO{}\033[m\n'.format(emoji.emojize('\U0001f44a\U0001f44a\U0001f44a',language='pt'),emoji.emojize('\U0001f44a\U0001f44a\U0001f44a',language='pt')))
    time.sleep(1)
    if escolha_jogador == 'TESOURA':
        if escolha_computador == 'TESOURA':
            print('\033[1:33m{}Houve Impate!{}\033[m'.format(emoji.emojize('\U0001f971\U0001f971\U0001f971',language='pt'),emoji.emojize('\U0001f971\U0001f971\U0001f971',language='pt')))
        elif escolha_computador == 'PAPEL':
            print('\033[1:32m{}Você ganhou!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6',language='pt'),emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6',language='pt')))
        else:
            print('\033[1:32m{}Você perdeu!{}\033[m'.format(emoji.emojize('\U0001f616\U0001f616\U0001f616',language='pt'),emoji.emojize('\U0001f616\U0001f616\U0001f616',language='pt')))
        print('\nCOMPUTADOR = \033[1:34m{}!\033[m\nJOGADOR = \033[1:34m{}!\033[m'.format(escolha_computador,escolha_jogador))
    elif escolha_jogador == 'PAPEL':
        if escolha_computador == 'PAPEL':
            print('\033[1:33m{}Houve Impate!{}\033[m'.format(emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt'),emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt')))
        elif escolha_computador == 'PEDRA':
            print('\033[1:32m{}Você ganhou!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6',language='pt'),emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6',language='pt')))
        else:
            print('\033[1:32m{}Você perdeu!{}\033[m'.format(emoji.emojize('\U0001f616\U0001f616\U0001f616',language='pt'),emoji.emojize('\U0001f616\U0001f616\U0001f616',language='pt')))
        print('\nCOMPUTADOR = \033[1:34m{}!\033[m\nJOGADOR = \033[1:34m{}!\033[m'.format(escolha_computador,escolha_jogador))
    elif escolha_jogador == 'PEDRA':
        if escolha_computador == 'PEDRA':
            print('\033[1:33m{}Houve Impate!{}\033[m'.format(emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt'),emoji.emojize('\U0001f971\U0001f971\U0001f971',language='pt')))
        elif escolha_computador == 'TESOURA':
            print('\033[1:32m{}Você ganhou!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'),emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
        else:
            print('\033[1:32m{}Você perdeu!{}\033[m'.format(emoji.emojize('\U0001f616\U0001f616\U0001f616', language='pt'),emoji.emojize('\U0001f616\U0001f616\U0001f616', language='pt')))
        print('\nCOMPUTADOR = \033[1:34m{}!\033[m\nJOGADOR = \033[1:34m{}!\033[m'.format(escolha_computador,escolha_jogador))
    else:
        print('{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C',language='pt'),emoji.emojize('\u274C\u274C\u274C',language='pt')))
elif quantidade_jogadores == 2:
    nome1 = str(input('\n\033[1:34mDigite o seu nome Jogador 1 {}: \033[m'.format(emoji.emojize('\U0001f601', language='pt')))).strip().title()
    print('\033[1:31mÉ um prazer {}\033[m\033[34m!\033[m'.format(nome1))
    nome2 = str(input('\033[1:34mDigite o seu nome Jogador 2 {}: \033[m'.format(emoji.emojize('\U0001f601', language='pt')))).strip().title()
    print('\033[1:31mÉ um prazer {}\033[m\033[34m!\033[m'.format(nome2))

    sim_nao = str(input('''
\033[1:33:40mNesse Jogo teremos algumas regras: {}\033[m
\033[1:34:40mRegra 1:\033[m\033[31:40m Enquanto o jogador estiver digitando o outro precisa fechar seus olhos!\033[m
\033[1:34:40mRegra 2:\033[m\033[31:40m Sem brigas! Isso é uma brincadeira não faça apostas!\033[m
\033[1:34:40mRegra 3:\033[m\033[31:40m Não joguem o dia inteiro! Por mais que o jogo seja espetacular...\033[m\033[1:32:40m Ass: Bruno!{}\033[m
\033[1:34:40mVamos lá {}?\033[m '''.format(emoji.emojize('\U0001f973', language='pt'),emoji.emojize('\U0001f92d\U0001f92d\U0001f92d',language='pt'),emoji.emojize('\U0001f44f', language='pt')))).strip().title()
    if sim_nao == 'Sim':
        print('\n\033[1:35mPROCESSANDO O JOGO!\nAGUARDE... {}\033[m\n'.format(emoji.emojize('\u270B\u270B\u270B', language='pt')))
        time.sleep(2)
        quem_comeca = random.randint(1,2)
        if quem_comeca == 1:
            print('\033[1:34mVamos começar por você {} {}! \033[m'.format(nome1, emoji.emojize('\U0001f917', language='pt')))
            escolha_jogador1 = str(input('''\033[1:34mEscolha sua opção {}...\033[m

\033[1:31:40mPara "Tesoura" digite {}:\033[m\033[1:34:40m TESOURA !\033[m
\033[1:31:40mPara "Papel" digite {}:\033[m\033[1:34:40m PAPEL !\033[m
\033[1:31:40mPara "Pedra" digite {}:\033[m\033[1:34:40m PEDRA !\033[m
\033[1:31:40mDigite aqui: \033[m'''.format(nome1,emoji.emojize('\u270C\uFE0F', language='pt'),emoji.emojize('\u270B', language='pt'),emoji.emojize('\U0001f44a', language='pt')))).strip().upper()
            print('''
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            ''')
            print('\n\033[1:34mSua vez {} {}! \033[m'.format(nome2,emoji.emojize('\U0001f917', language='pt')))
            escolha_jogador2 = str(input('''\033[1:34mEscolha sua opção {}...\033[m

\033[1:31:40mPara "Tesoura" digite {}:\033[m\033[1:34:40m TESOURA !\033[m
\033[1:31:40mPara "Papel" digite {}:\033[m\033[1:34:40m PAPEL !\033[m
\033[1:31:40mPara "Pedra" digite {}:\033[m\033[1:34:40m PEDRA !\033[m
\033[1:31:40mDigite aqui: \033[m'''.format(nome2, emoji.emojize('\u270C\uFE0F', language='pt'),emoji.emojize('\u270B', language='pt'),emoji.emojize('\U0001f44a', language='pt')))).strip().upper()
            print('\033[1:35m\nPROCESSANDO...\n\033[m')
            time.sleep(2)
            print('       \033[1:32:40m{}JO{}\033[m'.format(emoji.emojize('\u270C\uFE0F\u270C\uFE0F\u270C\uFE0F', language='pt'),emoji.emojize('\u270C\uFE0F\u270C\uFE0F\u270C\uFE0F', language='pt')))
            time.sleep(1)
            print('     \033[1:32:40m{}KEN{}\033[m'.format(emoji.emojize('\u270B\u270B\u270B', language='pt'),emoji.emojize('\u270B\u270B\u270B', language='pt')))
            time.sleep(1)
            print('     \033[1:32:40m{}PO{}\033[m\n'.format(emoji.emojize('\U0001f44a\U0001f44a\U0001f44a', language='pt'),emoji.emojize('\U0001f44a\U0001f44a\U0001f44a', language='pt')))
            time.sleep(1)
            if escolha_jogador1 == 'TESOURA':
                if escolha_jogador2 == 'TESOURA':
                    print('\033[1:33m{}Houve Impate!{}\033[m'.format(emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt'),emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt')))
                elif escolha_jogador2 == 'PAPEL':
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'),nome1,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                else:
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'),nome2,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                print('\n{} = \033[1:34m{}!\033[m\n{} = \033[1:34m{}!\033[m'.format(nome1,escolha_jogador1,nome2,escolha_jogador2))
            elif escolha_jogador1 == 'PAPEL':
                if escolha_jogador2 == 'PAPEL':
                    print('\033[1:33m{}Houve Impate!{}\033[m'.format(emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt'),emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt')))
                elif escolha_jogador2 == 'PEDRA':
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'),nome1,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                else:
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'),nome2,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                print('\n{} = \033[1:34m{}!\033[m\n{} = \033[1:34m{}!\033[m'.format(nome1,escolha_jogador1,nome2,escolha_jogador2))
            elif escolha_jogador1 == 'PEDRA':
                if escolha_jogador2 == 'PEDRA':
                    print('\033[1:33m{}Houve Impate!{}\033[m'.format(emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt'),emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt')))
                elif escolha_jogador2 == 'TESOURA':
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'),nome1,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                else:
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'),nome2,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                print('\n{} = \033[1:34m{}!\033[m\n{} = \033[1:34m{}!\033[m'.format(nome1,escolha_jogador1,nome2,escolha_jogador2))
            else:
                print('{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
        elif quem_comeca == 2:
            print('\033[1:34mVamos começar por você {} {}! \033[m'.format(nome2,emoji.emojize('\U0001f917', language='pt')))
            escolha_jogador2 = str(input('''\033[1:34mEscolha sua opção {}...\033[m

\033[1:31:40mPara "Tesoura" digite {}:\033[m\033[1:34:40m TESOURA !\033[m
\033[1:31:40mPara "Papel" digite {}:\033[m\033[1:34:40m PAPEL !\033[m
\033[1:31:40mPara "Pedra" digite {}:\033[m\033[1:34:40m PEDRA !\033[m
\033[1:31:40mDigite aqui: \033[m'''.format(nome2, emoji.emojize('\u270C\uFE0F', language='pt'),emoji.emojize('\u270B', language='pt'),emoji.emojize('\U0001f44a', language='pt')))).strip().upper()
            print('''
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            ''')
            print('\n\033[1:34mSua vez {} {}! \033[m'.format(nome1, emoji.emojize('\U0001f917', language='pt')))
            escolha_jogador1 = str(input('''\033[1:34mEscolha sua opção {}...\033[m

\033[1:31:40mPara "Tesoura" digite {}:\033[m\033[1:34:40m TESOURA !\033[m
\033[1:31:40mPara "Papel" digite {}:\033[m\033[1:34:40m PAPEL !\033[m
\033[1:31:40mPara "Pedra" digite {}:\033[m\033[1:34:40m PEDRA !\033[m
\033[1:31:40mDigite aqui: \033[m'''.format(nome1, emoji.emojize('\u270C\uFE0F', language='pt'),emoji.emojize('\u270B', language='pt'),emoji.emojize('\U0001f44a', language='pt')))).strip().upper()
            print('\033[1:35m\nPROCESSANDO...\n\033[m')
            time.sleep(2)
            print('       \033[1:32:40m{}JO{}\033[m'.format(emoji.emojize('\u270C\uFE0F\u270C\uFE0F\u270C\uFE0F', language='pt'),emoji.emojize('\u270C\uFE0F\u270C\uFE0F\u270C\uFE0F', language='pt')))
            time.sleep(1)
            print('     \033[1:32:40m{}KEN{}\033[m'.format(emoji.emojize('\u270B\u270B\u270B', language='pt'),emoji.emojize('\u270B\u270B\u270B', language='pt')))
            time.sleep(1)
            print('     \033[1:32:40m{}PO{}\033[m\n'.format(emoji.emojize('\U0001f44a\U0001f44a\U0001f44a', language='pt'),emoji.emojize('\U0001f44a\U0001f44a\U0001f44a', language='pt')))
            time.sleep(1)
            if escolha_jogador2 == 'TESOURA':
                if escolha_jogador1 == 'TESOURA':
                    print('\033[1:33m{}Houve Impate!{}\033[m'.format(emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt'),emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt')))
                elif escolha_jogador1 == 'PAPEL':
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'), nome2,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                else:
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'), nome1,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                print('\n{} = \033[1:34m{}!\033[m\n{} = \033[1:34m{}!\033[m'.format(nome2, escolha_jogador2, nome1,escolha_jogador1))
            elif escolha_jogador2 == 'PAPEL':
                if escolha_jogador1 == 'PAPEL':
                    print('\033[1:33m{}Houve Impate!{}\033[m'.format(emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt'),emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt')))
                elif escolha_jogador1 == 'PEDRA':
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'), nome2,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                else:
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'), nome1,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                print('\n{} = \033[1:34m{}!\033[m\n{} = \033[1:34m{}!\033[m'.format(nome2, escolha_jogador2, nome1,escolha_jogador1))
            elif escolha_jogador2 == 'PEDRA':
                if escolha_jogador1 == 'PEDRA':
                    print('\033[1:33m{}Houve Impate!{}\033[m'.format(emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt'),emoji.emojize('\U0001f971\U0001f971\U0001f971', language='pt')))
                elif escolha_jogador1 == 'TESOURA':
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'), nome2,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                else:
                    print('\033[1:32m{}Você ganhou {}!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'), nome1,emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                print('\n{} = \033[1:34m{}!\033[m\n{} = \033[1:34m{}!\033[m'.format(nome2, escolha_jogador2, nome1,escolha_jogador1))
            else:
                print('{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
    elif sim_nao == 'Não':
        print('\n\033[1:31mQuem sabe na próxima! \033[m\n\033[1:33mCaso deseje rode o progama novamente e jogue com 1 Jogador apenas! {}\033[m'.format(emoji.emojize('\U0001f947',language='pt')))
    else:
        print('{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
else:
    print('{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
input('\n\033[1:34mDigite "sair" para sair: \033[m')