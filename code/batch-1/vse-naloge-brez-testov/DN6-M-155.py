import collections

def unikati(s):
    seznam = []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    return unikati([avtor(zapis) for zapis in tviti])

def izloci_besedo(beseda):
    return "".join(i for i in beseda if i.isalnum() or i == "-")

def se_zacne_z(tvit, c):
    return [izloci_besedo(i) for i in tvit.split() if i.startswith(c)]

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        seznam += se_zacne_z(tvit, c)
    return unikati(seznam)

def vse_afne(tviti):
    seznam = []
    for i in tviti:
        for j in i.split():
            if j.startswith("@"):
                seznam.append(izloci_besedo(j))
    return unikati(seznam)

def vsi_hashtagi(tviti):
    seznam = []
    for i in tviti:
        for j in i.split():
            if j.startswith("#"):
                seznam.append(izloci_besedo(j))
    return unikati(seznam)

def vse_osebe(tviti):
    seznam = []
    for tvit in tviti:
        seznam.append(avtor(tvit))
    seznam += vse_afne(tviti)
    return unikati(sorted(seznam))

def custva(tviti, hashtagi):
    seznam = []
    for tvit in tviti:
        for hash in hashtagi:
            if hash in tvit:
                seznam.append(avtor(tvit))
    return unikati(sorted(seznam))

def besedilo(tvit):
    seznam = tvit.split(':')[1:]
    return ":".join(seznam).strip()

def zadnji_tvit(tviti):
    zadnji_slovar = {}
    for tvit in tviti:
        avt, bes = avtor(tvit), besedilo(tvit)
        zadnji_slovar[avt] = bes
    return zadnji_slovar

def prvi_tvit(tviti):
    prvi_slovar = {}
    for tvit in tviti:
        avt, bes = avtor(tvit), besedilo(tvit)
        if avt not in prvi_slovar:
            prvi_slovar[avt] = bes
    return prvi_slovar

def prestej_tvite(tviti):
    return collections.Counter([avtor(tvit) for tvit in tviti])

def omembe(tviti):
    omembe_slovar = collections.defaultdict(list)
    for tvit in tviti:
        avt, bes = avtor(tvit), besedilo(tvit)
        omembe_slovar[avt] += vse_afne([bes]) # funkcija vse_afne zahteva seznam
    return omembe_slovar

def neomembe(ime, omembe):
    avt = set(omembe)
    avt.discard(ime)
    return list(avt - set(omembe[ime]))

def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe.get(ime2, []) or ime2 in omembe.get(ime1, []):
        return True
    else:
        return False

def hashtagi(tviti):
    slovar_hash = collections.defaultdict(list)
    for tvit in tviti:
        avt = avtor(tvit)
        hashtag = vsi_hashtagi([tvit])
        for hash in hashtag:
            slovar_hash[hash] += [avt]
    for hash, tag in slovar_hash.items():
        tag.sort()
        slovar_hash[hash] = tag
    return slovar_hash


