def unikati(s):
    nov =[]

    for el in s:
        if el not in nov:
            nov.append(el)
    return nov

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        imena.append(avtor(tvit))
    return unikati(imena)


def izloci_besedo(beseda):
    for prva in range(len(beseda)):
        if beseda[prva].isalnum():
            break
    for zadnja in range(len(beseda), 0, -1):
        if beseda[zadnja-1].isalnum():
            break
    return beseda[prva:zadnja]


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


def besedilo(tvit):
    t = tvit.split(": ")
    return ": ".join(t[1:])

def zadnji_tvit(tviti):
    slovar = {}

    for tvit in tviti:
        slovar[avtor(tvit)]=besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}

    for tvit in tviti:
        if(avtor(tvit)not in slovar.keys()):

            slovar[avtor(tvit)]=besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    imena = []
    for tvit in tviti: #ustvarimo seznam avtorjev
        imena.append(avtor(tvit))
    seznam_avtorjev = imena
    nov = {}

    for kljuc in seznam_avtorjev:
        if(kljuc not in nov.keys()):
            nov[kljuc]=1
        elif(kljuc in nov.keys()):
            nov[kljuc]=nov[kljuc]+1
    return nov

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        s = se_zacne_z(tvit,"@") #seznam omenjenih oseb v tvitu

        if(avtor_tvita in slovar.keys()): # v primeru da je avtor ze v slovarju
            seznam = slovar[avtor_tvita] #seznam omenjenih oseb ki so ze pripisane temu avtorju
            slovar[avtor_tvita]=seznam+s

        else: #ce avtor ni v slovarju
            slovar[avtor_tvita]=s


    return slovar


#Funkcija neomembe(ime, omembe) prejme ime neke osebe in takšen slovar, kakršnega vrne gornja funkcija. Vrniti mora seznam vseh ljudi,
# ki so avtorji kakega tvita, podana oseba (ime) pa jih ni omenjala. Če funkciji kot argument podamo ime "Ana" in gornji slovar,
# mora vrniti ["sandra", "benjamin], saj Ana ni omenjala Sandre in Benjamina, Cilko in Berto pa je. Iz seznama naj bo seveda
# izključena oseba sama (v tem primeru Ana). Vrstni red oseb v seznamu je lahko poljuben.
def neomembe(ime, slovar):
    vrni = []
    vse_omenjene = []
    for kljuc in slovar:
        vse_omenjene.append(kljuc)

    for oseba in vse_omenjene:
        if(oseba not in slovar[ime] and oseba != ime):
            vrni.append(oseba)

    return vrni
def se_poznata(ime1,ime2,osebe):
    vrni = False
    if ime1 in osebe.keys():
        if ime2 in osebe[ime1]:
            return True
    if ime2 in osebe.keys():
        if ime1 in osebe[ime2]:
            return True
    return vrni

def hashtagi(tviti):
    slovar = {}

    has = vsi_hashtagi(unikati(tviti))
    for h in has: #gremo cez seznam vseh uporabljenih hashov
        for tvit in tviti: #gremo cez vse tvite
            hashi = se_zacne_z(tvit,"#") #hashtagi v trenutnem tvitu
            if h in hashi: #preverimo ce je trenutni hash v hashih v trenutnem tvitu
                if h not in slovar.keys(): #ce trenutni has ni v slovarju ga dodamo
                        l = []
                        l.append(avtor(tvit))
                        slovar[h]=l
                else: #ce je mu samo appendamo avtorja
                    slovar[h].append(avtor(tvit))
                slovar[h].sort()

    return slovar
#tessti ---------------------------------------------------------------------------------------------------------------
