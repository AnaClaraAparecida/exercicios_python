km = float(input('Quantos km a sua viagem vai ter? '))
if km <= 200:
    p = km * 0.50
    print('O valor da sua passagem será de R${} '.format(p))
else:
    p1 = km * 0.45
    print('O valor da sua passagem será de R${} '.format(p1))