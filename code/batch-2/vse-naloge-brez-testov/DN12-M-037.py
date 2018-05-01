########################
# Za oceno 6

def preberi(ime_datoteke):
    urejena_datoteka = {}
    stevec = 1
    datoteka = open(ime_datoteke, "r", encoding="utf-8")
    for vrstica in datoteka:
        seznam = [int(x) for x in vrstica.strip().split()]
        najmin = min(seznam)
        cifra = seznam.index(najmin)
        urejena_datoteka[stevec] = [najmin] + seznam[cifra + 1:] + seznam[0 : cifra]
        stevec += 1
    datoteka.close()
    return urejena_datoteka

def mozna_pot(pot, zemljevid):
    prva_zadnja_tocka = len(zemljevid[pot[0]]) == len(zemljevid[pot[len(pot) - 1]]) == 1
    vmesne_tocke = all([False for tocka in pot[1:-1] if len(zemljevid[tocka]) <= 1])
    ni_podvojenih_tock = all([False for t1, t2 in zip(pot, pot[1:]) if t1 == t2])
    prevozne_povezave = all([k2 in zemljevid[k1] for k1, k2 in zip(pot, pot[1:])])
    return True == prva_zadnja_tocka == vmesne_tocke == ni_podvojenih_tock == prevozne_povezave

def hamiltonova(pot, zemljevid):
    pot_obstaja = mozna_pot(pot, zemljevid)
    vsa_krozisca = list(zemljevid.keys() - [kljuc for kljuc in zemljevid if len(zemljevid[kljuc]) <= 1]) == sorted(pot[1:-1])
    ni_duplikatov = len(set(pot)) == len(pot)
    return True == pot_obstaja == vsa_krozisca == ni_duplikatov


########################
# Za oceno 7

def navodila(pot, zemljevid):
    navigacija = []
    for st_krozisca in range(1, len(pot)-1):
        izvozi_krozisca = zemljevid[pot[st_krozisca]]
        izvoz = izvozi_krozisca.index(pot[st_krozisca + 1]) - izvozi_krozisca.index(pot[st_krozisca - 1])
        navigacija.append(izvoz % len(izvozi_krozisca))
    return navigacija

########################
# Za oceno 8

def prevozi(zacetek, navodila, zemljevid):
    prevozeno = [zacetek] + zemljevid[zacetek]
    for st_izvoz in navodila:
        vsi_izvozi = zemljevid[prevozeno[-1]]
        izberi_izvoz = (vsi_izvozi.index(prevozeno[-2]) + st_izvoz) % len(vsi_izvozi)
        prevozeno.append(vsi_izvozi[izberi_izvoz])
    return prevozeno


########################
# Za oceno 9

def sosedi(doslej, zemljevid):
    mostovi = set()
    for izvoz in doslej:
        mostovi = mostovi | (set(zemljevid[izvoz]))
    return mostovi - set(doslej)


def razdalja(x, y, zemljevid):
    vsi_od_x = set(zemljevid[x])
    kilometri = 1
    while y not in vsi_od_x:
        for st in vsi_od_x:
            vsi_od_x = vsi_od_x | set(zemljevid[st])
        kilometri += 1
    return kilometri


########################
# Za oceno 10


def najkrajsa_navodila(x, y, zemljevid):
    pot_z_sosedi = pot(y, zemljevid)
    krozisce = x
    uporabljena_krozisca = [krozisce]
    while krozisce != y:
        krozisce = pot_z_sosedi[krozisce]
        uporabljena_krozisca.append(krozisce)
    kratka_navodila = navodila(uporabljena_krozisca, zemljevid)
    return kratka_navodila

def pot(y, zemljevid):
    mozna_krozisca = [y]
    pot_z_sosedi = {}
    for krozisce in mozna_krozisca:
        izvozi = zemljevid[krozisce]
        for izvoz in zemljevid.keys():
            if (izvoz in izvozi) and (izvoz not in pot_z_sosedi):
                pot_z_sosedi[izvoz] = krozisce
                mozna_krozisca.append(izvoz)
    return pot_z_sosedi



