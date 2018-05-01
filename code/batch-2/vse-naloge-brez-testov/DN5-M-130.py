def unikati(s):
    unikati = []

    for unikat in s:

        if unikat in unikati:
            unikati = unikati

        else:
            unikati.append(unikat)

    return unikati

def avtor(tvit):
    i = 0
    avtor= []
    while i < len(tvit):
        if tvit[i] != ":":
            avtor.append(tvit[i])
        else:
            break
        i += 1
    avtor = "".join(avtor)
    return avtor

def vsi_avtorji(tviti):
    avtorji = []

    for tvit in tviti:

        avtorji.append(avtor(tvit))
    avtorji = unikati(avtorji)
    return avtorji

def izloci_besedo(beseda):
    i = 0

    while i < len(beseda):
        if beseda[i].isalnum():
            break
        else:
            beseda = beseda.replace(beseda[i],"")


    j = (len(beseda)-1)
    while beseda[j].isalnum() == False:
        beseda = beseda.replace(beseda[j], "")
        j = (len(beseda) - 1)
    return beseda

def se_zacne_z(tvit, c):
    i = 0
    j = 0
    besede = []
    beseda = []
    bes = ""
    while i < len(tvit)-1:
        if tvit[i] == c:
            j = i +1

            while tvit[j].isalnum():

                beseda.append(tvit[j])
                j += 1
                if j == len(tvit):
                    break

            bes = "".join(beseda)

            besede.append(bes)
            beseda = []
        i +=1
    return besede

def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        besede += se_zacne_z(tvit, c)
    besede = unikati(besede)
    return besede

def vse_afne(tviti):
    afne = zberi_se_zacne_z(tviti, "@")
    return afne

def vsi_hashtagi(tviti):
    hashi = zberi_se_zacne_z(tviti, "#")
    return hashi

def vse_osebe(tviti):
    osebe= vsi_avtorji(tviti) + vse_afne(tviti)
    osebe = unikati(osebe)
    osebe.sort()
    return osebe

def custva(tviti, hashtagi):
    imena = []


    for tvit in tviti:

        for hash in hashtagi:

            for hash_v_tvitu in se_zacne_z(tvit, "#"):
                if hash_v_tvitu == hash:
                    avtor1 = avtor(tvit)
                    imena.append(avtor1)

    imena = unikati(imena)
    imena.sort()
    return imena

def se_poznata(tviti, oseba1, oseba2):



    for tvit in tviti:
        avtor1 = avtor(tvit)
        if avtor1 == oseba1 and oseba2 in se_zacne_z(tvit, "@"):
            return True
        if avtor1 == oseba2 and oseba1 in se_zacne_z(tvit, "@") :
            return True
    else:
        return False









