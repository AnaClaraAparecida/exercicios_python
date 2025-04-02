n = int(input('\033[36mDigite um numero: \033[m'))
n1 = int(input('\033[36mDigite outro numero: \033[m '))
if n > n1:
    print('O numero \033[32m{}\033[m, é maior que o numero \033[32m{}\033[m'.format(n, n1))
elif n == n1:
    print('O numero \033[32m{}\033[m e o numero \033[32m{}\033[m, correspondem ao mesmo valor.'.format(n, n1))
else:
    print('o numero \033[32m{}\033[m é menor que o numero \033[32m{}\033[m'.format(n, n1))




