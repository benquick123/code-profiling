def unikati(s):
    xs = []
    for e in s:
        if e not in xs:
            xs.append(e)
    return xs
def avtor(tvit):
    i = 0
    for e in tvit:
        i += 1
        if e == ":":
            break
    return tvit[: i-1]
def vsi_avtorji(tviti):
    s = []
    for tvit in tviti:
        avto = avtor(tvit)
        if avto not in s:
            s.append(avto)
    return s
def izloci_besedo(beseda):
    if beseda.isalnum() == False:
        for e in beseda:
            if e.isalnum() == True:
                break
            elif e.isalnum() == False:
                beseda = beseda[1:]
        for e in beseda[::-1]:
            if e.isalnum() == True:
                break
            elif e.isalnum() == False:
                beseda = beseda[:-1]
    else:
        return beseda
    return beseda

def se_zacne_z(tvit, c):
    s = tvit.split()
    xs = []
    for e in s:
        if c == e[0]:
            e = izloci_besedo(e)
            xs.append(e)
    return xs
def zberi_se_zacne_z(tviti, c):
    seznam = []
    for e in tviti:
        rez = se_zacne_z(e, c)
        for f in rez:
            if f not in seznam:
                seznam.append(f)
    return seznam
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    avtorji = vsi_avtorji(tviti)
    omenjeni = vse_afne(tviti)
    sez = []
    for e in avtorji:
        if e not in sez:
            sez.append(e)
    for f in omenjeni:
        if f not in sez:
            sez.append(f)
    sez.sort()
    return sez

def custva(tviti, hashtagi):
    s = []
    avto = ''
    for tvit in tviti:
        for e in hashtagi:
            if e in tvit:
                avto = avtor(tvit)
                if avto not in s:
                    s.append(avto)
    s.sort()
    return s

def se_poznata(tviti, oseba1, oseba2):
    c = custva(tviti, [oseba1])
    for tvit in tviti:
        ime = avtor(tvit)
        if ime == oseba1 and ("@"+oseba2) in tvit:
            return True
    return False

