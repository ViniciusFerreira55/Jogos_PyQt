frase = str(input("Digite uma frase: ")).strip().upper()
aux1 = frase.split()
aux2 = ''.join(aux1)
esarf = aux2[::-1]
if esarf == aux2:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
