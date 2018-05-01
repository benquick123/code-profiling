def preberi(ime_datoteke):
    datoteka = open(ime_datoteke, "r")
    d = {}
    i = 0

    for vrstica in datoteka:
        i += 1
        joined = " ".join(vrstica.split())  #razdeljene na koščke v array in združene na presledke
        vrednost = list(map(int, joined.split()))

        min_vrednost = min(vrednost)
        for element in vrednost[:min_vrednost]:
            if element != min_vrednost:
                vrednost.append(element)
                vrednost.remove(element)
            else:
                break

        d[i] = vrednost

    datoteka.close()
    return d

def mozna_pot(pot, zemljevid):
    d_s = len(pot)
    en_manj = len(pot) - 1

    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[d_s-1]]) == 1:
        for element in pot[1:en_manj]:
            if len(zemljevid.get(element)) == 1:
                return False

        for a, b in zip(pot, pot[1:]):
            if a not in zemljevid[b]:
                return False
        return True

    else:
        return False

def hamiltonova(pot, zemljevid):
    krozisca = []
    d_s = len(pot) - 1

    for kljuc, vrednost in zemljevid.items():
        if len(vrednost) > 1:
            if kljuc not in krozisca:
                krozisca.append(kljuc)

    if mozna_pot(pot, zemljevid):
        if set(pot[1:d_s]) == set(krozisca) and len(pot[1:d_s]) == len(krozisca):
            return True
    else:
        return False

def navodila(pot, zemljevid):
    seznam = []

    for vhod, trenutno, izhod in zip(pot, pot[1:], pot[2:]):
        trenutni = zemljevid[trenutno]
        rez1 = zemljevid[trenutno].index(izhod)
        rez2 = zemljevid[trenutno].index(vhod)


        seznam.append((rez1 - rez2) % len(trenutni))

    return seznam

def prevozi(zacetek, navodila, zemljevid):
    seznam = [zacetek, zemljevid[zacetek][0]]
    next = zemljevid[zacetek][0]

    for korak in navodila:
        prev_index = zemljevid[next].index(zacetek)
        exit = (prev_index + korak)

        if (exit >= len(zemljevid[next])):
            exit = exit - len(zemljevid[next])

        zacetek = next
        next = zemljevid[next][exit]

        seznam.append(next)

    return seznam

#IZPISI

print(preberi("zemljevid.txt"))
print(mozna_pot([1, 3, 6, 4, 2, 4, 5, 11, 14, 13, 12], preberi("zemljevid.txt")))
print(hamiltonova([1, 3, 7, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12], preberi("zemljevid.txt")))
print(navodila([1, 3, 6, 4, 2], preberi("zemljevid.txt")))
print(prevozi(12, [2, 1, 5, 1, 1, 2, 2, 3], preberi("zemljevid.txt")))


#TESTI

