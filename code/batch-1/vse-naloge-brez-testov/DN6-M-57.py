def unikati(s):
    novi_unikati = []
    for unikatni_unikati in s:
        if unikatni_unikati not in novi_unikati:
            novi_unikati.append(unikatni_unikati)
    return novi_unikati


def avtor(tvit):
    ime_avtorja = ''
    for crka1 in tvit:
        if crka1 != ':':
            ime_avtorja = ime_avtorja + crka1
        else:
            break
    return ime_avtorja


def vsi_avtorji(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        if avtor(tvit) not in seznam_avtorjev:
            seznam_avtorjev.append(avtor(tvit))
    return seznam_avtorjev



def izloci_besedo(beseda):
    seznam_besed = ''
    for crka in beseda:
        if True == crka.isalnum() or crka == '-':
            seznam_besed = seznam_besed + crka
    return seznam_besed


def se_zacne_z(tvit, c):
    vrnjene_besede = []
    beseda = ''
    pisemo = 0
    for i in range(len(tvit)):
        if tvit[i].isalnum() == False:
            pisemo = 0
            if beseda != '':
                vrnjene_besede.append(beseda)
            beseda = ''
        if pisemo == 1:
            beseda = beseda + tvit[i]
        if tvit[i] == c:
            pisemo = 1
        if i == len(tvit) - 1 and pisemo == 1:
            pisemo = 0
            if beseda != '':
                vrnjene_besede.append(beseda)
            beseda = ''
    return vrnjene_besede


def zberi_se_zacne_z(tviti, c):
    vrnjeni_tviti = []
    for vsi_tviti in tviti:
        besede_v_enem_tvitu = se_zacne_z(vsi_tviti, c)
        for ena_beseda in besede_v_enem_tvitu:
            if ena_beseda not in vrnjeni_tviti:
                vrnjeni_tviti.append(ena_beseda)
    return vrnjeni_tviti


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')


def vse_osebe(tviti):
    alfa_seznam = []
    a = vsi_avtorji(tviti)
    b = zberi_se_zacne_z(tviti, '@')
    for avtorji in a:
        if avtorji not in alfa_seznam:
            alfa_seznam.append(avtorji)
    for avtorji in b:
        if avtorji not in alfa_seznam:
            alfa_seznam.append(avtorji)
    alfa_seznam.sort()

    return alfa_seznam


def besedilo(tvit):
    string = ''
    pisemo = 0
    presledek = [' ']
    for crka in tvit:
        if pisemo == 1:
            string = string + crka
        if crka == ':':
            pisemo = 1
    if string[0] == ' ':
        string2 = ''
        for i in range(1, len(string)):
            string2 = string2 + string[i]
        return string2
    return string




def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar



def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = besedilo(tvit)
    return slovar


def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = 1
        else:
            slovar[avtor(tvit)] = slovar[avtor(tvit)] + 1
    return slovar


def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        osebe = se_zacne_z(tvit, '@')
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = osebe
        else:
            for oseba in osebe:
                if oseba not in slovar[avtor(tvit)]:
                    slovar[avtor(tvit)].append(oseba)
    return slovar
        

def neomembe(ime, omembe):
    seznam = []
    for avtor in omembe:
        if avtor not in omembe[ime] and avtor != ime:
            seznam.append(avtor)
    return seznam






















