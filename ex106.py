try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados digitados!')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario nao informou os dados!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre, muito obrigado!')