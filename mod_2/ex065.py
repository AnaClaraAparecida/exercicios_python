cont = s = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'O total de numeros digitados, foram {cont} e sua soma é de {s}')
