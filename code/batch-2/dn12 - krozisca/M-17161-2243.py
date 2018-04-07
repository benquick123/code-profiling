# Ocena 6
def preuredi(s):
    s = s.split(" ")
    s = [int(i) for i in s]
    index_min = s.index(min(s))
    return s[index_min:] + s[:index_min]


def preberi(ime_datoteke):
    kr = 1
    d = dict()
    for vrstica in open(ime_datoteke):
        v = vrstica.strip()
        if len(v) == 1:
            v = [int(i) for i in v]
            d[kr] = list(v)
        else:
            d[kr] = preuredi(v)
        kr += 1
    return d


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1:
        vmes = pot[1:-1]
        for i in vmes:
            if len(zemljevid[i]) == 1:
                return False
        for i in range(len(pot) - 1):
            if pot[i + 1] not in zemljevid[pot[i]]:
                return False
        return True
    return False


def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):
        pot = pot[1:-1]
        vsa_k = {}
        for k, v in zemljevid.items():
            if len(v) != 1:
                vsa_k[k] = 0
        for i in pot:
            vsa_k[i] += 1
        return all(x == 1 for x in vsa_k.values())
    return False


# Ocnea 7
def navodila(pot, zemljevid):
    s = []
    izz = pot[0]
    pot = pot[1:]
    for i in range(len(pot) - 1):
        if i == 0:
            iz = izz
        else:
            iz = pot[i - 1]
        iz_ind = zemljevid[pot[i]].index(iz)
        v_ind = zemljevid[pot[i]].index(pot[i + 1])
        if iz_ind < v_ind:
            s.append(v_ind - iz_ind)
        else:
            c = 0
            sezn = zemljevid[pot[i]]
            rr = len(sezn) - 1
            while iz_ind != v_ind:
                if iz_ind == rr:
                    iz_ind = 0
                    c += 1
                else:
                    iz_ind += 1
                    c += 1
            s.append(c)
    return s


# Ocena 8
def prevozi(zacetek, navodila, zemljevid):
    s = [zacetek, zemljevid[zacetek][0]]
    j = 0
    for i in range(len(navodila)):
        prej = s[i]
        nasl = s[i + 1]
        sezn = zemljevid[nasl]
        prej_ind = sezn.index(prej)
        for k in range(navodila[j]):
            if prej_ind == len(sezn)-1:
                prej_ind = 0
            else:
                prej_ind += 1
        s.append(sezn[prej_ind])
        j+=1
    return s

