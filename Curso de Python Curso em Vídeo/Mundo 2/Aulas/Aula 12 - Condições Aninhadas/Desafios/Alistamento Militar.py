import datetime

ano = int(input('\nDigite seu ano de nascimento: '))
atual = datetime.date.today().year
idade = atual - ano
if idade < 18:
    print('\nAinda não está na hora de se alistar... \033[1:33mAguarde seus 18 anos, falta(m) apenas {} ano(s)!\033[m'.format(18 - idade))
elif idade == 18:
    print('\nChegou a hora de se alistar... \033[1:33mVocê tem até dezembro para se alistar!\033[m')
else:
    print('''\nSeu tempo de alistamento já venceu...\033[1:33mCompareça a Junta de Serviço Militar mais 
próxima da sua residência, pagar a multa militar por estar fora do prazo e realizar seu 
alistamento.   O que acontecerá se não se alistar: O que acontecerá se não se alistar: 
Além da multa, quem não se alista no prazo estará em débito com o Serviço Militar e não 
poderá: Obter passaporte ou prorrogação de sua validade; Ingressar como funcionário, 
empregado ou associado em - instituição, empresa ou associação oficial, oficializada ou 
subvencionada; Assinar contrato com o Governo Federal, Estadual, dos Territórios ou 
Municípios; Prestar exame ou matricular-se em qualquer estabelecimento de ensino; 
Obter carteira profissional, registro de diploma de profissões liberais, matrícula ou 
inscrição para o exercício de qualquer função e licença de indústria e profissão; 
Inscrever-se em concurso para provimento de cargo público; Exercer, a qualquer título, 
sem distinção de categoria ou forma de pagamento, qualquer função pública ou cargo 
público, eletivos ou de nomeação; e Receber qualquer prêmio ou favor do Governo 
Federal, Estadual, dos Territórios ou Municípios.\033[m
\033[1:31mVocê se atrasou {} ano(s)!\033[m'''.format(idade - 18))
input('\n\033[1:34mDigite "sair" para sair: \033[m')