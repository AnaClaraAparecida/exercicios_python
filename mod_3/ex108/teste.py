from ex108 import moedas
p = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentado 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}')
