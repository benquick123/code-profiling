def vse_osebe(tviti):
    osebe = vse_afne(tviti) + vsi_avtorji(tviti)
    for element in osebe:
        element = (izloci_besedo(element))
    return sorted(unikati(osebe))

def vsi_hashtagi(tviti):
    hashtagi = []
    for tvit in tviti:
        temp = se_zacne_z(tvit, "#")
        for element in temp:
            hashtagi.append(element)
    return unikati(hashtagi)

def vse_afne(tviti):
    afne = []
    for tvit in tviti:
        temp = se_zacne_z(tvit, "@")
        for element in temp:
            afne.append(element)
    return unikati(afne)

def zberi_se_zacne_z(tviti, c):
    izbrani = []
    for tvit in tviti:
        temp = se_zacne_z(tvit, c)
        for element in temp:
            izbrani.append(element)
    return unikati(izbrani)

def se_zacne_z(tvit, c):
    zacne = []
    besede = tvit.split()
    for element in besede:
        if element.startswith(c):
            zacne.append(izloci_besedo(element))
    return zacne

def izloci_besedo(beseda):
    return ''.join(ch for ch in beseda if ch.isalnum() or ch=="-")

def vsi_avtorji(tviti):
    temp = []
    for element in tviti:
        temp.append(avtor(element))
    avtorji = unikati(temp)
    return avtorji

def avtor(tvit):
    besede = tvit.split()
    avtor = besede[0][:-1]
    return avtor

def unikati(s):
    unikat = []
    for element in s:
        if element not in unikat:
            unikat.append(element)
    return unikat

def besedilo(tvit):
    for i in range (len(tvit)):
        if tvit[i] == ":":
            dolzina = i + 2
            break
    return tvit[dolzina:]

def zadnji_tvit(tviti):
    my_dict = {}
    for tvit in tviti:
        ime = avtor(tvit)
        post = besedilo(tvit)
        if ime not in my_dict.keys():
            my_dict[ime] = post
        elif ime in my_dict.keys():
            my_dict[ime] = post
    return my_dict

def prvi_tvit(tviti):
    my_dict = {}
    for tvit in tviti:
        ime = avtor(tvit)
        post = besedilo(tvit)
        if ime not in my_dict.keys():
            my_dict[ime] = post
    return my_dict

def prestej_tvite(tviti):
    my_dict = {}
    for tvit in tviti:
        ime = avtor(tvit)
        if ime not in my_dict.keys():
            my_dict[ime] = 0
        if ime in my_dict.keys():
            my_dict[ime] += 1
    return my_dict

def omembe(tviti):
    my_dict = {}
    for tvit in tviti:
        ime = avtor(tvit)
        omenjeni = se_zacne_z(tvit, "@")
        if ime not in my_dict.keys():
            my_dict[ime] = omenjeni
        elif ime in my_dict.keys():
            my_dict[ime] += omenjeni
    return my_dict

def neomembe(ime, omembe):
    neomenjeni = []
    omenjene = omembe[ime]
    for oseba in omembe:
        if oseba not in omenjene and oseba != ime:
            neomenjeni.append(oseba)
    return neomenjeni


