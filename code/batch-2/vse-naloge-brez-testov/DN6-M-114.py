import collections

def besedilo(tvit):
    return tvit[tvit.index(':') + 2 : ]

def zadnji_tvit(tviti):
    return {avtor(x): besedilo(x) for x in tviti}

def avtor(tvit):
    return tvit.split(':')[0]

def prvi_tvit(tviti):
    slovar = collections.defaultdict(str)
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    return collections.Counter(avtor(x) for x in tviti)

def omembe(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        slovar[avtor(tvit)].extend(seznam_omenjenih(tvit))
    return slovar

def seznam_omenjenih(tvit):
    return [izloci_besedo(x) for x in tvit.split() if x[0] == '@' ]

def izloci_besedo(beseda):
   while not beseda[0].isalnum():
       beseda = beseda[1:]
   while not beseda[-1].isalnum():
       beseda = beseda[:-1]
   return beseda

def neomembe(ime, omembe):
    return list(set(omembe.keys()) - set(omembe[ime]) - set([ime]))

def se_poznata(ime1, ime2, omembe):
    if omembe.get(ime2, 0):
        if ime1 in omembe[ime2]:
            return True
    if omembe.get(ime1,0):
        if ime2 in omembe[ime1]:
            return True
    return False

def hashtagi(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        ime = avtor(tvit)
        for hashtag in [izloci_besedo(x) for x in tvit.split() if x[0] == '#']  :
            slovar[hashtag].append(ime)
    for x in slovar:
        slovar[x] = sorted(slovar[x])
    return slovar




























