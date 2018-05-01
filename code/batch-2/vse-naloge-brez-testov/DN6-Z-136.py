def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    besede = []
    for beseda in tvit.split():
        if beseda[0] == c:
            besede.append(izloci_besedo(beseda))
    return besede

def besedilo(tvit):
    ime, bes = tvit.split(maxsplit=1)
    return bes

def zadnji_tvit(tviti):
    s = {}
    for tvi in tviti:
        s[tvi.split(":")[0]] = besedilo(tvi)
        for k in s:
            if s[k] in s.keys():
                del s[k]
    return s

def prvi_tvit(tviti):
    s = {}
    rezultat = {}
    for tvi in tviti:
        s[tvi.split(":")[0]] = besedilo(tvi)
        for k, v in s.items():
            if k not in rezultat.keys():
                rezultat[k] = v
    return rezultat

import collections
def prestej_tvite(tviti):
    s = []
    for tvit in tviti:
        ime = tvit.split(" ")[0][:-1]
        s.append(ime)
    pogostosti = collections.defaultdict(int)
    for ime in s:
        pogostosti[ime] += 1
    return pogostosti


def omembe(tviti):
    vrni = collections.defaultdict(list)
    for vrstica in tviti:
        sp = vrstica.split(" ")
        ime = sp[0][:-1]
        if not vrni[ime]:
            vrni[ime] = []
        for x in sp:
            if x.startswith("@"):
                vrni[ime].append(x.strip("@, ?"))
    return vrni

def neomembe(ime, omembe):
    seznam = []
    for oseba in omembe.keys():
        if oseba not in omembe[ime] and oseba != ime:
            seznam.append(oseba)
    return seznam



