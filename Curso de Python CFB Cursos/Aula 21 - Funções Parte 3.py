valores = [1,5,3,2,4,5,6,8]
def somar(num):
    r = 0
    for n in num:
        r += n
    return r
print(str(valores) + " soma = " + str(somar(valores)))