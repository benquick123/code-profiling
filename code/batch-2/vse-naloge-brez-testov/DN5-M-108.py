def unikati(s):
    seznam = []
    for x in s:
        if x not in seznam:
            seznam.append(x)
    return seznam


def avtor(tvit):

    b = tvit.split(" ")
    return b[0][:-1]

def vsi_avtorji(tviti):
    seznam = []
    for x in tviti:
        a = avtor(x)
        seznam.append(a)

    seznam1= unikati(seznam)
    return seznam1

def izloci_besedo(beseda):
    for x in beseda:              #gres cez vse znake v besedi
        if x.isalnum() == False:   #ce 1. znak ni alfanumeričen ga odstraniš
            beseda = beseda[1:]
        else:
            break           #prenehaš ko prideš do prve črke ali številke

    a = beseda[::-1]            #obrnes besedo okoli in ponoviš
    for y in a:
        if y.isalnum()==False:
            a = a[1:]
        else:
            break
    return a[::-1]          #ko returnaš, ponovno obrneš besedo

def se_zacne_z(tvit, c):
    seznam = []
    b = tvit.split(" ")   #b= seznam splitanih besed

    for beseda in b:    #gres cez vse besede v b
        if beseda[0] == c:   #ce se beseda zacne z c, jo dodas na seznam
            seznam.append(beseda)

    koncniseznam = []
    for beseda1 in seznam:    #gres seenkrat cez seznam in vedno klices funkcijo izloci_besedo
        koncniseznam.append(izloci_besedo(beseda1))


    return koncniseznam


def zberi_se_zacne_z(tviti, c):
    seznam = []

    for tvit in tviti:
        a = se_zacne_z(tvit,c)
        seznam.extend(a)

    seznam = unikati(seznam)
    return seznam

def vse_afne(tviti):

    seznam = zberi_se_zacne_z(tviti, "@")
    return seznam

def vsi_hashtagi(tviti):
    seznam = zberi_se_zacne_z(tviti, "#")
    return seznam


def vse_osebe(tviti):
    seznam_avtorjev = vsi_avtorji(tviti)
    seznam_avtorjev.extend(vse_afne(tviti))

    seznam_avtorjev = sorted(unikati(seznam_avtorjev))

    return seznam_avtorjev

def custva(tviti, hashtagi):
    seznam = []
    for tvit in tviti:
        besede = tvit.split(" ")
        for beseda in besede:
            for beseda1 in hashtagi:
                if beseda == "#"+beseda1:
                    seznam.append(avtor(tvit))

    seznam = unikati(seznam)

    return sorted(seznam)

def se_poznata(tviti, oseba1, oseba2):
    se_poznata= False
    for tvit in tviti: #gres skozi vsak tvit
        avtor1 = avtor(tvit)   #zapises avtorja tvita
        seznam = se_zacne_z(tvit,"@")  #naredis seznam vseh oseb, ki jih je avtor omenil

        if oseba1 == avtor1 and oseba2 in seznam:  #ce je oseba 1 avtor in je oseba 2 med
            se_poznata = True          # seznamom omenjenih oseb nastavi se_poznata na True


    return se_poznata


