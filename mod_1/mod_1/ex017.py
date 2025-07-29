from math import hypot
co = float(input('qual o valor do cateto oposto? '))
ca = float(input('qual o valor do catetto adjacente? '))
h = hypot(co, ca)
print('o valor da hipotenusa é {:.2f}'.format(h))
