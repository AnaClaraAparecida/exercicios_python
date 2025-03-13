nome = str(input('digite seu nome: ')).strip()
print('o seu nome em letras maiusculas é {}'.format(nome.upper()))
print('o seu nome em letras minusculas é {}'.format(nome.lower()))
print('o seu nome tem o total de {} letras'.format(len(nome) - nome.count(' ')))
print('o seu primeiro nome tem no total {} letras'.format(nome.find(' ')))



