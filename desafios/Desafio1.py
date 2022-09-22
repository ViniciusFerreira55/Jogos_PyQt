from random import randrange
while True:
    certo = randrange(0, 101)
    pontos = 50
    vidas = 5
    cont = 0
    while cont < 5:

        print("Você possui", vidas, " vidas e ", pontos, "pontos")
        num = int(input("Digite um número: "))

        if num == certo:
            print("Você acertou parábens")
            break

        elif num != certo:
            print("Você errou.")
            vidas = vidas - 1
            if certo > num:
                pontos -= (certo - num)
            elif certo < num:
                pontos -= (num - certo)

        if pontos <= 0 or vidas <= 0:
            print("Perdeu")
            break

    print("Obrigado por jogar!!")
    print("O número era:", certo)
    op = str(input("Deseja jogar novamente S/N")).upper()
    if op in 'S':
        continue
    elif op in 'N':
        break