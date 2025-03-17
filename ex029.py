n = int(input('digite um numero, e eu te direi se é par ou impar: '))
r = n % 2
if r ==0:
    print('o numero {} é PAR!'.format(n))
else:
    print('o numero {} é IMPAR!'.format(n))