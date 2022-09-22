from random import randint
from time import sleep
print("Seja bem-vindo a Roleta do Wilsão")
sleep(2)
print("-"*80)
print("Regras")
print("Escolha uma cor (Vermelho e Preto dobra sua aposta, verde triplica)")
print("Pares são os pretos, vermelhos impares e verde 0")
print("Caso você erre a casa fica com o dinheiro")
print("-"*80)
sleep(5)
saldo = float(input("Digite seu saldo:"))
sleep(1)
while True:
    print("Começando a roleta")
    print("Seu saldo é de: ", saldo)
    sleep(2)
    cor = int(input("Vermelho-1; Preto-2; Verde-3 \nEm qual cor deseja apostar: "))
    sleep(1)
    aposta = float(input("Quanto deseja apostar: "))
    sleep(1)
    saldo = saldo - aposta
    numcor = randint(0,36)
    sleep(1)
    print("O número sorteado foi: ", numcor)
    sleep(1)
    if numcor == 0 and cor == 3:
        print("Você ganhou")
        saldo = saldo +(aposta*3)
    elif numcor % 2 == 0 and cor == 2:
        print("Você ganhou")
        saldo = saldo+(aposta * 2)
    elif numcor % 2 == 1 and cor == 1:
        print("Você ganhou")
        saldo = saldo+(aposta * 2)
    else:
        print("Você perdeu, a casa sempre vence")
    sleep(1)
    if saldo <=0:
        break
    op = str(input("Deseja continuar S/N: "))
    if op in 'sS':
        print("-"*80)
        continue
    elif op in 'nN':
        break
print("Obrigado por jogar, volte sempre")
print("Seu saldo final foi:", saldo)
if saldo > 0:
    print("Você ainda tem dinheiro...")
    sleep(1)
    print("por hora")
else:
    print("A casa sempre vence")

