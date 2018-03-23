def besedilo(tvit):
    ind = tvit.find(":")
    return tvit[ind+2:]

def zadnji_tvit(tviti):
    slovar = {}
    for el in tviti:
        slovar[el.split(":")[0]] = besedilo(el)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for el in tviti:
        if not el.split(":")[0] in slovar:
            slovar[el.split(":")[0]] = besedilo(el)
    return slovar

def prestej_tvite(tviti):
    x = 0
    slovar = {}
    for el in tviti:
        if not el.split(":")[0] in slovar:
            slovar[el.split(":")[0]] = 1
        else:
            slovar[el.split(":")[0]] += 1
    return slovar

def izloci_besedo(beseda):
    i = 0
    while beseda[i].isalnum() == False:
        beseda = beseda[1:]
    i = len(beseda)-1
    while i >= 0 and beseda[i].isalnum() == False:
        beseda = beseda[:-1]
        i -= 1
    return beseda

def omembe(tviti):
    slovar = {}
    for el in tviti:
        slovar[el.split(":")[0]] = []
    for el in tviti:
        temp = el[el.find(":")+1:].split(" ")
        for e in temp:
            if e != "":
                if e[0] == "@":
                    slovar[el.split(":")[0]].append(izloci_besedo(e))
    return slovar

def neomembe(ime, omembe):
    vsi = []
    seznam = []
    for el in omembe:
        vsi.append(el)
    for el in vsi:
        if el != ime and el not in omembe[ime]:
            seznam.append(el)
    return seznam

def se_poznata(ime1, ime2, omembe):
    om1 = []
    om2 = []
    if ime1 in omembe:
        om1 = omembe[ime1]
    if ime2 in omembe:
        om2 = omembe[ime2]
    if om2 != []:
        if ime1 in om2:
            return True
    if om1 != []:
        if ime2 in om1:
            return True
    return False

def hashtagi(tviti):
    slovar = {}
    for el in tviti:
        temp = el[el.find(":") + 1:].split(" ")
        for e in temp:
            if e != "":
                if e[0] == "#":
                    slovar[izloci_besedo(e)] = []
    for kljuc in slovar:
        for el in tviti:
            if "#"+kljuc in el:
                slovar[kljuc].append(el.split(":")[0])
    for kljuc in slovar:
        slovar[kljuc] = sorted(slovar[kljuc])
    return slovar





