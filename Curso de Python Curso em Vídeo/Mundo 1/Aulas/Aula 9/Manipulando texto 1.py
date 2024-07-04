frase = ('Curso em Vídeo Python')
a = frase[::2]
print('"A frase "Curso em Vídeo Python" do começo ao fim sendo pulada de 2 em 2 letras é "{}"!'.format(a))
print('''    Tomara que a gente não desista de ser quem é por nada nem ninguém deste mundo.
    Que a gente reconheça o poder do outro sem esquecer do nosso.
    Que as mentiras alheias não confundam as nossas verdades, mesmo que as mentiras e as verdades sejam impermanentes.
    Que friagem nenhuma seja capaz de encabular o nosso calor mais bonito.
    Que, mesmo quando estivermos doendo, não percamos de vista nem de sonho a ideia da alegria.
    Tomara que, apesar dos apesares todos, a gente continue tendo valentia suficiente para não abrir mão de se sentir feliz.
    As coisas vão dar certo.
    Vai ter amor, vai ter fé, vai ter paz – se não tiver, a gente inventa.
    Te quero ver feliz, te quero ver sem melancolia nenhuma.
    Certo, muitas ilusões dançaram.
    Mas eu me recuso a descrer absolutamente de tudo, eu faço força para manter algumas esperanças acesas como velas.''')
b = '''    Tomara que a gente não desista de ser quem é por nada nem ninguém deste mundo.
    Que a gente reconheça o poder do outro sem esquecer do nosso.
    Que as mentiras alheias não confundam as nossas verdades, mesmo que as mentiras e as verdades sejam impermanentes.
    Que friagem nenhuma seja capaz de encabular o nosso calor mais bonito.
    Que, mesmo quando estivermos doendo, não percamos de vista nem de sonho a ideia da alegria.
    Tomara que, apesar dos apesares todos, a gente continue tendo valentia suficiente para não abrir mão de se sentir feliz.
    As coisas vão dar certo.
    Vai ter amor, vai ter fé, vai ter paz – se não tiver, a gente inventa.
    Te quero ver feliz, te quero ver sem melancolia nenhuma.
    Certo, muitas ilusões dançaram.
    Mas eu me recuso a descrer absolutamente de tudo, eu faço força para manter algumas esperanças acesas como velas.'''
c = input('Digite uma letra: ')
print('A letra "{}" aparaceu {} vezes no texto acima!'.format(c,b.count(c)))
nome = str(input('Digite seu nome completo: '))
nome1 = nome.upper()
nome4 = nome.lower()
print('Seu nome em letras maiúsculas é: {}!'.format(nome1))
print('Seu nome em letras minúsculas é: {}!'.format(nome4))
print('Seu nome agora tem {} "A" maiúsculos!'.format(nome1.count('A')))
print('Seu nome tem {} letras!'.format(len(nome1)))
nome2 = str(input('Digite o nome de alguem aleatório com espaços no começo e fim: '))
print('O nome que você digitou foi "{}"!'.format(nome2))
print('O nome que você digitou sem os espaços indesejados é: {}!'.format(nome2.strip()))
nome3 = str(input('Digite seu nome todo bagunçado: '))
print('O nome que você digitou foi "{}", porém seu nome completo correto é "{}"!'.format(nome3,nome3.replace(nome3, nome)))
input('Digite "sair" para sair: ')