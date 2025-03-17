num = int(input('digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(' a sua unidade é {}\n sua dezena é {}\n sua centena é {}\n seu milhar é {}'.format(u,d, c, m))
