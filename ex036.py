num = int(input('Digite um numero inteiro: '))
print('''Selecione uma das opções de conversão:
[0] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opção = int(input('Qual a sua opçao de converção? '))
if opção == 0:
    print('{} convertido para Binário, é {}'.format(num, bin(num) [2:]))
elif opção == 1:
    print('{} convertido para Octal, é {}'.format(num, oct(num) [2:]))
elif opção == 2:
    print('{} convertido para Hexadecimal, é {}'.format(num, hex(num) [2:]))
else:
    print('Opção invalida, tente novamente!')
