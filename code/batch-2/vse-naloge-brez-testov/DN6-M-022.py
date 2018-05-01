import collections

def unikati(s):
    return [x for i, x in enumerate(s) if x not in s[0:i]]

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    return [avtor(x) for x in tviti]

def izloci_besedo(beseda):
    while not beseda[0].isalnum(): 
        beseda = beseda[1:]
    while not beseda[-1].isalnum(): 
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    return [izloci_besedo(i) for i in tvit.split() if i [0] == c]
  
def zberi_se_zacne_z(tviti, c):
    return unikati(sum([se_zacne_z(x, c) for x in tviti], []))

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")
 
def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

def vsi_hashtagi(tviti):
    return unikati(zberi_se_zacne_z(tviti, "#"))

# Funkcije tviti 2.

# Obvezne naloge:

def besedilo(tvit):
    len_avtor = len(avtor(tvit))
    return tvit[len_avtor + 2:]

def zadnji_tvit(tviti):
    a = {}
    for i in tviti:
        a[avtor(i)] = besedilo(i)
    return a

def prvi_tvit(tviti):
    a = {}
    for i in tviti:
        if avtor(i) not in a:
            a[avtor(i)] = besedilo(i)
    return a

def prestej_tvite(tviti):
    return collections.Counter(vsi_avtorji(tviti))

def omembe(tviti):
    a = {}
    for i in tviti:
        if avtor(i) not in a:
            a[avtor(i)] = [izloci_besedo(x) for x in besedilo(i).split() if izloci_besedo(x) in vse_afne(tviti)]
        else:
            a[avtor(i)] += [izloci_besedo(x) for x in besedilo(i).split() if izloci_besedo(x) in vse_afne(tviti)]
    return a

def neomembe(ime, omembe):
    a = []
    if ime in omembe.keys():
        for i in omembe:
            if i not in omembe[ime] and i != ime:
                a.append(i)
    return a

# Dodatne naloge:

def se_poznata(ime1, ime2, omembe):
    for i in omembe:
        if i == ime1 and ime2 in omembe[i] or i == ime2 and ime1 in omembe[i]:
            return True
    return False

def hashtagi(tviti):
    a = {}
    for i in vsi_hashtagi(tviti):
        if i not in a:
            a[i] = [avtor(x) for x in tviti if i in x]
        else:
            a[i] += [avtor(x) for x in tviti if i in x]
    for key in a:
        a[key] = sorted(a[key])
    return a

