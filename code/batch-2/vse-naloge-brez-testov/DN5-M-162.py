def unikati(s):
    w = []
    for c in s:
        if c not in w:
            w.append(c)
    return w


def avtor(tvit):
    w = tvit.split(":")
    return w[0]


def vsi_avtorji(tviti):
    m = []
    for e in tviti:
        m.append(avtor(e))
    return unikati(m)


def izloci_besedo(beseda):
    w = list(beseda)
    i = (-1)
    b = (-1)
    for e in w:
        i += 1
        if e.isalnum():
            w1 = w[i:]
            w1 = w1[::-1]
            for e1 in w1:
                b += 1
                if e1.isalnum():
                    wfinalno = w1[b:]
                    wfinalno = wfinalno[::-1]
                    return "".join(wfinalno)


def se_zacne_z(tvit, c):
    w = list(tvit.split())
    wfin = []
    for e in w:
        ke = list(e)
        if ke[0] is c:
            wfin.append((izloci_besedo(e)))
    return wfin


def zberi_se_zacne_z(tviti, c):
    wfin = []
    for stavek in tviti:
        w = stavek.split()
        for e in w:
            ke = list(e)
            if ke[0] is c:
                wfin.append((izloci_besedo(e)))
    return unikati(wfin)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    pomen = vse_afne(tviti)
    tvit = vsi_avtorji(tviti)
    vsi = []
    for e in pomen:
        vsi.append(e)
    for e1 in tvit:
        if e1 not in pomen:
            vsi.append(e1)
    return sorted(vsi)


def custva(tviti, hashtagi):
    a = []
    for h in hashtagi:
        h1 = "#" + h
        for tvit in tviti:
            if h1 in tvit:
                a.append(avtor(tvit))
    return unikati(sorted(a))


def se_poznata(tviti, oseba1, oseba2):
    oseba_avtor = oseba1 + ":"
    oseba_oznacena = "@" + oseba2
    for tvit in tviti:
        if oseba_avtor in tvit:
            if oseba_oznacena in tvit:
                return True
    return False

