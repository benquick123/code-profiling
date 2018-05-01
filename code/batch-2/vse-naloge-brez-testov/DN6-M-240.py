def unikati(s):
    tab = []
    i = 0
    j = 0
    while i < len(s):
        j = 0
        vsebuje = False
        while j < len(tab):
            if s[i] == tab[j]:
                vsebuje = True
            j = j + 1
        if vsebuje == False:
            tab.append(s[i])
        i = i + 1

    return tab

def avtor(tvit):
    znaki = list(tvit)
    i = 0
    while i < len(znaki):
        if znaki[i] == ":":
            break
        i = i + 1

    tab = []
    j = 0
    while j < i:
        tab.append(znaki[j])
        j = j + 1

    avtor = "".join(tab)

    return avtor

def vsi_avtorji(tviti):
    avtorji = []
    i = 0
    while i < len(tviti):
        x = avtor(tviti[i])
        avtorji.append(x)
        i = i + 1

    avtorji = unikati(avtorji)

    return avtorji


def izloci_besedo(beseda):
    tab = list(beseda)
    i = 0
    while i < len(beseda):
        if tab[i].isalnum() == 1:
            break
        i = i + 1

    j = len(beseda) - 1
    while j > 0:
        if tab[j].isalnum() == 1:
            break
        j = j - 1

    tab2 = []

    while i <= j:
        tab2.append(tab[i])
        i = i + 1

    return "".join(tab2)

def se_zacne_z(tvit, c):
    tab1 = tvit.split()
    tab2 = []
    i = 0
    while i < len(tab1):
        beseda = list(tab1[i])
        if beseda[0] == c:
            tab2.append(tab1[i])
        i = i + 1


    besede = []
    j = 0
    while j < len(tab2):
        besede.append(izloci_besedo(tab2[j]))
        j = j + 1

    return besede

def zberi_se_zacne_z(tviti, c):
    i = 0
    besede = []
    while i < len(tviti):
        besede = list(besede) + list(se_zacne_z(tviti[i], c))
        i = i +1

    return unikati(besede)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    tab = list(vsi_avtorji(tviti))+list(vse_afne(tviti))
    return sorted(unikati(tab), key=str.lower)


#----------------------------------------------------------------------------

def besedilo(tvit):
    znaki = list(tvit)
    tab = []
    stevec = 0

    while stevec < len(znaki):
        if znaki[stevec] == ":":
            break
        stevec = stevec + 1

    stevec = stevec + 2

    while stevec < len(znaki):
        tab.append(znaki[stevec])
        stevec = stevec + 1

    return "".join(tab)

def zadnji_tvit(tviti):
    slovar = {}
    stevec = 0
    while stevec < len(tviti):
        slovar[avtor(tviti[stevec])] = besedilo(tviti[stevec])
        stevec = stevec + 1
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    stevec = 0
    while stevec < len(tviti):
        if avtor(tviti[stevec]) not in slovar:
            slovar[avtor(tviti[stevec])] = besedilo(tviti[stevec])
        stevec = stevec + 1
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    stevec = 0
    while stevec < len(tviti):
        if avtor(tviti[stevec]) in slovar:
            slovar[avtor(tviti[stevec])] = slovar[avtor(tviti[stevec])]+1
        else:
            slovar[avtor(tviti[stevec])] = 1
        stevec = stevec + 1
    return slovar

def vse_omembe_od_osebe(tviti, oseba):
    tab = []
    a = 0
    while a < len(tviti):
        if avtor(tviti[a]) == oseba:
            tab.append(besedilo(tviti[a]))
        a = a + 1
    return vse_afne(tab)

def omembe(tviti):
    slovar = {}
    a = 0
    while a < len(tviti):
        if avtor(tviti[a]) not in slovar:
            slovar[avtor(tviti[a])] = vse_omembe_od_osebe(tviti, avtor(tviti[a]))
        a = a + 1
    return slovar

def avtorji_omemb(slovar):
    return list(slovar.keys())

def neomembe(ime, omembe):
    tab1 = omembe[ime]
    tab1.append(ime)
    tab2 = avtorji_omemb(omembe)
    tab3 = []
    for x in tab2:
        if x not in tab1:
            tab3.append(x)
    return tab3




































