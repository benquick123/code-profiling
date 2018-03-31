def preberi(ime_datoteke):
    x = open(ime_datoteke, "r")

    slovar = {}
    for st, vrstica in enumerate(x, start=1):
        slovar[st] = vrstica.split()
        slovar[st] = [int(y) for y in slovar[st]]

        while min(slovar[st]) != slovar[st][0]:
            pridrzi = slovar[st][0]
            for i in range(1, len(slovar[st])):
                slovar[st][i - 1] = slovar[st][i]
            slovar[st][-1] = pridrzi

    x.close()
    return slovar


def mozna_pot(pot, zemljevid):
    if len(pot) == 0 or len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False

    for od, do in zip(pot, pot[1:]):
        if od == do or do not in zemljevid[od] or len(zemljevid[od]) == 1 and od != pot[0]:
            return False

    return True


def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False

    krozisca = {x for x, povezave in zemljevid.items() if len(povezave) != 1} #samo krozisca, ne vhodi in izhodi!
    for tocka in pot[1:-1]:
        if tocka in krozisca:
            krozisca.remove(tocka)
        else:
            return False

    if len(krozisca) != 0:
        return False
    return True

def navodila(pot, zemljevid): #[3, 1, 3, 2, 3]
    return [(zemljevid[el2].index(el3) - zemljevid[el2].index(el1)) % len(zemljevid[el2]) for el1, el2, el3 in zip(pot, pot[1:], pot[2:])]


def prevozi(zacetek, navodila, zemljevid):
    tocke = []

    tocke.append(zacetek)
    tocke.append(zemljevid[zacetek][0])
    # zdej sta notr dva elementa

    for skok in navodila:
        nova = zemljevid[tocke[-1]]
        while (nova[0] != tocke[-2]):
            prvi = nova[0]
            for i in range(1, len(nova)):
                nova[i - 1] = nova[i]
            nova[-1] = prvi
        tocke.append(nova[skok])

    return tocke


def sosedi(doslej, zemljevid):
    sosedje = set()
    for tocka in doslej:
        sosedje |= set(zemljevid[tocka])
    return sosedje - doslej
