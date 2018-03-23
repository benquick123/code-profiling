# zacetek funkcij iz prejšnje naloge
# Ali se da te funkcije kako drugače uvoziti?
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
    return avtorji

def izloci_besedo(beseda):
    isci = re.search('((?!-)[\w-]+(\w))',beseda)
    return isci.group(0)                            

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

# konec funkcij iz prejsne naloge
import collections

def besedilo(tvit):
    return tvit.split(": ", 1)[1]

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti[::-1]:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    return collections.Counter(vsi_avtorji(tviti))

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        oznacene = se_zacne_z(tvit, "@")
        pisec = avtor(tvit)
        if pisec in slovar:
            slovar[pisec] += oznacene
        else:
            slovar[pisec] = oznacene
    return slovar

def neomembe(ime, omembe):
    osebe = []
    for d in omembe:
        if d != ime and d not in omembe[ime]:
            osebe.append(d)
    return osebe

def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe and ime2 in omembe:
        prva = omembe[ime1]
        druga = omembe[ime2]
        return (ime2 in prva or ime1 in druga)
    return False

def hashtagi(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        oznaka = se_zacne_z(tvit, "#")
        pisec = avtor(tvit)
        for tag in oznaka:
            if tag not in slovar:
                slovar[tag].append(pisec)
            else:
                slovar[tag].append(pisec)
    for d in slovar:
        slovar[d] = sorted(slovar[d])
    return slovar

