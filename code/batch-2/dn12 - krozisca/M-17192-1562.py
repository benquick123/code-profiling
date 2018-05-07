def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    zemljevid = {}
    i = 1
    for vrstica in datoteka:
        vrednosti = vrstica.split()
        for x in range(0, len(vrednosti)):
            vrednosti[x] = int(vrednosti[x])
        index = 0
        min_index = vrednosti.index(min(vrednosti))
        dolzina = len(vrednosti)
        if dolzina > 1:
            if min_index != 0:
                for pop_index in range(min_index, dolzina):
                    vrednosti.insert(index, vrednosti.pop(pop_index))
                    index += 1
        zemljevid[i] = vrednosti
        i += 1
    datoteka.close()
    return zemljevid


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) == 1:
        if len(zemljevid[pot[len(pot) - 1]]) == 1:
            for x in range(0, len(pot) - 1):
                if pot[x] not in zemljevid[pot[x + 1]]:
                    return False
                elif 0 < x < len(pot):
                    if len(zemljevid[pot[x]]) == 1:
                        return False
            return True
        else:
            return False
    else:
        return False

def hamiltonova(pot, zemljevid):
    hamilton=[]
    pot2= list(pot)
    for x in zemljevid.keys():
        if len(zemljevid[x])!=1:
            hamilton.append(x)

    if mozna_pot(pot,zemljevid)== True:
        del pot2[0]
        del pot2[len(pot2)-1]

        print(hamilton,"\n")
        print(sorted(pot2), "\n")

        if sorted(pot2)==hamilton:
            return True
    return False

def navodila(pot, zemljevid):
    potovanje = []

    for x in range(1, len(pot) - 1):
        vrednosti = zemljevid[pot[x]]
        index = 0
        izhodisce = pot[x - 1]
        dolzina = len(vrednosti)
        if vrednosti[0] != izhodisce:
            for pop_index in range(vrednosti.index(izhodisce), dolzina):
                vrednosti.insert(index, vrednosti.pop(pop_index))
                index += 1
        potovanje.append(vrednosti.index(pot[x + 1]))
    return potovanje

def prevozi(zacetek, navodila, zemljevid):
    lokacija = zemljevid[zacetek]
    potovanje = [zacetek, lokacija[0]]
    for x in range(0, len(navodila)):
        lokacija = potovanje[len(potovanje) - 1]
        izhodisce = potovanje[len(potovanje) - 2]
        destinacija = zemljevid[lokacija]
        index = 0
        if destinacija[0] != izhodisce:
            for pop_index in range(destinacija.index(izhodisce), len(destinacija)):
                destinacija.insert(index, destinacija.pop(pop_index))
                index += 1
        cilj = destinacija[navodila[x]]
        potovanje.append(cilj)
    return potovanje