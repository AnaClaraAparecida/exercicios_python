def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO: Entrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero real valido\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mERRO: Entrada de dados interrompida pelo usuario\033[m ')
            return 0
        else:
            return n
#mean
n1 = leiaint('Digite um numero inteiro: ')
n2 = leiafloat('Digite um numero real: ')
print(f'O numero interio foi {n1}, e o real {n2}')