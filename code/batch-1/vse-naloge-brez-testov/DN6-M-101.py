#FUNKCIJE IZ PREJŠNJE DOMAČE NALOGE:
#Unikati v seznamu:
def unikati(s):
    sez = []
    for i in s:
        if i not in sez:
            sez.append(i)
    return (sez)


#Avtor tvita:
def avtor (tvit):
    deli = tvit.split(":")
    return (deli[0])

#Vsi avotrji tvitov:
def vsi_avtorji(tvit):
    sez = []
    for i in tvit:
        deli = i.split(":")
        d = deli[0]
        if d not in sez:
            sez.append(d)
    return (sez)


#Izloči vse na začetku in kocu razen črk:
def izloci_besedo(beseda):
    for start, s in enumerate(beseda):
        if s.isalnum():
            break
    for end, s in enumerate(beseda[::-1]):
        if s.isalnum():
            break
    return (beseda[start:len(beseda) - end])


#Beseda se začne z:
def se_zacne_z(tvit, c):
    sez = []
    w = tvit.split()
    for i in w:
        if i[0] in c:
            n = izloci_besedo(i)
            sez.append(n)
    return (sez)


#Beseda se začne z:
def zberi_se_zacne_z(tviti, c):
    sez = []
    for i in tviti:
        w = i.split()
        for i in w:
            if i[0] in c:
                n = izloci_besedo(i)
                sez.append(n)
    #u =unikati(sez)
    return (sez)


#Beseda se začne z "@":
def vse_afne(tviti):
    o = zberi_se_zacne_z(tviti, "@")
    return (o)


#Beseda se začne z "#":
def vsi_hashtagi(tviti):
    o = zberi_se_zacne_z(tviti, "#")
    return (o)


#Vse osebe v tvitih:
def vse_osebe(tviti):
    a = vsi_avtorji(tviti) + vse_afne(tviti)
    u = unikati(a)
    s = sorted(u)
    return (s)





#FUNKCIJE ZA TO DOMAČO NALOGO:
#Besedilo po prvem ":":
def besedilo(tvit):
    deli = tvit.split(": ", 1)[1]
    return (deli)


#Zadni tvit v seznamu dodaj v slovar:
def zadnji_tvit(tviti):
    s = {}
    for i in tviti:
        deli = i.split(": ", 1)
        avtorji = deli[0]
        besedil = deli[1]
        s[avtorji] = besedil
    return (s)


#Prvi tvit v seznamu dodaj v slovar:
def prvi_tvit(tviti):
    s = {}
    for i in tviti:
        deli = i.split(": ", 1)
        avtorji = deli[0]
        besedil = deli[1]
        if avtorji not in s:
            s[avtorji] = besedil
    return (s)


#Preštej število tvitov avtorja:
def prestej_tvite(tviti):
    s = {}
    sez = []
    for i in tviti:
        deli = i.split(": ", 1)
        avtorji = deli[0]
        sez.append(avtorji)
    for bes in sez:
        if bes in s:
            s[bes] += 1
        else:
            s[bes] = 1
    return (s)


#Koga avtor omeni v tvitu ("@"):
def omembe(tviti):
    s = {}
    for i in tviti:
        deli = i.split(": ", 1)
        avtorji = deli[0]
        if avtorji not in s:
            s[avtorji] = []
        for o in i.split():
            if o[0] == "@" and izloci_besedo(o[0]) not in s[avtorji]:
                s[avtorji] += [izloci_besedo(o)]
    return (s)


#Koga avtor NEomeni v tivitu
def neomembe(ime, omembe):
    sez1 = []
    sez2 = omembe[ime]
    sez3 = []
    for a in omembe:
        sez1.append(a)
    for i in sez1:
        if i not in sez2 and i !=  ime:
            sez3.append(i)
    return (sez3)



#TESTI:
