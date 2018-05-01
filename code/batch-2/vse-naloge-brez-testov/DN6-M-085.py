import collections
def izloci_besedo(beseda): #deklaracija funkcije
    for x in beseda: #premikanje po seznamu
        if x.isalnum(): #uporaba funkcije isalnum()
            a=beseda.find(x) #shrani se v a
            break #izhod iz if stavka
    beseda=beseda[::-1] #beseda je zadnji znak
    for x in beseda: #zanka za pomik po seznamu
        if x.isalnum(): #ponovna uporaba isalnum
            b=beseda.find(x)
            break #izhod iz if stavka
    beseda=beseda[::-1] #deklaracija zadnjega elementa
    konec= beseda[a:(len(beseda)-b)]
    return konec
def se_zacne_z(tvit,c): #deklaracija funkcije
    a=tvit.split() #razdelitev elementa
    seznam=[] #prazen seznam
    for x in a: #zanka za premik po terki
        if x[0]==c:#preveri če je element enak c
            seznam.append(izloci_besedo(x)) #pripnitev elementa v seznam (pripne elemnt katerega vrne funkcija izloči besedo)
    return seznam #izpis
def besedilo(tvit):
    vrednost=tvit.split(": ",1)
    return vrednost[1]

def avtorji(tvit):
    avtor=tvit.split(": ", 1)
    return avtor[0]

def zadnji_tvit(tviti):
    slovar=collections.defaultdict(str)#slovar ki ima znotraj neko privzeto vrednost ""
    for i in tviti:
        tvit=besedilo(i)
        avtor=avtorji(i)
        slovar[avtor]=tvit
    return slovar

def prvi_tvit(tviti):
    slovar = collections.defaultdict(str)  # slovar ki ima znotraj neko privzeto vrednost
    for i in tviti:
        tvit = besedilo(i)
        avtor = avtorji(i)
        if slovar[avtor] == "":
            slovar[avtor] = tvit
    return slovar

def prestej_tvite(tviti):
    slovar = collections.defaultdict(int)  # slovar ki ima znotraj neko privzeto vrednost
    for i in tviti:
        avtor = avtorji(i)
        slovar[avtor]+=1
    return slovar


def omembe(tviti):
    slovar= collections.defaultdict(list)

    for i in tviti:
        sezacnez=se_zacne_z(i, "@")
        avtor=avtorji(i)
        slovar[avtor].extend(sezacnez)
    return slovar

"""{"sandra": ["berta", "benjamin", "ana"],
"benjamin": [],
"cilka": [],
"berta": ["sandra"],
"ana": ["berta", "cilka", "dani"]}

ana
"""
def neomembe(ime, omembe):
    seznam= []
    for avt, vrednosti in omembe.items():
        if avt not in omembe[ime] and avt != ime:
            seznam.append(avt)

    return seznam




