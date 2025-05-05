cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorzez',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    n = int(input('Escolha um numero de 0 a 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente, error...')
resp = ' '
while resp not in 'SN':
    esc = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if esc == 'N':
         break
print(f'O numero digitado foi {cont[n]}')