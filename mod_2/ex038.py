from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
idade = (date.today().year - ano)
atual = date.today().year
if idade < 18:
    saldo = 18 - idade
    ano1 = atual + saldo
    print('Você vai tem mais {} anos, até seu alistamneto. Que sera no ano de {}'.format(saldo, ano1))
elif idade == 18:
    print('Você já pode se alistar!')
else:
    saldo = idade - 18
    ano1 = atual - saldo
    print('Você deveria ter se alistado a {} anos atras, em {}'.format(saldo, ano1))


