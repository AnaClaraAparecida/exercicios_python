idadeS = 0
idadeM = 0
Midademan = 0
nomeV = ''
mulherT = 0
for p in range (1, 5):
    print('======== PESSOA {} ========'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    idadeS += idade
    if p == 1 and sexo in 'Mm':
        Midademan = idade
        nomeV = nome
    if sexo in 'Mm'and Midademan:
            Midademan = idade
            nomeV = nome
    if sexo in 'Ff' and idade < 20:
        mulherT += 1
idadeM = idadeS / 4
print('A mediade de  idade do grupo é de {}'.format(idadeM))
print('O home mais  velho do grupo tem {} anos e se chama {}'.format(Midademan, nomeV))
print('Ao todo são {} mulheres com menos de vinte anos'.format(mulherT))

