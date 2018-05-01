def avtor(tvit):
    return tvit.split(":")[0]

def izloci_besedo(beseda):
    print(beseda)
    for i in range(len(beseda)):
        if beseda[i].isalnum():
            beseda = beseda[i:]
            break
    for i in range(len(beseda)-1, 0, -1):
        if beseda[i].isalnum():
            beseda = beseda[:i+1]
            break
    return beseda




def besedilo(tvit):
    return tvit.split(": ", 1)[1]

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        avtor_ = avtor(tvit)
        slovar[avtor_] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        avtor_ = avtor(tvit)
        if avtor_ not in slovar:
            slovar[avtor_] = besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        avtor_ = avtor(tvit)
        if avtor_ not in slovar:
            slovar[avtor_] = 0
        slovar[avtor_] += 1
    return slovar

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        avtor_ = avtor(tvit)
        slovar[avtor_] = []

    for tvit in tviti:
        avtor_ = avtor(tvit)
        besedilo_ = besedilo(tvit)
        besede = besedilo_.split()
        for beseda in besede:
            if beseda.startswith("@") and beseda not in slovar[avtor_]:
                print("appending:", izloci_besedo(beseda))
                slovar[avtor_].append(izloci_besedo(beseda))
    print(dict(slovar))
    return dict(slovar)

def neomembe(ime, omembe):
    seznam = []

    for avtor1 in omembe.keys():
        if avtor1 != ime:
            continue
        for avtor2 in omembe.keys():
            if avtor2 != avtor1 and avtor2 not in omembe[avtor1]:
                seznam.append(avtor2)
    return seznam

def se_poznata(ime1, ime2, omembe):
    for avtor in omembe.keys():
        if avtor == ime1 and ime2 in omembe[avtor]:
            return True
        if avtor == ime2 and ime1 in omembe[avtor]:
            return True
    return False

def hashtagi(tviti):
    slovar = {}
    for tvit in tviti:
        besedilo_ = besedilo(tvit)
        besede = besedilo_.split()
        for beseda in besede:
            if beseda.startswith("#"):
                slovar[izloci_besedo(beseda)] = []

    for tvit in tviti:
        avtor_ = avtor(tvit)
        besedilo_ = besedilo(tvit)
        besede = besedilo_.split()
        for beseda in besede:
            if beseda.startswith("#"):
                slovar[izloci_besedo(beseda)].append(avtor_)

    for hashtag in slovar.keys():
        slovar[hashtag].sort()
    return slovar

