frase = str(input('digite uma frase: ')).upper().strip()
print('a frase tem no total, {} A'.format(frase.count('A')))
print('a letra A aparece pela primeira vez na posiçao {}'.format(frase.find('A')+1))
print('a ultima letra A apareceu na posiçao {}'.format(frase.rfind('A')+1))