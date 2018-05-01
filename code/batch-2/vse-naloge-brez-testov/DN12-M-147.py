import collections


def preberi(imeDatoteke):
    krizisca = {}
    datoteka = open(imeDatoteke)
    for i, line in enumerate(datoteka, 1):
        krizisca[i] = [int(i) for i in line.split()]
        najmanjsi = min(krizisca[i])
        temp = []
        for j in range(len(krizisca[i])):
            if krizisca[i][0] != najmanjsi:
                a = krizisca[i].pop(0)
                temp.append(a)
        krizisca[i] += temp

    datoteka.close()
    return krizisca


def mozna_pot(pot, zemljevid):
    vhodi = [i for i, j in zemljevid.items() if len(j) == 1]
    if pot[0] not in vhodi or pot[len(pot) - 1] not in vhodi:
        return False
    for i in pot[1:-1]:
        if i in vhodi:
            return False
    for i, j in zip(pot, pot[1:]):
        if i == j:
            return False
        elif j not in zemljevid[i]:
            return False

    return True


def hamiltonova(way, map):
    for value in way:
        if way.count(value) > 1:
            return False
    condition = 0
    final = 0
    #pogledas ce je pot sploh mozna
    if condition > 10:
        return True
    for inxed in map:
        if dolzina(map[inxed]) == 1:
            final = final + 1

    leng1 = dolzina(map)
    lengh = dolzina(way)
    pogoj = leng1 - final
    if pogoj != lengh - 2:
        return False


    return True

def dolzina(a):
    dolzina = len(a)
    return dolzina

