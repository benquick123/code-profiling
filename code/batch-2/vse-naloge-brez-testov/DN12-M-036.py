def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)

    slovar = {}

    stevec = 1

    for vrstica in datoteka:
        vrstica_split = list(map(int, [i for i in vrstica.split()]))
        min_el = int(min(vrstica_split))

        while vrstica_split[0] > min_el:
            vrstica_split += [vrstica_split.pop(0)]

        slovar[stevec] = list(map(int, vrstica_split))
        stevec += 1

    datoteka.close()
    return slovar

def mozna_pot(pot, zemljevid):
    skupine_list = []

    prvi = pot[0]
    zadnji = pot[len(pot) - 1]
    konci = [i for i in zemljevid if len(zemljevid[i]) < 2]

    brez_prvi_zadnji = pot[1:-1]
    st_bpz = len([i for i in range(len(brez_prvi_zadnji)) if brez_prvi_zadnji[i] in konci])

    ponoven = len([i for i in range(len(pot[:-1])) if pot[i] == pot[i + 1]])

    for i in range(len(pot[:-1])):
        if pot[i + 1] in zemljevid[pot[i]] and prvi in konci and zadnji in konci and st_bpz < 1 and ponoven < 1:
            skupine_list.append(True)
        else:
            skupine_list.append(False)

    return all(skupine_list)

def hamiltonova(pot, zemljevid):
    skupine_list = []

    konci = [i for i in zemljevid if len(zemljevid[i]) < 2]

    vsa_krozisca = [i for i in zemljevid if i not in konci]

    cela_pot = sorted([i for i in pot if i not in konci])

    skupine_list.append(mozna_pot(pot, zemljevid))

    if vsa_krozisca != cela_pot:
        skupine_list.append(False)

    return all(skupine_list)

