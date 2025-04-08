frase = str(input('Digite uma frase, e te direi se é um palindormo: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('a forma inversa da frase {} é {}'.format(junto, inverso))
#for letra in range(len(junto) -1, -1, -1,):
    #inverso += junto[letra]
if inverso == junto:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')
