#prejšnja domača naloga
def unikati(s):
    seznamNov = []
    for e in s:
        if e not in seznamNov:
            seznamNov.append(e)
    return seznamNov

def avtor(tvit):
    return tvit.split(':')[0]

def izloci_besedo(beseda):
    for i in range(len(beseda)):
        if beseda[i].isalnum():
            start = i
            break
    for i in range(len(beseda)):
        if beseda[(len(beseda)-1)-i].isalnum():
            end = i
            break
    if end == 0:
        return beseda[start:]
    else:
        return beseda[start:-end]

def se_zacne_z(tvit, c):
    novSeznam = []
    for rijec in tvit.split(' '):
        if rijec[0] == c:
            novSeznam.append(izloci_besedo(rijec))
    return novSeznam

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        rijec = se_zacne_z(tvit, c)
        seznam.extend(rijec)
    return unikati(seznam)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

#####nova naloga#########

def besedilo(tvit):
   for i in range(len(tvit)):
       if tvit[i] == ':':
           start = i+2
           break
   return tvit[start:]

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
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = 1
        else:
            slovar[avtor(tvit)]+=1
    return slovar

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
       oseba1 = avtor(tvit)
       omenjeni = se_zacne_z(tvit, '@')
       if oseba1 not in slovar:
           slovar[oseba1] = []
           slovar[oseba1].extend(omenjeni)
       else:
           slovar[oseba1].extend(omenjeni)
    return slovar

def neomembe(ime, omembe):
    seznam = []
    for key, value in omembe.items():
        if key != ime:
            seznam.append(key)
    for i in omembe[ime]:
        if i in seznam:
            seznam.remove(i)
    return seznam

def se_poznata(ime1, ime2, omembe):
    for key, value in omembe.items():
        if ime1 == key and ime2 in omembe[key] or \
            ime2 == key and ime1 in omembe[key]:
            return True
    return False

def hashtagi(tviti):
    slovar = {}
    seznam = vsi_hashtagi(tviti)
    for i in range(len(seznam)):
        slovar[seznam[i]] = []
        for tvit in tviti:
            if seznam[i] in besedilo(tvit):
                slovar[seznam[i]].append(avtor(tvit))
    for i in range(len(seznam)):
        slovar[seznam[i]].sort(key=str.lower)
    return slovar

