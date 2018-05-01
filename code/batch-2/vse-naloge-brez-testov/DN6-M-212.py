def besedilo(tvit):

    return tvit.split(":", 1)[1].strip()



def zadnji_avtor(tvit):

    return tvit.split(":")[0]



def zadnji_tvit(tviti):
    dict_tviti = {}
    for tvit in tviti:
        dict_tviti[zadnji_avtor(tvit)] = besedilo(tvit)

    return dict_tviti



def prvi_tvit(tviti):
    dict_tviti = {}
    for tvit in tviti:
        if not dict_tviti.get(zadnji_avtor(tvit)):
            dict_tviti[zadnji_avtor(tvit)]=besedilo(tvit)

    return dict_tviti

def prestej_tvite(tviti):
    število_tvitov = {}
    for tvit in tviti:
        if not število_tvitov.get(zadnji_avtor(tvit)):
            število_tvitov[zadnji_avtor(tvit)] = 1
        else:
            število_tvitov[zadnji_avtor(tvit)] += 1

    return število_tvitov



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


def omembe(tviti):
    dict_omembe = {}
    for tvit in tviti:
        omemba = se_zacne_z(besedilo(tvit), "@")
        if not dict_omembe.get(zadnji_avtor(tvit)):
            dict_omembe[zadnji_avtor(tvit)] = []
            dict_omembe[zadnji_avtor(tvit)].extend(omemba)

    return dict_omembe


def neomembe(ime, omembe):
    omenjena_oseba = omembe[ime]
    vse_osebe = list(omembe.keys())
    neomenjena_oseba = []
    for i in vse_osebe:
        if not i in omenjena_oseba and i != ime:
            neomenjena_oseba.append(i)
    return neomenjena_oseba

