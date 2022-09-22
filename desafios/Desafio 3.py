numero1 = int(input("Primeiro termo "))
numero2 = int(input("Ultimo termo: "))
soma = 0

print("Números de Armostrong: ")
for i in range(numero1,numero2):
    aux = i
    soma = 0
    while aux > 0:
        resto = aux % 10
        soma += resto**(len(str(i)))
        aux /= 10
        aux = int(aux)
    if i == soma:
        print(i)
print("---------------------------------")
for i in range(0,1000):
    aux = i
    soma = 0
    while aux > 0:
        resto = aux % 10
        soma += resto**(len(str(i)))
        aux /= 10
        aux = int(aux)
    if i == soma:
        print(i)