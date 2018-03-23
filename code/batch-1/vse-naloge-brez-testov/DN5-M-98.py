def unikati(s):
    seznam = []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

def avtor(tvit):
    a = tvit.split()
    b = a[0]
    c = b[:-1]
    return c

def vsi_avtorji(tviti):
    seznam = []
    for i in tviti:
        a = avtor(i)
        if a not in seznam:
            seznam.append(a)
    return seznam

def izloci_besedo(beseda):
    for i in range(len(beseda) - 1):
        if beseda[i].isalnum():
            break

    for j in range(len(beseda)-1, 0, -1):
        if beseda[j].isalnum():
            break
    beseda = beseda[i:j + 1]
    return beseda

def se_zacne_z(tvit, c):
    besede = tvit.split()
    seznam_besed = []
    for b in besede:
        if b[0] == c:
            seznam_besed.append(izloci_besedo(b))
    return seznam_besed

def zberi_se_zacne_z(tviti, c):
    s = []
    for i in tviti:
        s = s + se_zacne_z(i, c)
    return unikati(s)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    seznam_oseb = vsi_avtorji(tviti) + vse_afne(tviti)
    return sorted(unikati(seznam_oseb))

#Dodatna naloga

def custva(tviti, hashtagi):
    avtorji = []
    for i in tviti:
        if bool(set(se_zacne_z(i, "#")) & set(hashtagi)):
            avtorji.append(avtor(i))
    return sorted(unikati(avtorji))


def se_poznata(tviti, oseba1, oseba2):
    for i in tviti:
        avtor_t = avtor(i)
        omenjeni = se_zacne_z(i, "@")
        if omenjeni:
            osebe = []
            osebe = osebe + omenjeni
            osebe.append(avtor_t)
            if oseba1 in unikati(osebe) and oseba2 in unikati(osebe):
                return True
    else:
        return False


