def list():
    if num not in tupla:
        return -1
    else:
        return tupla.index(num)
import random
tupla = []
for i in range(20):
    sn = random.randrange(0,101)
    tupla.append(sn)
print(tupla)
num = int(input("Digite um valor:"))
print(list())