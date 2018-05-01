def preberi(ime_datoteke):
    priloga = []
    for item in open(ime_datoteke, encoding="UTF8"):
        p = [int(s) for s in item.split() if s.isdigit()]
        priloga.append(p)

    for item in priloga:
        mini = min(item)
        min_indeks = item.index(mini)
        premik = min_indeks
        novo = zamik(item, premik)
        item.clear()
        item.extend(novo)

    slovar = dict(zip(range(1,len(priloga)+1), priloga))


    return slovar

def zamik(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

def koncne_postaje(zemljevid):
    odgovor = []
    for item in zemljevid:
        if len(zemljevid[item]) == 1:
            odgovor.append(item)

    return odgovor

def ponavljanje(pot):
    if len(pot) == 1:
        return True
    else:
        prvo = pot[0]
        drugo = pot[1]

        if prvo == drugo:
            return False
        else:
            return ponavljanje(pot[1::])

def potujemo(pot, zemljevid):
    if len(pot) == 1:
        return True
    else:
        prvo = pot[0]
        drugo = pot[1]

        if drugo in zemljevid[prvo]:
            return potujemo(pot[1::], zemljevid)
        else:
            return False

def unikati(pot):
    odgovor = []
    for element in pot:
        if element not in odgovor:
            odgovor.append(element)

        else:
            continue

    return odgovor

def mozna_pot(pot, zemljevid):
    enojne = koncne_postaje(zemljevid)

    if pot[0] in enojne and pot[len(pot)-1] in enojne:

        for krizisce in pot[1:len(pot)-1]:
            if krizisce in enojne:
                return False
            else:
                continue

        if ponavljanje(pot):
            return potujemo(pot, zemljevid)


        else:
            return False

    else:
        return False

def vsa_krizisca(zemljevid):
    t = []
    for item in zemljevid.keys():
        if item not in t:
            t.append(item)
        else:
            continue
    return t

def hamiltonova(pot, zemljevid):
    vsa = vsa_krizisca(zemljevid)
    vhod_izhod = [pot[0], pot[len(pot)-1]]
    vhodi_izhodi = koncne_postaje(zemljevid)
    for item in vhod_izhod:
        if item in vhodi_izhodi:
            vhodi_izhodi.remove(item)
        else:
            continue


    for item in pot:
        if item in vsa:
            vsa.remove(item)
        else:
            continue

    return mozna_pot(pot, zemljevid) and unikati(pot) == pot and vhodi_izhodi == vsa

def navodila(pot, zemljevid):
    seznam = list(zip(pot, pot[1::], pot[2::]))
    odgovor = []
    for item in seznam:
        a, b, c = item
        g = (zemljevid[b].index(c)-zemljevid[b].index(a))%len(zemljevid[b])
        odgovor.append(g)

    return odgovor


def prevozi(zacetek, navodila, zemljevid):
    seznam = []
    druga = zemljevid[zacetek]
    seznam.append(zacetek)
    for item in navodila:
        novo = zemljevid[druga]
        novo.index()






