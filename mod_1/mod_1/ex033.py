s = float(input('Informe o valor de seu salario, para aumento: '))
if s <= 1250:
    aumento = (s + (s * 15/100))
    print('O salario de {}, com o aumento foi para {} '.format(s, aumento))
else:
    aumento2 = (s + (s * 10/100))
    print('O salario de {}, com o aumento foi para {}'.format(s, aumento2))