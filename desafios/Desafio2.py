import random
saldo = 25
pcp = 0
usp = 0
rev = 0
aux = 0
win = 0
vinte = 0
comeco = True
while saldo > 0:
    if saldo <=0:
        break
    if comeco:
        print("Seu saldo é:", saldo)
        saldo -= 5
        comeco = False
    else:
        if rev == 0:
            saldo -= 5
            print("Seu saldo é:", saldo)
    usn = int(input("Escolha um número entre 1 e 6: "))

    while True:
        if usn > 6 or usn < 1:
            usn = int(input("Digite um valor válido: "))
        else:
            break
    pcn = random.randrange(1, 7)
    while True:
        if pcn == usn:
            pcn = random.randrange(1,7)
        else:
            break
    while usp < 2 or pcp < 2:
        awn = random.randrange(1,7)
        if pcn == awn:
            pcp += 1
        if usn == awn:
            usp += 1
        if pcp == 2 or usp == 2:
            break
    if pcp > usp:
        print("Computador ganhou","\nPontos do user:",usp, "\nPontos do computador",pcp)
        pcp = 0
        aux = 0
        win = 0
        rev = 0

    else:
        print("Usuario ganhou","\nPontos do user:",usp, "\nPontos do computador",pcp)
        usp = 0
        aux = 1
        win = 1
        if rev == 1:
            vinte = 1
    if win == 1 and rev == 0:
        op1 = int(input("Revanche pato? 1-S/2-N "))
        print("--------------------------------------")
        if op1 == 1:
            rev = 1
            continue
        elif op1 == 2:
            saldo = saldo + 10
            break

    op = int(input("Jogar novamente? [1S/2N]: "))
    print("----------------------------------------")
    if op == 1 and win == 1:
        rev = 0
        aux = 0
        if vinte == 1:
            vinte = 0
            saldo += 20
        continue
    elif op == 1 and win == 0:
        rev = 0
        continue
    elif op == 2 and win == 0:
        break
    elif op == 2 and win == 1:
        if vinte == 1:
            vinte = 0
            saldo += 20
        break
if saldo <= 0:
    print("Você está falido, vai trabalhar")
else:
    print("Seu saldo final foi de: ",saldo,"melhor do que nada")