import collections

def besedilo(tvit):
    return tvit[tvit.index(":")+2:]             # + 2 ker me zanima od ": " naprej
                                                # return ": ".join(tvit.split(": ")[1:])

def avtor(tvit):
    return tvit[:tvit.index(":")]

def zadnji_tvit(tviti):
    return {avtor(tvit):besedilo(tvit) for tvit in tviti}

def prvi_tvit(tviti):
    d = collections.defaultdict(str)
    for tvit in tviti:
        avtor_t = avtor(tvit)
        if avtor_t not in d:                    # samo če še ga ni, ga dodamo
            d[avtor_t] = besedilo(tvit)
    return d


def prestej_tvite(tviti):
    return collections.Counter([avtor(tvit) for tvit in tviti])

def pomožna_funkcija1(beseda):
    for e in beseda:
        if e.isalnum():
            indeks = beseda.index(e)
            break
    return beseda[indeks:]


def izloci_besedo(beseda):
    beseda = pomožna_funkcija1(beseda)
    beseda = pomožna_funkcija1(beseda[::-1])
    return beseda[::-1]


def pomožna_funkcija2(tvit, c):
    return [izloci_besedo(e) for e in tvit.split() if e[0] == c]

def omembe(tviti):
    d = collections.defaultdict(list)
    for tvit in tviti:
        avtor_t = avtor(tvit)
        d[avtor_t].extend(pomožna_funkcija2(tvit, "@"))
    return d


def neomembe(ime, omembe):
    return [ključ for ključ in omembe if ključ != ime and ključ not in omembe[ime]]

def se_poznata(ime1, ime2, omembe):
    return any(True for ključ in omembe if (ključ == ime1 and ime2 in omembe[ime1]) or (ključ == ime2 and ime1 in omembe[ime2]))


def hashtagi(tviti):
    d = collections.defaultdict(list)
    for tvit in tviti:
        avtor_t = avtor(tvit)
        for beseda in tvit.split():
            if beseda[0] == "#":
                d[izloci_besedo(beseda)].append(avtor_t)
                d[izloci_besedo(beseda)].sort()
    return d
















