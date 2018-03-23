def unikati(s):
    seznam = []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

def avtor(tvit):
    author, x = tvit.split(":", 1)
    return author

def vsi_avtorji(tviti):
    seznam = []
    for i in tviti:
        x = avtor(i)
        if x not in seznam:
            seznam.append(x)
    return seznam

def izloci_besedo(beseda):
    if not beseda.isalnum():
        for znak in beseda:
            if znak.isalnum():
                break
            else:
                beseda = beseda.replace(znak, '')

        for znak2 in reversed(beseda):
            if znak2.isalnum():
                break
            else:
                beseda = beseda.replace(znak2, '')
    return beseda

def se_zacne_z(tvit, c):
    s = []
    tvit = izloci_besedo(tvit)

    spliti = tvit.split(" ")
    for i in spliti:
        if i.startswith(c):
            s.append(i.replace(c, '').replace(",", '').replace("?", ''))

    return s

def zberi_se_zacne_z(tviti, c):
    s = []
    for tvit in tviti:
        tvit = se_zacne_z(tvit, c)          #dobim nazaj seznam besed iz funkcije se_zacne_z(tvit, c)
        for beseda in tvit:                 #grem cez ta seznam da dobim ven vse besede
            if beseda not in s:             #ce posamezna beseda ni v MAIN seznamu, jo dodam
                s.append(beseda)
    return s

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    s = []
    for i in vsi_avtorji(tviti):
        s.append(i)
    for i in vse_afne(tviti):
        if i not in s:
            s.append(i)

    return sorted(s)

##################################################################

def besedilo(tvit):
    author, besedilo = tvit.split(":", 1)
    return besedilo[1:]                        #odstrani prvi znak niza; whitespace .. (' ')

def zadnji_tvit(tviti):
    slovar = {}
    for i in tviti:
        slovar[avtor(i)] = besedilo(i)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for i in tviti:
        if avtor(i) in slovar:
            pass
        else:
            slovar[avtor(i)] = besedilo(i)
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for i in tviti:
        if avtor(i) in slovar:
            slovar[avtor(i)] +=1                    #ce je avtor ze v slovarju se stevilo tvitov(value) poveca za 1
        else:
            slovar[avtor(i)] = 1
    return slovar

def omembe(tviti):
    slovar = {}
    for i in tviti:
        if avtor(i) not in slovar:
            slovar[avtor(i)] = se_zacne_z(i, '@')
        else:
            for element in se_zacne_z(i, '@'):
                slovar[avtor(i)].append(element)
    return slovar

def neomembe(ime, omembe):
    obstojeca_imena = []
    s = []                              #deklariram seznam za vse avtorje, ki so pisali tvite
    if ime in omembe:
        for name, tags in omembe.items():
            if name == ime:
                obstojeca_imena = tags                      #poiscemo avtorico in zapisemo omembe prijateljev v seznam

            if name not in s and name != ime:               #dodajamo vse avtorje razen sebe
                s.append(name)


    if not obstojeca_imena:                                 #ce je seznam prazen in oseba ni omenila nobenega, vrnemo vse avtorje
        return s
    else:
        for i in obstojeca_imena:
            return [i for i in s if i not in obstojeca_imena]          #vrni elemente iz seznama vseh avtorjev,
                                                            # kateri se ne pojavijo v omembah

