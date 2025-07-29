km = float(input('quantos km foram percorridos? '))
dias = int(input('por quantos dias o carro foi alugado? '))
valor = ( dias * 60) + ( km * 0.15)
print('o valor a ser pago é de: {:.2f} '.format(valor))
