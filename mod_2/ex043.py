print('{:=^40}'.format(' GOOD THINGS MARKET '))
preço = float(input('Qual o valor da sua compra? '))
print('''FORMAS DE PAGAMENTO 
[1] À vista dinheiro/cheque
[2] À vista no cartao 
[3] Em ate 2X no cartao 
[4] 3X ou mais no cartao''')
pag = int(input('Qual sera a forma de pagamento? '))
if pag == 1:
    valor = preço - (preço * 10 / 100)
    print('A opção concede a 10% de desconto no dinheiro/cheque')
elif pag == 2:
    valor = preço - (preço * 5 / 100)
    print('A opção concede a compra 5% de desconto no cartão')
elif pag == 3:
    valor = preço
    valor1 = preço / 2
    print('A opção concede a compra em ate 2X sem juros no cartão. Sua parcelas saem no valor de {}'.format(valor1))
elif pag == 4:
    valor = preço + (preço * 20 / 100)
    parc = int(input('Em quantas vezes deseja parcelar? '))
    valor1 = valor / parc
    print('A opção concede a compra em ate 3X ou mais com juros de 20% no cartão')
    print('suas parcelas saem no valor de {:.2f}'.format(valor1))
else:
    valor = preço
    print('OPÇAO INVALIDA, tente novamente')
print('Do valor de {:.2f} sua compra sai no valor de {:.2f}'.format(preço, valor))





