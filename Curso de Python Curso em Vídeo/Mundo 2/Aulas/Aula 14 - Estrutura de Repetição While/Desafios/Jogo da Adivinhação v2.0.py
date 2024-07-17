import emoji, pygame, random, time

nova_tentativa = 'Sim'
while nova_tentativa == 'Sim':
    print('''
\033[1:32:40m                                         {}Digite a música que deseja{}                                                                 \033[m
\033[1:32:40m                                                                                                                                         \033[m
\033[0::40m                                          \033[m\033[4:31:40m1\033[m\033[::40m - \033[m\033[1:33:40mJulia Vitoria - De Dentro Pra Fora.                                                         \033[m
\033[0::40m                                          \033[m\033[4:31:40m2\033[m\033[::40m - \033[m\033[1:33:40mHeloisa Rosa - Há um Lugar.                                                                 \033[m
\033[0::40m                                          \033[m\033[4:31:40m3\033[m\033[::40m - \033[m\033[1:33:40mMaria Marçal - Deserto.                                                                 \033[m
\033[0::40m                                          \033[m\033[4:31:40m4\033[m\033[::40m - \033[m\033[1:33:40mNelsinho Correa - Sacramento da Comunhão.                                                   \033[m
\033[0::40m                                          \033[m\033[4:31:40m5\033[m\033[::40m - \033[m\033[1:33:40mAdriana Arydes - Lindo Céu.                                                                 \033[m
\033[0::40m                                          \033[m\033[4:31:40m6\033[m\033[::40m - \033[m\033[1:33:40mMORADA - É Tudo Sobre Você.                                                                 \033[m
\033[0::40m                                          \033[m\033[4:31:40m0\033[m\033[0::40m -\033[m\033[1:33:40m Não Tocar Nada.                                                                                             \033[m
\033[1:32:40m                                                                                                                                         \033[m                                        
\033[0::40m                                               \033[m\033[1:31:40m{}Bom Jogo{}\033[m\033[0::40m                                                               \033[m'''.format(emoji.emojize('\U0001f3b5\U0001f3b5\U0001f3b5',language='pt'),emoji.emojize('\U0001f3b5\U0001f3b5\U0001f3b5',language='pt'),emoji.emojize('\U0001f3ae\U0001f3ae\U0001f3ae',language='pt'),emoji.emojize('\U0001f3ae\U0001f3ae\U0001f3ae',language='pt')))
    print('\033[0::40m                                                                                                                                                                                        \033[m')
    musica = int(input('\033[1:34mDigite a opção que deseja:\033[m '))

    print('\n\033[1:35mPROCESSANDO O LOUVOR!\nAGUARDE... {}\033[m\n'.format(emoji.emojize('\u270B\u270B\u270B',language='pt')))
    time.sleep(2)
    if musica == 1:
        pygame.init()
        pygame.mixer_music.load('Julia Vitoria - De Dentro Pra Fora.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
        nova_tentativa = 'Não'
    elif musica == 2:
        pygame.init()
        pygame.mixer_music.load('Heloisa Rosa - Há um Lugar.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
        nova_tentativa = 'Não'
    elif musica == 3:
        pygame.init()
        pygame.mixer_music.load('Maria Marçal - Deserto.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
        nova_tentativa = 'Não'
    elif musica == 4:
        pygame.init()
        pygame.mixer_music.load('Sacramento da Comunhão - Diácono Nelsinho Corrêa.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
        nova_tentativa = 'Não'
    elif musica == 5:
        pygame.init()
        pygame.mixer_music.load('Lindo céu.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
        nova_tentativa = 'Não'
    elif musica == 6:
        pygame.init()
        pygame.mixer_music.load('É tudo sobre você.mp3')
        pygame.mixer_music.play()
        pygame.event.wait()
        nova_tentativa = 'Não'
    elif musica == 0:
        print('\033[1:31mNenhuma música será reproduzida!\033[m')
        nova_tentativa = 'Não'
    else:
        print('\033[1:31mNenhuma música foi encontrada!\033[m')
        print('\033[1:32mQuer tentar escolher uma música novamente?\033[m')
        nova_tentativa = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
        while nova_tentativa != 'Sim' and nova_tentativa != 'Não':
            print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
            print('\n\033[1:31mDigite\033[m \033[1:33m"Sim"\033[m \033[1:31mou\033[m \033[1:33m"Não"\033[m\033[1:31m!\033[m')
            nova_tentativa = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
        if nova_tentativa == 'Não':
            print('\n\033[1:31mNenhuma música será reproduzida!\033[m')
print('\n\033[1:36:40m=-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-Bem-vindo ao Jogo de Adivinhação v2.0-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-==-=-=-=-=\033[m')
print('                                                             {}'.format(emoji.emojize('\U0001f3b5\U0001f441\uFE0F\U0001f422\U0001f9d0',language='pt')))
print('                                             Criado por: \033[4:31mBruno Gonçalves de Souza\033[m\033[31m.\033[m')
print('\n                                               Com quantos jogadores deseja jogar?')
print('                                                          {}'.format(emoji.emojize('\U0001f93e\u200D\u2642\uFE0F\U0001f93e\u200D\u2642\uFE0F\U0001f93e\u200D\u2642\uFE0F\U0001f93e\u200D\u2642\uFE0F',language='pt')))
print('                                                       \033[4:31:40m1\033[1::40m - \033[1:33:40mSinglePlayer\033[m\n'
      '                                                       \033[4:31:40m2\033[m\033[1::40m - \033[m\033[1:33:40mMultiplayer \033[m')
quantidade_de_jogadores = (int(input('                                                       \033[1:34:40m  Digite aqui:\033[m ')))
while quantidade_de_jogadores != 1 and quantidade_de_jogadores != 2:
    print('\n                                                 {}\033[7::40mOpção Inválida!\033[m{}\n'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
    print('                                                          {}'.format(emoji.emojize('\U0001f93e\u200D\u2642\uFE0F\U0001f93e\u200D\u2642\uFE0F\U0001f93e\u200D\u2642\uFE0F\U0001f93e\u200D\u2642\uFE0F',language='pt')))
    print('                                                       \033[4:31:40m1\033[1::40m - \033[1:33:40mSinglePlayer\033[m\n''                                                       \033[4:31:40m2\033[m\033[1::40m - \033[m\033[1:33:40mMultiplayer \033[m')
    quantidade_de_jogadores = (int(input('                                                       \033[1:34:40m  Digite aqui:\033[m ')))
if quantidade_de_jogadores == 1:
    continuar_jogando = 'Sim'
    nome = str(input('\n\033[1:34mDigite o Seu Nome Jogador {}: \033[m'.format(emoji.emojize('\U0001f601', language='pt')))).strip().title()
    print('\033[1:31mÉ um prazer {}\033[m\033[34m!\033[m'.format(nome))
    while continuar_jogando == 'Sim':
        num = random.randint(1, 10)
        escolhido = 0
        tentativa = 1
        while num != escolhido:
            print('\n','\033[1:31:40m=-' * 27, '\033[m\033[1:33:40m{}º Tentativa\033[m\033[1:31:40m'.format(tentativa), '-=' * 29,'\033[m')
            escolhido = int(input('\n\033[1:34mDigite um Número de 1 até 10:\033[m '))
            print('\033[1:35m\nPROCESSANDO...\n\033[m')
            time.sleep(2)
            if escolhido == num:
                print('\033[1:32m{}Você Ganhou!{}\033[m'.format(emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt'),emoji.emojize('\U0001f3c6\U0001f3c6\U0001f3c6', language='pt')))
                print('O número Sorteado é o {}!'.format(num))
            elif escolhido != num and escolhido >= 1 and escolhido <= 10:
                print('\033[1:32m{}Você Perdeu!{}\033[m'.format(emoji.emojize('\U0001f616\U0001f616\U0001f616', language='pt'),emoji.emojize('\U0001f616\U0001f616\U0001f616', language='pt')))
                if escolhido < num:
                    print('    {}\033[1:31mMais{}\033[m'.format(emoji.emojize('\U0001f9d0\U0001f9d0\U0001f9d0',language='pt'),emoji.emojize('\U0001f9d0\U0001f9d0\U0001f9d0',language='pt')))
                else:
                    print('    {}\033[1:31mMenos{}\033[m'.format(emoji.emojize('\U0001f9d0\U0001f9d0\U0001f9d0', language='pt'),emoji.emojize('\U0001f9d0\U0001f9d0\U0001f9d0', language='pt')))
            else:
                print('{}\033[7::40mVocê Digitou um Número Inválido!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
            tentativa += 1
        print('\n\033[1:31mO número Sorteado é o\033[m \033[1:33m{}\033[m\033[1:31m!\033[m'.format(num))
        print('\033[1:31mVocê Acertou na\033[m \033[1:33m{}º\033[m \033[1:31mTentativa!\033[m'.format(tentativa-1))
        print('\n\033[1:36:40mVocê Deseja Continuar Jogando?\033[m')
        continuar_jogando = str(input('\n\033[1:34mSim / Não :\033[m ')).strip().title()
        while continuar_jogando != 'Sim' and continuar_jogando != 'Não':
            print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'), emoji.emojize('\u274C\u274C\u274C', language='pt')))
            continuar_jogando = str(input('\n\033[1:34mSim / Não :\033[m ')).strip().title()
        if continuar_jogando == 'Não':
            print('\n\033[1:32mVocê tem certeza?\033[m\n\033[1:31mDigite\033[m \033[1:33m"Sim"\033[m \033[1:31mou\033[m \033[1:33m"Não"\033[m\033[1:31m!\033[m')
            continuar_jogando= str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
            while continuar_jogando != 'Sim' and continuar_jogando != 'Não':
                print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
                print('\n\033[1:32mVocê tem certeza?\033[m\n\033[1:31mDigite\033[m \033[1:33m"Sim"\033[m \033[1:31mou\033[m \033[1:33m"Não"\033[m\033[1:31m!\033[m')
                continuar_jogando = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
            if continuar_jogando == 'Sim':
                continuar_jogando = 'Sair'
            elif continuar_jogando == 'Não':
                print('\n\033[1:33mJá que não tem certeza... Que tal jogar novamente?\033[m')
                print('\033[1:32mQuer jogar novamente?\033[m')
                continuar_jogando = str(input('\033[1:34mSim / Não:\033[m ')).strip().title()
                while continuar_jogando != 'Sim' and jogar_novamente != 'Não':
                    print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
                    print('\033[1:32mQuer jogar novamente?\033[m')
                    continuar_jogando = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
                if continuar_jogando == 'Não':
                    continuar_jogando = 'sair'





elif quantidade_de_jogadores == 2:
    nome = str(input('\n\033[1:34mDigite o seu nome Jogador 1 {}: \033[m'.format(emoji.emojize('\U0001f601', language='pt')))).strip().title()
    print('\033[1:31mÉ um prazer {}\033[m\033[34m!\033[m'.format(nome))
    nome1 = str(input('\n\033[1:34mDigite o seu nome Jogador 2 {}: \033[m'.format(emoji.emojize('\U0001f601', language='pt')))).strip().title()
    print('\033[1:31mÉ um prazer {}\033[m\033[34m!\033[m'.format(nome1))

    print('''
    \033[1:33:40mNesse Jogo teremos algumas regras: {}\033[m
    \033[1:34:40mRegra 1:\033[m\033[31:40m Enquanto o jogador estiver digitando o outro precisa fechar seus olhos!\033[m
    \033[1:34:40mRegra 2:\033[m\033[31:40m O jogador que for digitar deve ser bem específico para a adivinhação!\033[m
    \033[1:34:40mRegra 3:\033[m\033[31:40m Sem brigas! Isso é uma brincadeira não faça apostas!\033[m
    \033[1:34:40mRegra 4:\033[m\033[31:40m Não joguem o dia inteiro! Por mais que o jogo seja espetacular...\033[m\033[1:32:40m Ass: Bruno!{}\033[m
    \033[1:34:40mVamos lá {}?\033[m '''.format(emoji.emojize('\U0001f973', language='pt'),emoji.emojize('\U0001f92d\U0001f92d\U0001f92d', language='pt'),emoji.emojize('\U0001f44f', language='pt')))

    print('\n\033[1:31mDigite\033[m \033[1:33m"Sim"\033[m \033[1:31mou\033[m \033[1:33m"Não"\033[m\033[1:31m!\033[m')
    jogar_novamente = str(input('\n\033[1:34mDigite... Sim / Não:\033[m ')).strip().title()
    while jogar_novamente != 'Sim' and jogar_novamente != 'Não':
        print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
        print('\n\033[1:31mVocê concorda com as regras e quer jogar?\033[m')
        jogar_novamente = str(input('\033[1:34mDigite... Sim / Não:\033[m ')).strip().title()
    while jogar_novamente == 'Sim' or jogar_novamente == 'Não':
        if jogar_novamente == 'Sim':
            print('\n\033[1:35mPROCESSANDO O JOGO!\nAGUARDE... {}\033[m\n'.format(emoji.emojize('\u270B\u270B\u270B', language='pt')))
            time.sleep(2)
            resposta1 = 'Negativo'
            while resposta1 != 'Positivo':
                quem_comeca = random.randint(1, 2)
                if quem_comeca == 1:
                    print('\033[1:34mVamos começar por você {} {}! \033[m'.format(nome,emoji.emojize('\U0001f917', language='pt')))
                    adivinhacao = str(input('\n\033[1:34mDigite a Adivinhação {}:\033[m '.format(nome))).strip().capitalize()
                    dica = str(input('\n\033[1:36mDigite a Primeira Dica {}:\033[m '.format(nome))).strip().capitalize()
                    dica1 = str(input('\033[1:36mDigite a Segunda Dica {}:\033[m '.format(nome))).strip().capitalize()
                    dica2 = str(input('\033[1:36mDigite a Terceira Dica {}:\033[m '.format(nome))).strip().capitalize()
                    adivinhar_novamente = 'Sim'
                    while adivinhar_novamente == 'Sim':
                        resposta = str(input('''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
\033[1:31mA primeira dica é:\033[m \033[1:33m{}\033[m\033[1:31m!\033[m
\033[1:31mA segunda dica é:\033[m \033[1:33m{}\033[m\033[1:31m!\033[m
\033[1:31mA terceira dica é:\033[m \033[1:33m{}\033[m\033[1:31m!\033[m
        
\033[1:34mÉ sua vez {}\033[m ... \033[1:31m Adivinhe {}:\033[m   '''.format(dica, dica1, dica2, nome1,emoji.emojize('\U0001f52e', language='pt')))).strip().capitalize()
                        print('\n\033[1:35mPROCESSANDO A REPOSTA!\nAGUARDE... {}\033[m\n'.format(emoji.emojize('\U0001f440', language='pt')))
                        time.sleep(2)
                        if adivinhacao == resposta:
                            print('\033[1:32mVocê Venceu {} {}\033[m'.format(nome1, emoji.emojize('\U0001f4af', language='pt')))
                            resposta1 = 'Positivo'
                            print('\n\033[1:32mVocês querem jogar novamente?\033[m')
                            jogar_novamente = str(input('\033[1:34mSim / Não:\033[m ')).strip().capitalize()
                            while jogar_novamente != 'Sim' and jogar_novamente != 'Não':
                                print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
                                print('\033[1:32mVocê querem jogar novamente?\033[m')
                                jogar_novamente = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
                            adivinhar_novamente = 'Não'
                        elif adivinhacao != resposta:
                            print('\033[1:31mVocê Errou {} {}\033[m\n'.format(nome1, emoji.emojize('\U0001f623', language='pt')))
                            print('\033[1:32mQuer tentar adivinhar novamente?\033[m')
                            adivinhar_novamente = str(input('\033[1:34mSim / Não:\033[m ')).strip().capitalize()
                            while adivinhar_novamente != 'Sim' and adivinhar_novamente != 'Não':
                                print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
                                print('\033[1:32mQuer adivinhar novamente?\033[m')
                                adivinhar_novamente = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
                            if adivinhar_novamente == 'Não':
                                print('\n\033[1:31mA Adivinhação é \033[m \033[1:33m"{}"\033[m\033[1:31m!\033[m'.format(adivinhacao))
                                print('\n\033[1:32mVocês querem sortear os jogadores novamente e jogar denovo?\033[m')
                                jogar_novamente = str(input('\033[1:34mSim / Não:\033[m ')).strip().title()
                                resposta1 = 'Positivo'
                                while jogar_novamente != 'Sim' and jogar_novamente != 'Não':
                                    print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
                                    print('\033[1:32mVocês querem voltar e jogar novamente?\033[m')
                                    jogar_novamente = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().capitalize()

                else:
                    print('\n\033[1:34mVamos começar por você {} {}! \033[m'.format(nome1,emoji.emojize('\U0001f917', language='pt')))
                    adivinhacao = str(input('\n\033[1:34mDigite a Adivinhação {}:\033[m '.format(nome1))).strip().title()
                    dica = str(input('\n\033[1:36mDigite a Primeira Dica {}:\033[m '.format(nome1))).strip().capitalize()
                    dica1 = str(input('\033[1:36mDigite a Segunda Dica {}:\033[m '.format(nome1))).strip().capitalize()
                    dica2 = str(input('\033[1:36mDigite a Terceira Dica {}:\033[m '.format(nome1))).strip().capitalize()

                    adivinhar_novamente = 'Sim'
                    while adivinhar_novamente == 'Sim':
                        resposta = str(input('''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
\033[1:31mA primeira dica é:\033[m \033[1:33m{}\033[m\033[1:31m!\033[m
\033[1:31mA segunda dica é:\033[m \033[1:33m{}\033[m\033[1:31m!\033[m
\033[1:31mA terceira dica é:\033[m \033[1:33m{}\033[m\033[1:31m!\033[m     
        
\033[1:34mÉ sua vez {}\033[m ... \033[1:31m Adivinhe {}:\033[m  '''.format(dica, dica1, dica2, nome,emoji.emojize('\U0001f52e', language='pt')))).strip().capitalize()
                        print('\n\033[1:35mPROCESSANDO A REPOSTA!\nAGUARDE... {}\033[m\n'.format(emoji.emojize('\U0001f440', language='pt')))
                        time.sleep(2)
                        if adivinhacao == resposta:
                            print('\033[1:32mVocê Venceu {} {}\033[m'.format(nome, emoji.emojize('\U0001f4af', language='pt')))
                            resposta1 = 'Positivo'
                            print('\n\033[1:32mVocês querem jogar novamente?\033[m')
                            jogar_novamente = str(input('\033[1:34mSim / Não:\033[m ')).strip().capitalize()
                            while jogar_novamente != 'Sim' and jogar_novamente != 'Não':
                                print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
                                print('\033[1:32mVocê querem jogar novamente?\033[m')
                                jogar_novamente = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().capitalize()
                            adivinhar_novamente = 'Não'
                        elif adivinhacao != resposta:
                            print('\033[1:31mVocê Errou {} {}\033[m\n'.format(nome, emoji.emojize('\U0001f623', language='pt')))
                            print('\033[1:32mQuer tentar adivinhar novamente?\033[m')
                            adivinhar_novamente = str(input('\033[1:34mSim / Não:\033[m ')).strip().capitalize()
                            while adivinhar_novamente != 'Sim' and adivinhar_novamente != 'Não':
                                print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
                                print('\033[1:32mQuer adivinhar novamente?\033[m')
                            if adivinhar_novamente == 'Não':
                                print('\n\033[1:31mA Adivinhação é \033[m \033[1:33m"{}"\033[m\033[1:31m!\033[m'.format(adivinhacao))
                                print('\n\033[1:32mVocês querem sortear os jogadores novamente e jogar denovo?\033[m')
                                jogar_novamente = str(input('\033[1:34mSim / Não:\033[m ')).strip().title()
                                resposta1 = 'Positivo'
                                while jogar_novamente != 'Sim' and jogar_novamente != 'Não':
                                    print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
                                    print('\033[1:32mVocês querem voltar e jogar novamente?\033[m')
                                    jogar_novamente = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
        if jogar_novamente == 'Não':
            print('\n\033[1:32mVocê tem certeza?\033[m\n\033[1:31mDigite\033[m \033[1:33m"Sim"\033[m \033[1:31mou\033[m \033[1:33m"Não"\033[m\033[1:31m!\033[m')
            jogar_novamente = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
            while jogar_novamente != 'Sim' and jogar_novamente != 'Não':
                print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
                print('\n\033[1:32mVocê tem certeza?\033[m\n\033[1:31mDigite\033[m \033[1:33m"Sim"\033[m \033[1:31mou\033[m \033[1:33m"Não"\033[m\033[1:31m!\033[m')
                jogar_novamente = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
            if jogar_novamente == 'Sim':
                jogar_novamente = 'Sair'
            elif jogar_novamente == 'Não':
                print('\n\033[1:33mJá que não tem certeza... Que tal jogar novamente?\033[m')
                print('\033[1:32mQuer jogar novamente?\033[m')
                jogar_novamente = str(input('\033[1:34mSim / Não:\033[m ')).strip().title()
                while jogar_novamente != 'Sim' and jogar_novamente != 'Não':
                    print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
                    print('\033[1:32mQuer jogar novamente?\033[m')
                    jogar_novamente = str(input('\n\033[1:34mSim / Não:\033[m ')).strip().title()
                if jogar_novamente == 'Não':
                    jogar_novamente = 'sair'

else:
    print('\n{}\033[7::40mOpção Inválida!\033[m{}'.format(emoji.emojize('\u274C\u274C\u274C', language='pt'),emoji.emojize('\u274C\u274C\u274C', language='pt')))
input('\n\033[1:34mDigite "sair" para sair: \033[m')