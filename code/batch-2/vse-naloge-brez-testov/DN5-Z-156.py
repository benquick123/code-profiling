def unikati(s):
    s_nov = []
    for e in s:
        if e not in s_nov:
            s_nov.append(e)
    return s_nov

def avtor(tvit):
    return tvit[:tvit.index(":")]       #najdem najprej indeks od dvopicja, nato vse do tega indeksa je avtor tvita (ime)
                                        # return tvit.split(":")[0] še ena opcija

def vsi_avtorji(tviti):
    return unikati([avtor(tvit) for tvit in tviti])    #izvirna koda po korakih v bju


def pomožna_funkcija1(beseda):
    for e in beseda:
        if e.isalnum():
            indeks = beseda.index(e)
            break
    return beseda[indeks:]


def izloci_besedo(beseda):
    beseda = pomožna_funkcija1(beseda)          #tu imam iz prve strani pobrisan
    beseda = pomožna_funkcija1(beseda[::-1])    # brisanje druge strani
    return beseda[::-1]                         #ker je beseda obrnjena, jo rabim obrnat spet v pravo stran, torej vrnem prav obrnjeno besedo


def se_zacne_z(tvit, c):
    return [izloci_besedo(e) for e in tvit.split() if e[0] == c]  #v bju mam celo kodo, ki je bolj berljiva

def zberi_se_zacne_z(tviti, c):
    return unikati(se_zacne_z(" ".join(tviti), c))   #v bju mam celo kodo, ki je po korakih

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    s = vsi_avtorji(tviti)
    s += vse_afne(tviti)
    return sorted(unikati(s))


def custva(tviti, hashtagi):
    s = []
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        seznam_besed_tvita = tvit.split()
        for beseda in seznam_besed_tvita:
            if beseda[1:] in hashtagi:        #skrb kaj če nastopi ista beseda v hastagih a je brez hastaga???
                s.append(avtor_tvita)         #USEEN COOL KER pol beseda[1:] bo pokvarjena in nebo enaka besedi hastaga!
                break                         #AKA NEBOTA ISTE
    return sorted(unikati(s))



def se_poznata(tviti, oseba1, oseba2):
    return any(True for tvit in tviti if (avtor(tvit) == oseba1 or avtor(tvit) == oseba2) and (oseba1 in se_zacne_z(tvit, "@") or oseba2 in se_zacne_z(tvit, "@")))

    #v bju mam po korakih spisan




