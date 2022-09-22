import math
while True:
    print("1-Soma de senos\n2-Subtração de senos\n3-Soma de Cossenos\n4-Subtração de Cossenos\n5-Soma de Tangente\n6-Subtração de tangente\n7-sair")
    op = int(input("Digite a op desejada: "))
    if op ==1:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        sena = math.sin(math.radians(a))
        senb = math.sin(math.radians(b))
        cosa = math.cos(math.radians(a))
        cosb = math.cos(math.radians(b))
        somas = (sena*cosb)+(senb*cosa)
        print(f"A soma é {somas:.2f}")
    if op == 2:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        sena = math.sin(math.radians(a))
        senb = math.sin(math.radians(b))
        cosa = math.cos(math.radians(a))
        cosb = math.cos(math.radians(b))
        subsen = (sena * cosb) - (senb * cosa)
        print(f"A soma é {subsen:.2f}")
    if op == 3:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        sena = math.sin(math.radians(a))
        senb = math.sin(math.radians(b))
        cosa = math.cos(math.radians(a))
        cosb = math.cos(math.radians(b))
        somacos = (cosa * cosb) - (sena * senb)
        print(f"A soma é {somacos:.2f}")
    if op == 4:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        sena = math.sin(math.radians(a))
        senb = math.sin(math.radians(b))
        cosa = math.cos(math.radians(a))
        cosb = math.cos(math.radians(b))
        subcos = (cosa * cosb) + (sena * senb)
        print(f"A soma é {subcos:.2f}")
    if op == 5:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        tanA = math.tan(math.radians(a))
        tanB = math.tan(math.radians(b))
        somaTan = (tanA + tanB)/(1-(tanA*tanB))
        print(f"A soma é {somaTan:.2f}")
    if op == 6:
        a = float(input("Digite o valor de A: "))
        b = float(input("Digite o valor de B: "))
        tanA = math.tan(math.radians(a))
        tanB = math.tan(math.radians(b))
        subTan = (tanA - tanB)/(1+(tanA*tanB))
        print(f"A soma é {subTan:.2f}")
    if op == 7:
        break
    else:
        print("Digite uma opção valida")
        continue