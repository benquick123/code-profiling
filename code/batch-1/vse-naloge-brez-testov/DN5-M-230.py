import re
def unikati(s):
    seznam = []
    for x in s:
        if not (x in seznam):
            seznam.append(x)
    return seznam

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)

def izloci_besedo(beseda):
    isci = re.search('((?!-)[\w-]+(\w))',beseda) # funkcijo sem se trudil narediti na tak način kot je opisana v nalogi a nisem zmogel
    return isci.group(0)                            # zato sem s pomočjo pythonove dokumentacije https://docs.python.org/2/library/re.html
                                                    # in strani regexr.com sestavil lažjo rešitev in jo uporabil.

def se_zacne_z(tvit, c):
    tvit = tvit.split()
    besede = []
    for beseda in tvit:
        if(beseda.startswith(c)):
            besede.append(izloci_besedo(beseda))
    return besede

def zberi_se_zacne_z(tviti, c):
    besede=[]
    beseda = [besede.extend(se_zacne_z(tvit, c)) for tvit in tviti]
    return unikati(besede)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    oznacene_osebe = vse_afne(tviti)
    avtorji = vsi_avtorji(tviti)
    osebe = unikati(oznacene_osebe + avtorji)
    return sorted(osebe)

def custva(tviti, hastagi):
    avtorji = []
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        if any("#"+a in tvit for a in hastagi) and avtor_tvita not in avtorji:
            avtorji += [avtor_tvita]
    return sorted(avtorji)

def se_poznata(tviti, oseba1, oseba2):
    oseba = vse_osebe(tviti)
    for tvit in tviti:
        oznaka = se_zacne_z(tvit, "@")
        avtor_t = avtor(tvit)
        if (oseba1 in oznaka and avtor_t == oseba2 or oseba2 in oznaka and avtor_t==oseba1):
            return True
    return False

