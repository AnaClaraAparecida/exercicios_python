def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f"\033[0;31mErro: '{entrada}' é um preço inválido\033[m")
        else:
            valido = True
            return float(entrada)

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero valido.\033[m')
        if ok:
            break
    return valor