from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
idade = date.today().year - ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Sua categoria é a MIRIM')
elif idade <= 14:
    print('Sua categoria é a INFANTIL')
elif idade <= 19:
    print('Sua categoria é a JUNIOR')
elif idade <= 25:
    print('Sua categoria é a SENIOR')
else:
    print('Sua categoria é a MASTER')
