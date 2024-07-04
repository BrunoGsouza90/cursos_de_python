soma = lambda a,b:a+b
mul = lambda a,b,c:(a+b)*c
print(soma(2,5))
print(mul(2,5,3))

print('')

print((lambda a,b:a+b)(3,2))

print('')

r = lambda x,func:x+func(x)
res = r(2, lambda x:x*x)
print(res)

res = r(2, lambda x:x+3)
print(res)