print('-=-' * 20)
casa = float(input('Qual o valor da casa que deseja adquirir? '))
salario = float(input('Informe o valor de seu salario. '))
anos = int(input('Em quantos anos deseja fazer o finaceamento? '))
print('-=-' * 20)
valor = casa / (anos * 12)
minimo = salario * 30 /100
print('Para finaciar uma casa de {} em {} anos, '.format(casa, anos))
print('você deve pagar {:.2f} de prestação '.format(valor))
if salario >= minimo:
    print('Seu emprestimo foi \033[4;31mNEGADO\033[m')
else:
    print('Seu emprestimo foi \033[4;32mCONCEDIDO!\033[m')