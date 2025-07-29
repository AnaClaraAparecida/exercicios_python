from ex109 import moedas
p = float(input('Digite o preço: R$'))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')#True -> Formatado
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)                                 }')
print(f'Aumentado 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13, True)} ')
