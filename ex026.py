n = str(input('digite seu nome inteiro: ')).strip()
nome = n.split()
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))