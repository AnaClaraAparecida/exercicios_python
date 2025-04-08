from datetime import date
atual = date.today().year
maior = 0
menor = 0
for p in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da pessoa {}: '.format(p)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('A quantidade de maiores de idade sao de {}'.format(maior))
print('A quantidada de menores de idade sao de {}'.format(menor))
