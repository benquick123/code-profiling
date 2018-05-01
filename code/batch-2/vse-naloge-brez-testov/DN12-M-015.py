import operator

def preberi(ime_datoteke):
    f = open(ime_datoteke, "r")
    dict = {}
    st = 1

    s = []
    z = []
    xx = 0
    i = 0
    b = 3

    for line in f.readlines():
        s = []
        line = line.replace("\n", "")
        vrsta = line.split(" ")

        vrstica = list(map(int, vrsta))

        minimum = min(vrstica)
        for x in vrstica:
            if x == minimum:
                break
            else:
                xx = x
                s.append(xx)
        b = len(s)
        z = vrstica + s
        z = z[b:]

        dict.update({st: z})
        st += 1
    return dict

#pot = [3, 5, 6, 8]
def mozna_pot(pot, zemljevid):
    rezultat = True

    for x1, x2 in zip(pot, pot[1:]):
        sosedje = zemljevid[x1]
        if x2 not in sosedje or x1 == x2:
            rezultat = False
    for x in pot[1:-1]:
        y = zemljevid[x]
        if len(y) < 2:
            rezultat = False
    a = pot[0]
    aa = zemljevid[a]
    if len(aa) > 1:
        rezultat = False
    b = pot[len(pot) - 1]
    bb = zemljevid[b]
    if len(bb) > 1:
        rezultat = False
    return rezultat

def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False
    for kljuc in zemljevid:
        if kljuc not in pot and len(zemljevid[kljuc]) > 1:
            return False
    for x in pot:
        if pot.count(x)>1:
            return False
    return True








