import collections

def izloci_besedo(beseda):
    stevec_d = 0
    stevec_l = 0
    for i in range(0, len(beseda)):
        if (beseda[i].isalnum() == False):
            stevec_l = stevec_l + 1
        else:
            break

    for i in range(len(beseda) - 1, 0, -1):
        if (beseda[i].isalnum() == False):
            stevec_d = stevec_d + 1
        else:
            break

    return beseda[stevec_l:len(beseda) - stevec_d]

def unikati(seznam):
    novi_seznam = []
    for element_a in seznam:
        if(element_a in novi_seznam):
            continue
        else:
            novi_seznam.append(element_a)

    return novi_seznam

def se_zacne_z(tvit, c):
    seznam_besed = []
    seznam_tvit = tvit.split()
    for beseda in seznam_tvit:
        if(beseda[0] == c):
            if(len(beseda) > 1):
                skrajsana_beseda = izloci_besedo(beseda)
                seznam_besed.append(skrajsana_beseda)
            else:
                continue
        else:
            continue

    return unikati(seznam_besed)

def zberi_se_zacne_z(tviti, c):
    koncni_seznam = []
    for tvit in tviti:
        koncni_seznam.extend(se_zacne_z(tvit, c))

    return unikati(koncni_seznam)

def vse_afne(tviti):
    odgovor = zberi_se_zacne_z(tviti, "@")

    return  odgovor

def besedilo(tvit):
    nov_tvit = tvit.split()
    odgovor = nov_tvit[1: len(nov_tvit)]

    return " ".join(odgovor)

def avtor(tvit):
    seznam = tvit.split()
    prvi_element = seznam[0]
    odgovor = prvi_element[0:len(prvi_element)-1]

    return odgovor

def zadnji_tvit(tviti):
    slovar = collections.defaultdict()
    for tvit in tviti:
        pisec = avtor(tvit)
        text = besedilo(tvit)
        slovar[pisec] = text

    return slovar

def prvi_tvit(tviti):
    slovar = collections.defaultdict()
    for tvit in tviti:
        pisec = avtor(tvit)
        if pisec in slovar:
            continue
        else:
            text = besedilo(tvit)
            slovar[pisec] = text

    return slovar

def prestej_tvite(tviti):

    slovar = collections.defaultdict()
    for tvit in tviti:
        pisec = avtor(tvit)
        if pisec in slovar:
            slovar[pisec] += 1
        else:
            slovar[pisec] = 1

    return slovar

def omembe(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        pisec = avtor(tvit)
        omenjeni = se_zacne_z(tvit, "@")
        slovar[pisec].extend(omenjeni)

    return slovar

def vse_osebe(tviti):
    seznam1 = vsi_avtorji(tviti)
    seznam2 = vse_afne(tviti)

    return  sorted(unikati(seznam1+seznam2))

def vsi_avtorji(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        nov_uporabnik = avtor(tvit)
        seznam_avtorjev.append(nov_uporabnik)

    return seznam_avtorjev

def neomembe(ime, omembe):
    omenjeni = []
    pisec = [ime]
    for nekdo in omembe:
        if nekdo == ime:
            omenjeni.extend(omembe[ime])

    omenjeni.extend(pisec)
    novi_omenjeni = unikati(omenjeni)

    vsi = []
    for key in omembe:
        vsi.extend([key])

    odgovor = []
    neki = unikati(vsi)
    for oseba in neki:
        if oseba not in novi_omenjeni:
            odgovor.extend([oseba])
        else:
            continue

    return odgovor

def se_poznata(ime1, ime2, omembe):
    for key in omembe:
        if ime1 == key:
            if ime2 in omembe[ime1]:
                return True
        elif ime2 == key:
            if ime1 in omembe[ime2]:
                return True
    else:
        return False

def vsi_hashtagi(tviti):
    odgovor = zberi_se_zacne_z(tviti, "#")

    return odgovor

def hashtagi(tviti):
    hashtagi = sorted(unikati(vsi_hashtagi(tviti)))
    avtorji = sorted(unikati(vsi_avtorji(tviti)))
    slovar = dict.fromkeys(hashtagi, [])

    for kakec in avtorji:

        for tvit in tviti:
            pisec = avtor(tvit)
            if kakec == pisec:
                trenutni_hashtagi = se_zacne_z(tvit, "#")


                for hashtag in trenutni_hashtagi:

                    if kakec not in slovar[hashtag]:
                        slovar[hashtag].extend([pisec])
                    else:
                        continue


    return slovar



