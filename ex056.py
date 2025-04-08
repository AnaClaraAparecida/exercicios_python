s = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while s not in 'MmFf':
    s = str(input('Dados invalidos. Por favor, informe seu sexo novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(s))



