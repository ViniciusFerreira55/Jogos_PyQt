import random
res1 = "Sim, com certeza"
res2 = "Definitivamente não"
res3 = "Talvez"
res4 = "Sim"
res5 = "Não"
res6 = "Não sei"
while True:
    pergunta = str(input("Digite a sua pergunta: "))
    res = random.randrange(0, 7)
    if res == 1:
        print(res1)
    elif res == 2:
        print(res2)
    elif res == 3:
        print(res3)
    elif res == 4:
        print(res4)
    elif res == 5:
        print(res5)
    elif res == 6:
        print(res6)
    op = int(input("Deseja continuar (1-S/2-N)"))
    if op == 1:
        continue
    elif op == 2:
        print("Adeus")
        break