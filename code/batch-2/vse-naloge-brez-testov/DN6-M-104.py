# Ni iz te naloge
def avtor(tvit):
    seznam = tvit.split(":")
    return seznam[0]

def besedilo(tvit):
    izpis = len(avtor(tvit))
    return tvit[izpis + 2:]

# Ni iz te naloge
def avtor(tvit):
    seznam = tvit.split(":")
    return seznam[0]

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for i in tviti:
        if avtor(i) not in slovar:
            slovar[avtor(i)] = 1
        elif avtor(i) in slovar:
            slovar[avtor(i)] += 1
    return slovar

# Ni iz te naloge
def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

#Ni iz te naloge
def se_zacne_z(tvit, c):
    besede = []
    for beseda in tvit.split():
        if beseda[0] == c:
            besede.append(izloci_besedo(beseda))
    return besede

def omembe(tviti):
    izpis = {}
    for tvit in tviti:
        if avtor(tvit) not in izpis:
            izpis[avtor(tvit)] = se_zacne_z(tvit, "@")
        elif avtor(tvit) in izpis:
            izpis[avtor(tvit)] += se_zacne_z(tvit, "@")
    return izpis

def neomembe(ime, omembe):
    vsi = []
    for tvit in omembe:
        vsi.append(avtor(tvit))
    rezultat = [item for item in vsi if (item not in omembe[ime] and item != ime)]
    return rezultat

"""=================================================================================="""

