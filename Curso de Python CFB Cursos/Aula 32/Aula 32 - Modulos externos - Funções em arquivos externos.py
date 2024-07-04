import canal as cn

cn.canal_nome()
print(cn.jogador["nome"])
print('')

from canal import jogador

print(jogador["energia"])
print('')

import canal

resultado = dir(canal)

print(resultado)