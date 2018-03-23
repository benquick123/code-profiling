

def unikati(s):
    seznam=[]
    seznam.clear()
    for x in s:
        if x not in seznam:
            seznam.append(x)

    return seznam

def avtor(tvit):
    return tvit.split(": ",1)[0]

def vsi_avtorji(tviti):
    seznam_avtorji=[]
    seznam_avtorji.clear()
    for i in tviti:
        seznam_avtorji.append(avtor(i))

    return unikati(seznam_avtorji)

def izloci_besedo(beseda):
    wrd=list(beseda)
    while True:
        if not (wrd[0].isalnum()):
            del wrd[0]
        else:break

    while True:
        if not (wrd[len(wrd)-1].isalnum()):
            del wrd[len(wrd)-1]
        else:break

    wrd="".join(wrd)
    return wrd

def se_zacne_z(tvit, c):
    z=tvit.split(" ")
    l=[]
    for i in z:
        if i.startswith(c):
            l.append(izloci_besedo(i))
    if l==[]:
        return
    else:
        return l

def zberi_se_zacne_z(tviti, c):
    lt=[]
    for i in tviti:
        l=se_zacne_z(i,c)
        if l!=None:
            for j in l:
                    lt.append(j)

    return unikati(lt)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def unija(s1, s2):
    return list(set(s1) | set(s2))


def vse_osebe(tviti):
    osebe=unija(vsi_avtorji(tviti),vse_afne(tviti))
    osebe.sort()
    return osebe

def custva(tviti, hashtagi):
    osebe=[]
    for i in tviti:
        for j in hashtagi:
            if j in i:
                osebe.append(avtor(i))
    osebe=unikati(osebe)
    osebe.sort()
    return osebe

def se_poznata(tviti, oseba1, oseba2):
    if oseba1 in vse_osebe(tviti) and oseba2 in vse_osebe(tviti) and (oseba1 in vsi_avtorji(tviti) or oseba2 in vsi_avtorji(tviti)):
        for i in tviti:
            if oseba1==avtor(i):
                if i.find(oseba2)>0:
                    return True
            elif oseba2 ==avtor(i):
                if i.find(oseba1)>0:
                    return True

        return False
    else:return False




