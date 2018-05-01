# Za oceno 6:

def preberi(ime_datoteke):
    zemljevid = {}
    for stevec, vrstica in enumerate(open(ime_datoteke), 1):
        zemljevid[stevec] = [int(i) for i in vrstica.strip().split()]
        while zemljevid[stevec][0] != min(zemljevid[stevec]):
            zemljevid[stevec].append(zemljevid[stevec][0])
            del(zemljevid[stevec][0])
    return zemljevid

def mozna_pot(pot, zemljevid):
    zacetek = pot[0]
    konec = pot[-1]
    for i in range(1, len(pot)):
        if pot[i] == pot[i - 1] or pot[i] not in zemljevid[pot[i - 1]] or (len(zemljevid[pot[i]]) == 1 and i != len(pot) - 1) or len(zemljevid[zacetek]) != 1 or len(zemljevid[konec]) != 1:
            return False
    return True

def hamiltonova(pot, zemljevid):
    krozisca = [i for i in zemljevid if len(zemljevid[i]) > 1]
    for krozisce in krozisca:
        if krozisce not in pot or not mozna_pot(pot, zemljevid) or list(set(pot)) != sorted(pot):
            return False
    return True

# Za oceno 7

def navodila(pot, zemljevid):
    return [(zemljevid[b].index(c) - zemljevid[b].index(a)) % len(zemljevid[b]) for a, b, c in zip(pot, pot[1:], pot[2:])]

# Za oceno 8

def prevozi(zacetek, navodila, zemljevid):
    pot = [zacetek, zemljevid[zacetek][0]]
    for navodilo in navodila:
        trenutni = pot[-1]
        predhodni = pot[-2]
        izvoz = zemljevid[trenutni].index(predhodni) + navodilo
        pot.append(zemljevid[trenutni][izvoz % len(zemljevid[trenutni])])
    return pot

# Za oceno 9:

def sosedi(doslej, zemljevid):
    return {j for i in doslej for j in zemljevid[i] if j not in doslej}

def razdalja(x, y, zemljevid):
    raz = 0
    soseska = sosedi({x}, zemljevid)
    while y not in soseska:
        soseska = sosedi(soseska, zemljevid)
        raz += 1
    return raz + 1

# Za oceno 10:

def sosedi_2(doslej, zemljevid):
    return {j:i for i in doslej for j in zemljevid[i] if j not in doslej}

def skupine_do_cilja(x, y, zemljevid):
    skupine_sosedov = []
    soseska = sosedi_2({x}, zemljevid)
    while y not in soseska:
        skupine_sosedov.append(soseska)
        soseska = sosedi_2(soseska, zemljevid)
    skupine_sosedov.append(soseska)
    return skupine_sosedov

def najkrajsa_navodila(x, y, zemljevid):
    skupine_sosedov = list(reversed(skupine_do_cilja(x, y, zemljevid)))
    pot = [y]
    for skupina in skupine_sosedov:
        for sosed in skupina:
            if sosed == y:
                pot.append(skupina[sosed])
                y = skupina[sosed]
    return navodila(list(reversed(pot)), zemljevid)


