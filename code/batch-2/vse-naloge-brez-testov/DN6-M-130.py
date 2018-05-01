def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    return unikati(map(avtor, tviti))

def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def izloci_besedo(beseda):
    for prva in range(len(beseda)):
        if beseda[prva].isalnum():
            break
    for zadnja in range(len(beseda), 0, -1):
        if beseda[zadnja-1].isalnum():
            break
    return beseda[prva:zadnja]

def se_zacne_z(tvit, c):
    return [izloci_besedo(beseda) for beseda in tvit.split() if beseda[0] == c]

def zberi_se_zacne_z(tviti, c):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, c)
    return unikati(afne)

def vsi_hashtagi(tviti):
    return unikati(zberi_se_zacne_z(tviti, "#"))

def besedilo(tvit):
    s = tvit.split()
    del s[0]
    s = " ".join(s)
    return s

def zadnji_tvit(tviti):
    seznam_tvitov = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        seznam_tvitov[avtor1] = besedilo(tvit)
    return seznam_tvitov

def prvi_tvit(tviti):
    seznam_tvitov = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        if seznam_tvitov.get(avtor1, 1) == 1:
            seznam_tvitov[avtor1] = besedilo(tvit)
    return seznam_tvitov

def prestej_tvite(tviti):
    seznam_tvitov = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        if seznam_tvitov.get(avtor1, 0) == 0:
            seznam_tvitov[avtor1] = 1
        else:
            seznam_tvitov[avtor1] += 1
    return seznam_tvitov

def omembe(tviti):
    seznam_tvitov = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        if seznam_tvitov.get(avtor1, 0) == 0:
            seznam_tvitov[avtor1] = se_zacne_z(tvit, "@")
        else:
            seznam_tvitov[avtor1] += se_zacne_z(tvit, "@")
    return seznam_tvitov

def neomembe(ime,omembe):
    seznam_oseb = []
    for avtor in omembe:
        seznam_oseb.append(avtor)
    for oseba in omembe[ime]:
        if oseba in seznam_oseb:
            seznam_oseb.remove(oseba)
    seznam_oseb.remove(ime)


    return seznam_oseb

def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe and ime2 in omembe:
        for ime in omembe[ime1]:
            if ime == ime2:
                return True

        for ime in omembe[ime2]:
            if ime == ime1:
                return True
        else:
            return False






