
def preberi(ime_datoteke):
    slovar = {}
    count = 1
    with open(ime_datoteke) as f:
        for line in f:
            seznam = [int(num) for num in line.split(' ')]
            min_index = seznam.index(min(seznam))
            arr = seznam[min_index:] + seznam[:min_index]
            slovar[count] = arr
            count += 1
    return slovar


def mozna_pot(pot, zemljevid):

    prejsnji = pot[0]
    zadnji = pot[len(pot) - 1]

    if len(zemljevid[prejsnji]) != 1:
        # print("Prvi ni koncni")
        return False
    if len(zemljevid[zadnji]) != 1:
        # print("Zadnji ni koncni")
        return False

    if len(pot) < 3:
        if prejsnji not in zemljevid[zadnji]:
            return False

    for i in range(1, len(pot) - 1):
        trenutni = pot[i]
        if len(zemljevid[trenutni]) == 1 and trenutni != zadnji:
            # print("Trenutni je koncni: " + str(trenutni))
            return False

        if prejsnji not in zemljevid[trenutni]:
            # print("Ni povezave med: " + str(prejsnji) + " in " + str(trenutni))
            return False
        prejsnji = trenutni

    return True


def hamiltonova(pot, zemljevid):

    mozna = mozna_pot(pot, zemljevid)
    if not mozna:
        return False

    obiskano = list()
    krozisca = list()

    for krozisce in pot:
        if krozisce in obiskano:
            return False
        if len(zemljevid[krozisce]) > 1:
            obiskano.append(krozisce)

    for key in zemljevid.keys():
        if len(zemljevid[key]) > 1:
            krozisca.append(key)

    if sorted(obiskano) == sorted(krozisca):
        return True
    else:
        return False



