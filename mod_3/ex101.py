def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um numero
    :param num: O numero a ser fatorado
    :param show: (opcional) Mostra ou nao o calculo
    :return: O valor de um Fatorial de um numero n
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
#mean
print(fatorial(5, show=True))
help(fatorial)