def se_zacne_z(tvit, c):
    tabela=[]
    offset=0
    vse_besede = tvit.split(" ")
    for x in vse_besede:
        if x[0] == c:
            trenutna = izloci_besedo(x)
            tabela.append(trenutna)
    return tabela



def izloci_besedo(beseda):
    asd = beseda
    while(not asd[0].isalnum()):
        asd = asd[1:]

    while(not asd[-1].isalnum()):
        asd = asd[:-1]

    return asd

def besedilo(tvit):



    return tvit[tvit.find(":")+2:]

def zadnji_tvit(tviti):


    slovar = {}

    for x in tviti:

        besedilotvita = besedilo(x)

        ime = x[:x.find(":")]

        slovar[ime]=besedilotvita

    return slovar

def prvi_tvit(tviti):

    slovar = {}

    for x in tviti:

        besedilotvita = besedilo(x)


        ime = x[:x.find(":")]

        if ime not in slovar:
            slovar[ime] = besedilotvita



    return slovar


def prestej_tvite(tviti):

    slovar = {}

    for x in tviti:

        ime = x[:x.find(":")]

        if ime not in slovar:
            slovar[ime] = 0

        slovar[ime] = slovar[ime] + 1

    return slovar



def omembe(tviti):
    slovar = {}

    for x in tviti:

        ime = x[:x.find(":")]
        if ime not in slovar:
            slovar[ime] = []

        besedilotvita = besedilo(x)

        seznamoseb = se_zacne_z(besedilotvita, "@")


        for y in seznamoseb:

            if slovar[ime]:
                if y not in slovar[ime]:
                    slovar[ime].append(y)

            else :
                slovar[ime]=[y]

            #print(slovar[ime])


    return slovar

def neomembe(ime, omembe):

    seznamAvtorjev = []
    for x in omembe:
        if x not in seznamAvtorjev:
            seznamAvtorjev.append(x)

    osebaJeOmenila = omembe[ime]

    result=[]

    for x in seznamAvtorjev:
        if x not in osebaJeOmenila and x != ime:
            result.append(x)


    return result




