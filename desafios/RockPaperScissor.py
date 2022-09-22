import random
pcp = 0
usp = 0
dr = 0
while True:
    player = int(input("1-Pedra; 2-Papel; 3-Tesoura\nQual você escolhe: "))
    computer = random.randint(1,3)
    if computer == 1:
        print("Computador escolheu Pedra")
    elif computer == 2:
        print("Computador escolheu Papel")
    elif computer == 3:
        print("Computador escolheu Tesoura")
    if player == computer:
        dr += 1
        print("Empate!")
    elif player == 1 and computer == 2:
        pcp += 1
        print("Computador Ganhou")
    elif player == 1 and computer == 3:
        usp += 1
        print("Usuário Ganhou")
    elif player == 2 and computer == 1:
        usp += 1
        print("Usuário Ganhou")
    elif player == 2 and computer == 3:
        pcp += 1
        print("Computador Ganhou")
    elif player == 3 and computer == 1:
        pcp += 1
        print("Computador Ganhou")
    elif player == 3 and computer == 2:
        usp += 1
        print("Usuário Ganhou")
    print("-"*40)
    print("Placar")
    print("Computador: ",pcp)
    print("Usuário: ", usp)
    print("Empates: ", dr)
    print("-"*40)
    op = str(input("Deseja continuar? S/N: "))
    if op in 'sS':
        continue
    elif op in 'nN':
        break