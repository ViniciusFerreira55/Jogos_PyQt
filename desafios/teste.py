def pos(palavra, letra):
    num = palavra.count(letra)
    posi = []
    posia = 0
    '''for _ in range(num):
        posic = palavra.find(letra, posia + 1)
        posia = posic
        posi.append(posic)'''
    for _ in range(len(palavra)):
        if letra == palavra[_]:
            posi.append(_)
    return posi

