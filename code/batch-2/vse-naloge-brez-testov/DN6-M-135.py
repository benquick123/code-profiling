import collections
def unikati(s):
    sez = []
    for x in s:
        if x not in sez:
            sez.append(x)
    return sez
def avtor(tvit):
    a = ""
    for x in range(len(tvit)):
        if tvit[x] == ":":
            break
        else:
            a += tvit[x]
    return a
def izloci_besedo(beseda):
    beseda_1 = ""
    for x in range(len(beseda)):
        if beseda[x].isalnum() == True:
            beseda_1 += beseda[x]
        elif beseda[x] == "-" and beseda[x-1].isalnum() == True and beseda[x+1].isalnum() == True:
            beseda_1 += beseda[x]
    return beseda_1
def vsi_avtorji(tviti):
    sez = []
    for x in tviti:
        avtor_ime = avtor(x)
        if avtor_ime not in sez:
            sez.append(avtor_ime)
    return sez

def se_zacne_z(tvit, c):
    sez = tvit.split()
    sez_besed = []
    for x in sez:
        if x[0] == c:
            if x[-1].isalnum() == True:
                sez_besed.append(x[1:])
            else:
                sez_besed.append(x[1:-1])
    return sez_besed

def vse_afne(tviti):
    sez_imen = []
    for x in tviti:
        besede = x.split()
        for x in besede:
            if x[0] == "@":
                if x[-1].isalnum() == True:
                    if x[1:] not in sez_imen:
                        sez_imen.append(x[1:])
                else:
                    if x[1:-1] not in sez_imen:
                        sez_imen.append(x[1:-1])
    return sez_imen
def vse_osebe(tviti):
    sez = vse_afne(tviti)
    sez_imen = vsi_avtorji(tviti)
    n = 0
    for x in range(len(sez)):
        if sez[n] not in sez_imen:
            sez_imen.append(sez[n])
        n += 1
    sez = sorted(sez_imen)
    return sez

def vsi_hashtagi(tviti):
    sez = []
    for x in tviti:
        besede = x.split()
        for x in besede:
            if x[0] == "#":
                if x[-1].isalnum() == True:
                    if x[1:] not in sez:
                        sez.append(x[1:])
                else:
                    if x[1:-1] not in sez:
                        sez.append(x[1:-1])
    return sez
def zberi_se_zacne_z(tviti, c):
    sez_besed = []
    for x in tviti:
        sez = x.split()
        for x in sez:
            if x[0] == c:
                if x[-1].isalnum() == True:
                    if x[1:] not in sez_besed:
                        sez_besed.append(x[1:])
                else:
                    if x[1:-1] not in sez_besed:
                        sez_besed.append(x[1:-1])
    return sez_besed
def custva(tviti, hashtagi):
    sez_imen = []
    for x in tviti:
        sez = x.split()
        avtor = sez[0][:-1]
        for x in sez:
            if x[0] == "#":
                if x[1:] in hashtagi and avtor not in sez_imen:
                    sez_imen.append(avtor)
    return sorted(sez_imen)

def se_poznata(tviti, oseba1, oseba2):
    zakljucek = False
    sez = [oseba1, oseba2]
    for x in sez:
        for y in tviti:
            besede = y.split()
            for s in besede:
                sez_besed = []
                if s[0] == "@":
                    if besede[0][:-1] == x:
                        if s[-1].isalnum() == True:
                            if s[1:] not in sez_besed:
                                sez_besed.append(s[1:])
                        else:
                            if s[1:-1] not in sez_besed:
                                sez_besed.append(s[1:-1])
                        for d in sez_besed:
                            if x == oseba1:
                                if oseba2 in sez_besed:
                                    zakljucek = True
                            else:
                                if oseba1 in sez_besed:
                                    zakljucek = True
    return zakljucek
def besedilo(tvit):
    a = ""
    b = 0
    c = 0
    for x in range(len(tvit)):
        if tvit[x] == " " and c == 0:
            c = 1
            continue
        if b == 1 :
            a += tvit[x]
        if tvit[x]== ":":
            b = 1
    return a
def zadnji_tvit(tviti):
    slovar = {}
    for x in tviti:
        ime = avtor(x)
        besedilo1 = besedilo(x)
        if ime in slovar:
            slovar[ime] = besedilo1
        else:
            slovar[ime] = besedilo1
    return slovar
def prvi_tvit(tviti):
    slovar = {}
    for x in tviti:
        ime = avtor(x)
        besedilo1 = besedilo(x)
        if ime not in slovar:
            slovar[ime] = besedilo1
    return slovar
def prestej_tvite(tviti):
    slovar = {}
    for x in tviti:
        ime = avtor(x)
        if ime not in slovar:
            slovar[ime] = 0
        slovar[ime] += 1
    return slovar
def omembe(tviti):
    slovar = {}
    c = "@"
    for x in tviti:
        ime = avtor(x)
        v = se_zacne_z(x,c)
        if ime not in slovar:
            slovar[ime] = v
        else:
            for y in v:
                slovar[ime].append(y)
    return slovar
def neomembe(ime, omembe):
    sez_imen = []
    sez_omenjenih = []
    sez_neomenjenih = []
    for x in omembe:
        if x not in sez_imen:
            sez_imen.append(x)
    for x in omembe:
        if x == ime:
            for u in omembe[x]:
                sez_omenjenih.append(u)
    for x in sez_imen:
        if x == ime:
            continue
        else:
            if x in sez_omenjenih:
                continue
            else:
                sez_neomenjenih.append(x)
    return sez_neomenjenih
