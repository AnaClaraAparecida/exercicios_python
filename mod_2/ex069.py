total = totmil = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Insira o nome do produto: '))
    preço = int(input('insira o preço do produro: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
            break
print('FIM DO PROGRAMA!')
print(f'O total gasto na compra foi de R${total}')
print(f'Na compra, existem {totmil} itens com o valor maior que R$1.000')
print(f'O produto mais barato foi {barato} que custa R${preço}')