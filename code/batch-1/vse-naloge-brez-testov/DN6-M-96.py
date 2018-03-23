def besedilo(tvit):
    besedilo = tvit.split()
    del besedilo[0]
    return ' '.join(str(e) for e in besedilo)

def avtor(tvit):
    t = tvit.split()
    avtor = t[0]
    avtor = avtor[:-1]
    return avtor

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    a = 0
    for tvit in tviti:
        trenutni = avtor(tvit)
        for oseba in slovar:
            if oseba == trenutni:
                a = 1
        if a == 0:
            slovar[avtor(tvit)] = besedilo(tvit)
        a = 0
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = 0
    for tvit in tviti:
        slovar[avtor(tvit)] += 1
    return slovar

def afna(tvit):
    t = tvit.split()
    besede = []
    for beseda in t:
        if beseda.startswith("@"):
            besede.append(izloci_besedo(beseda))
    return besede

def izloci_besedo(beseda):
    from string import ascii_letters, digits
    return "".join([ch for ch in beseda if ch in (ascii_letters + digits + "-")])


def omembe(tviti):
    slovar = {}
    preverjeni = []

    for tvit in tviti:
        if avtor(tvit) not in preverjeni:
            slovar[avtor(tvit)] = omenil(avtor(tvit), tviti)
        preverjeni.append(avtor(tvit))
    return slovar

def omenil(ime, tviti):
    omenjeni = []
    for tvit in tviti:
        if ime == avtor(tvit):
            omenjeni = omenjeni + afna(tvit)
    return omenjeni

def neomembe(ime, omembe):
    neomenjeni = []
    omenjeni = []
    for name in omembe:
        omenjeni.append(name)
    for oseba in omenjeni:
        if oseba not in omembe[ime] and oseba != ime:
            neomenjeni.append(oseba)
    return neomenjeni

def se_poznata(ime1, ime2, omembe):
    trditevresnicna = 1
    if ime1 not in set(omembe) or ime2 not in set(omembe):
        trditevresnicna = 0

    if trditevresnicna == 1:
        for imena1 in omembe[ime1]:
            if imena1 == ime2:
                return True
        for imena2 in omembe[ime2]:
            if imena2 == ime1:
                return True
    return False

