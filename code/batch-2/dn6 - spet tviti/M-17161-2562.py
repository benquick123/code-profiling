#Funkcije iz naloge tviti

# Obvezni del
def unikati(s):
    nov = []
    for el in s:
        if el not in nov:
            nov.append(el)
    return nov

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    seznam_avotrjev = []
    for vrstica in tviti:
        seznam_avotrjev.append(avtor(vrstica))
    return unikati(seznam_avotrjev)

def izloci_besedo(beseda):
    for c in beseda:
        if c.isalnum():
            break
        else:
            beseda = beseda[1:]
    beseda = beseda[::-1]
    for c2 in beseda:
        if c2.isalnum():
            break
        else:
            beseda = beseda[1:]
    return beseda[::-1]

def se_zacne_z(tvit, c):
    nove = []
    for cha in tvit.split(" "):
        if cha.startswith(c):
            nove.append(izloci_besedo(cha))
    return nove

def zberi_se_zacne_z(tviti, c):
    nov = []
    for a in tviti:
        n = se_zacne_z(a,c)
        if n:
            for p in n: nov.append(p)
    return unikati(nov)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    osebe = zberi_se_zacne_z(tviti,"@")
    osebe2 = vsi_avtorji(tviti)
    vse = unikati(osebe + osebe2)
    return sorted(vse)

# Dodatna naloga
def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        avt = avtor(tvit)
        for t in tvit.split(" "):
            if izloci_besedo(t) in hashtagi:
                avtorji.append(avt)
    return unikati(sorted(avtorji))

def se_poznata(tviti, oseba1, oseba2):
    r = False
    for tv in tviti:
        avt = avtor(tv)
        if avt == oseba1:
            for i in tv.split(" "):
                if izloci_besedo(i) == oseba2 and i.startswith("@"):
                    r = True
    return r

#------------------------------------------

#Obvezne naloge
def besedilo(tvit):
    c = 0
    for znak in tvit:
        c += 1
        if znak == ":":
            return tvit[c:].strip()

def zadnji_tvit(tviti):
    tvit = {}
    for tv in tviti:
        tvit[avtor(tv)] = besedilo(tv)
    return tvit

def prvi_tvit(tviti):
    tvit = {}
    for tv in tviti:
        if avtor(tv) not in tvit.keys():
            tvit[avtor(tv)] = besedilo(tv)
    return tvit

def prestej_tvite(tviti):
    d = {}
    vsi = vsi_avtorji(tviti)
    for av in vsi:
        d[av] = 0
    for tv in tviti:
        d[avtor(tv)] += 1
    return d

def omembe(tviti):
    d = {}
    vsi = vsi_avtorji(tviti)
    for i in vsi:
        d[i] = []
    for tv in tviti:
        if se_zacne_z(tv, "@"):
            kat = se_zacne_z(tv,"@")
            for i in kat:
                d[avtor(tv)].append(i)
    return d

def neomembe(ime, omembe):
    s = []
    osebe = omembe[ime]
    for i,o in omembe.items():
        if i not in osebe and i != ime:
            s.append(i)
    return s

#Dodatne naloge
def se_poznata(ime1, ime2, omembe):
    r = False
    for av,kdo in omembe.items():
        if av == ime1:
            if ime2 in kdo:
                r = True
        if av == ime2:
            if ime1 in kdo:
                r = True
    return r

def hashtagi(tviti):
    d = {}
    vsi = vsi_hashtagi(tviti)
    for i in vsi:
        d[i] = []
    for vrs in tviti:
        av,tv = vrs.split(":")
        for i in tv.split(" "):
            if i.startswith("#"):
                d[izloci_besedo(i)].append(av)
    for k,v in d.items():
        d[k] = sorted(v)
    return d

