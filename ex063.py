num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print('Você digiou {} numeros e a soma entre eles é de {}'.format(cont, soma))