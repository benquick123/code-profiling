def vse_osebe(tvit, znak):
    besede = []
    for beseda in tvit.split():
        if beseda[0] == znak:
            for prva in range(len(beseda)):
                if beseda[prva].isalnum():
                    break
                for zadnja in range(len(beseda), 0, -1):
                    if beseda[zadnja-1].isalnum():
                        break
            besede.append(beseda[prva:zadnja])
    return besede
 
def besedilo(tvit):
    for _ in tvit:
        tvit = tvit.replace(_, '', 1)
        if _ == ':':
            break
    return tvit.strip(' ')

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        seznam = tvit.split(':')
        slovar[seznam[0]] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        seznam = tvit.split(':')
        if seznam[0] not in slovar:
            slovar[seznam[0]] = besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        seznam = tvit.split(':')
        if seznam[0] not in slovar:
            slovar[seznam[0]] = 0
        slovar[seznam[0]] += 1
    return slovar

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        seznam = tvit.split(':')
        
        if seznam[0] not in slovar:
            slovar[seznam[0]] = []
        slovar[seznam[0]] += vse_osebe(tvit, '@')
    return slovar

def neomembe(ime, omembe):
    seznam = []
    for osebe in omembe:
        if osebe not in omembe[ime] and ime != osebe:
            seznam.append(osebe)
    return seznam

def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe and ime2 in omembe:
        if ime1 in omembe[ime2] or ime2 in omembe[ime1]:
            return True
    else:
        return False

def hashtagi(tviti):
    slovar = {}
    for tvit in tviti:
        seznam = tvit.split(':')
        oseba = seznam[0]
        hashtag = vse_osebe(tvit, '#')
        for _ in hashtag:
            if _ not in slovar:
                slovar[_] = []
            slovar[_].append(oseba)
            slovar[_] = sorted(slovar[_])
    return slovar
    
