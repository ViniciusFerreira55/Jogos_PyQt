def db(num):
    if num > 1:
        db(num//2)
    print(num%2, end='')
while True:
    print("1 - Binário para Decimal")
    print("2 - Decimal para Binário")
    print("3 - Sair")
    op = int(input("Digite a opção desejada: "))
    if op == 1:
        num = str(input("Digite um número: "))
        numd = int(num,2)
        print(num,"em decimal é", numd)
    elif op == 2:
        num = int(input("Digite um número: "))
        db(num)
        print("\n")
    elif op == 3:
        print("Adeus!")
        break