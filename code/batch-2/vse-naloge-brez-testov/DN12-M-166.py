

def preberi(ime_datoteke):
    zemljevid = {}
    datoteka = open(ime_datoteke, "r")
    kljuc = 0
    for vrstica in datoteka:
        kljuc += 1
        stevilke = vrstica.strip().split(" ")
        zemljevid[kljuc] = []
        stevilke2 = []
        indeks = 0
        for i in stevilke:
            stevilke2.append(int(i))
        najmanjsi = min(stevilke2)
        for i in stevilke:
            if najmanjsi in zemljevid[kljuc]:
                indeks += 1
                zemljevid[kljuc].insert(indeks, int(i))
            if int(i) == najmanjsi:
                zemljevid[kljuc].insert(0, int(i))
            if najmanjsi not in zemljevid[kljuc]:
                zemljevid[kljuc].append(int(i))
    return zemljevid

def mozna_pot(pot, zemljevid):
    if not len(zemljevid[pot[0]]) < 2 or not len(zemljevid[pot[-1]]) < 2:
        return False
    for i in range(len(pot)-2):
        if len(zemljevid[pot[i+1]]) < 2:
            return False
    seznam = zip(pot, pot[1:])
    for x, y in seznam:
        if x == y:
            return False
    for i in range(len(pot)-1):
        if pot[i] not in zemljevid[pot[i+1]]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    mnozica = set()
    for i in range(len(zemljevid)):
        if len(zemljevid[i+1]) > 1:
            mnozica.add(i+1)
    seznam = []
    for postaja in pot:
        if postaja not in seznam:
            seznam.append(postaja)
        else:
            return False
    if mozna_pot(pot, zemljevid):
        if set(pot[1:-1]) == mnozica:
            return True
    return False

def navodila(pot, zemljevid):
    seznam = []
    

