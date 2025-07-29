km = float(input('a quantos km o seu carro está? '))
multa = (km - 80) * 7
if km <= 80:
    print('Tenha um otimo dia, esta liberado!')
else:
    print('Você esta a cima do limite. Será multado com {} reais!'.format(multa))
