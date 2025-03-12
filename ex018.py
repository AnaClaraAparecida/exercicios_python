from math import cos, sin, tan, radians
an = float(input('digite o valor do angulo: '))
sn = sin (radians(an))
print('o angulo tem o valor de {}, com o SENO de {:.2f}'.format(an, sn))
cs = cos(radians(an))
print('o valor do COSSENO é {:.2f}'.format(cs))
tn = tan(radians(an))
print('o valor da TANGENTE é {:.2f}'.format(tn))

