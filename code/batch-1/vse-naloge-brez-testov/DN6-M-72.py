#FUNKCIJE IZ PREJŠNJE NALOGE

def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        imena.append(avtor(tvit))
    return unikati(imena)

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

def zberi_se_zacne_z(tviti, c):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, c)
    return unikati(afne)

def vse_afne(tviti):
    return unikati(zberi_se_zacne_z(tviti, "@"))

def vsi_hashtagi(tviti):
    return unikati(zberi_se_zacne_z(tviti, "#"))

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

#NOVA NALOGA

def besedilo(tvit):
    return tvit.split(": ", 1)[1]

def zadnji_tvit(tviti):
    d = {}
    for i in tviti:
        avtor = i.split(": ")[0]
        split_besedilo = besedilo(i)
        d[avtor] = split_besedilo
    return d

def prvi_tvit(tviti):
    d = {}
    for i in tviti:
        avtor = i.split(": ")[0]
        split_besedilo = besedilo(i)
        if avtor not in d:
            d[avtor] = split_besedilo
    return d

def prestej_tvite(tviti):
    d = {}
    for i in tviti:
        avtor = i.split(": ")[0]
        d[avtor] = d.get(avtor, 0) + 1
    return d

def omembe(tviti):
    d = {}
    for i in tviti:
        avtor = i.split(": ")[0]
        omemba = se_zacne_z(i, "@")
        if omemba != []:
            if avtor not in d:
                d[avtor] = omemba
            else:
                for i in omemba:
                    d[avtor].append(i)
        else:
            d[avtor] = []
    return d

def neomembe(ime, omembe):
    d = omembe
    omenjen = []
    neomenjen = []

    for element in d[ime]:
        omenjen.append(element)

    for o in omembe.keys():
        if o == ime:
            continue
        if o not in omenjen:
            neomenjen.append(o)

    return neomenjen

def se_poznata(ime1, ime2, omembe):
    d = omembe

    if ime1 in d:
        for element in d[ime1]:
            if element == ime2:
                return True
            else:
                continue
        else:
            if ime2 in d:
                for element2 in d[ime2]:
                    if element2 == ime1:
                        return True
                    else:
                        continue
    else:
        if ime2 in d:
            for element2 in d[ime2]:
                if element2 == ime1:
                    return True
                else:
                    continue
    return False

def hashtagi(tviti):
    d = {}

    for tvit in tviti:
        avtorcek = avtor(tvit)
        hastagic = se_zacne_z(tvit, "#")

        for hastag in hastagic:
            if hastag not in d:
                d[hastag] = avtorcek.split()
            else:
                d[hastag].append(avtorcek)

        for element in d:
            x = d[element]
            x = sorted(x)
            d[element] = x

    return d


#TESTI

