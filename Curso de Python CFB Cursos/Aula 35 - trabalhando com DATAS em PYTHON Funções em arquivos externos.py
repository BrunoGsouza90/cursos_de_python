import datetime

data = datetime.datetime.now()

print(str(data.day) + "/" + str("0" + str(data.month)) + "/" + str(data.year))
nascimento = datetime.datetime(1978,3,7)
print(nascimento)
print(data.strftime("%M"))
'''
Abreviações do strftime:

%a - Texto do dia da semana resumido.
%A - Texto do dia da semana.
%w - Número do dia semana.
%d - Número do dia do mês.
%b - Texto do mês resumido.
%B - Texto do mês.
%m - Número do mês.
%y - Ano com dois dígitos.
%Y - Ano com quatro dígitos.
%H - Hora de 00h - 23h.
%I - Hora 00h - 12h.
%p - Hora americana AM / PM.
%M - Minutos.
%S - Segundos.
%f - Microsecundos.
%j - Dia do ano 001 - 366.
%W - Número da semana do ano.
'''