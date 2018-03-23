def unikati (s):
    se= []
    for stvar in s:
        if stvar not in se:
            se.append (stvar)
    return se

def avtor(tvit):
    t2 = []
    for črka in tvit:
        if črka != ":":
            t2.append(črka)

        else:
           return "".join (t2)

    return t2


def vsi_avtorji(tviti):
    nov= []
    for vsi in tviti:
        eden= avtor (vsi)
        nov.append(eden)
    return unikati(nov)

def izloci_besedo(beseda):
    s=[]




    for letter in beseda:
        if letter.isalnum () or letter== "-":
            s.append(letter)



    return "".join(s)

def se_zacne_z(tvit, c):
    s=[]
    tviti=tvit.split()

    for beseda in tviti:
        if beseda.startswith(c):
            s.append( izloci_besedo(beseda))
    return s
def zberi_se_zacne_z(tviti, c):
    s=[]
    for tvit in tviti:
        s.extend(se_zacne_z (tvit,c))

    return unikati(s)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    s=[]
    s = vsi_avtorji(tviti)
    s1=(vse_afne(tviti))
    s.extend(s1)
    s= unikati(s)
    s.sort()


    return s

def custva(tviti, hashtagi):
    s=[]
    for tvit in tviti:
        avtor1 = avtor(tvit)
        hash= se_zacne_z(tvit, "#")
        for tag in hashtagi:
            if (tag in hash):
                s.append(avtor1)

    s.sort()

    return unikati(s)

def se_poznata(tviti, oseba1, oseba2):
    s=[]
    onanjo=[]

    for tvit in tviti:
       if avtor(tvit)== oseba1 or avtor(tvit)== oseba2:
           s.append(tvit)


    onanjo= vse_afne(s)

    for tvit in s:
        for to in onanjo:
            if avtor(tvit)==oseba1 and to== oseba2:
                return True

    for tvit in s:
        for to in onanjo:
            if avtor(tvit) == oseba2 and to == oseba1:
                return True

            else:
                return False














