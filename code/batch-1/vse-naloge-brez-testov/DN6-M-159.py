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
    seznam_avtorjev = []
    for tvit in tviti:
        avt = avtor(tvit) # avt - v to spremenljivko se shrani trenutni avtor
        if avt not in seznam_avtorjev:
            seznam_avtorjev.append(avt)
    return seznam_avtorjev

def izloci_besedo(beseda):
    while True:
        if not beseda[0].isalnum():
            beseda = beseda[1:]
        else:
            break

    while True:
        if not beseda[-1].isalnum():
            beseda = beseda[:-1]
        else:
            break

    return beseda

def se_zacne_z(tvit, c):
    beseda = ""
    seznam = []
    pisi = False
    for z in tvit:
        if c == z:
            pisi = True
            continue
        if pisi and z.isalnum():
            beseda = beseda + z
        elif pisi:
            seznam.append(beseda)
            pisi = False
            beseda = ""
    if beseda != "":
        seznam.append(beseda)

    return seznam

def zberi_se_zacne_z(tviti, c):
    f = []
    for tvit in tviti:
        a = se_zacne_z(tvit, c)
        f.extend(a)
    f = unikati(f)
    return f

def vse_afne(tviti):    # vrne vse označbe iz vseh tvitov
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    seznam = vsi_avtorji(tviti)
    seznam.extend(vse_afne(tviti))
    seznam = sorted(unikati(seznam))
    return seznam

def custva(tviti, hashtagi):
    seznam = []
    for tvit in tviti:
        avt = avtor(tvit)
        hash = se_zacne_z(tvit, "#")
        for h in hash:
            if h in hashtagi:
                seznam.append(avt)
    seznam = sorted(unikati(seznam))
    return seznam

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        avt = avtor(tvit)
        afna = se_zacne_z(tvit, "@")
        for a in afna:
            if oseba1 == avt and oseba2 == a:
                return True
            elif oseba2 == avt and oseba1 == a:
                return True

    return False

#############################

def split_tvit(tvit):
    return tvit.split(": ", 1)

def get_key(tvit):
    return split_tvit(tvit)[0]

def get_afne(tvit): ##afne iz enega tvita
    return se_zacne_z(tvit, "@")

def get_hashi(tvit): ##hashi iz enega tvita
    return se_zacne_z(tvit, "#")


#############################

def besedilo(tvit):
    return split_tvit(tvit)[1]

def zadnji_tvit(tviti):
    zadnji = collections.defaultdict(str)
    for tvit in tviti:
        key = get_key(tvit)
        text = besedilo(tvit)
        zadnji[key] = text
    return zadnji

def prvi_tvit(tviti):
    prvi = collections.defaultdict(str)
    for tvit in tviti:
        key = get_key(tvit)
        text = besedilo(tvit)
        if not prvi[key]:
            prvi[key] = text
    return prvi

def prestej_tvite(tviti):
    slovar = collections.defaultdict(int)
    for tvit in tviti:
        key = get_key(tvit)
        slovar[key] += 1
    return slovar

def omembe(tviti):
    omembice = collections.defaultdict(list)
    for tvit in tviti:
        key = get_key(tvit)
        # za trenutni tvit pridobi vse označbe (afne) v seznam
        afne = get_afne(tvit)
        # seznam omenjenih besed (unikati)
        omembice[key].extend(afne)
        omembice[key] = unikati(omembice[key])
    return omembice

def neomembe(ime, omembe):
    avtorji = []
    for key, omenjeni in omembe.items():  # omenjeni - seznam
        if key != ime and key not in omembe[ime]:  # vse seznam shranimo avtorje, ki niso 'ime', in jih oseba 'ime' ni omenila
            avtorji.append(key)
    return avtorji

def se_poznata(ime1, ime2, omembe):
    for key, omenjeni in omembe.items():
        if ime1 == key and ime2 in omenjeni:
            return True
        if ime2 == key and ime1 in omenjeni:
            return True
    return False

def avtorji_hash(hash, tviti):  # vrne seznam avtorjev, ki so uporabili določen hash
    avtorji = []
    for tvit in tviti:
        hashi_tvit = get_hashi(tvit)  # seznam hashov
        if hash in hashi_tvit:
            avtorji.append(avtor(tvit))
    avtorji = unikati(avtorji)
    return avtorji

def hashtagi(tviti):
    slovar = collections.defaultdict(list)
    hashi = vsi_hashtagi(tviti)
    for hash in hashi:
        # kliči funkcijo, ki vrne seznam, v katerega se shranijo avtorji, ki so uporabili ta hash.
        slovar[hash].extend(sorted(avtorji_hash(hash, tviti)))
    return slovar

