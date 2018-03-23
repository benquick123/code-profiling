def unikati(s):
    unikatek = []
    for i in range(len(s)):
        if s[i] in unikatek:
            continue
        else:
            unikatek.append(s[i])
    return unikatek


def avtor(tvit):
    return tvit.split()[0].split(":")[0]


def vsi_avtorji(tviti):
    tviterji = []
    for t in range(len(tviti)):
        if avtor(tviti[t]) not in tviterji:
            tviterji.append(avtor(tviti[t]))
    return tviterji


def izloci_besedo(beseda):
    while beseda[0].isalnum() == False:
        beseda = beseda[1: len(beseda)]
    while beseda[-1].isalnum() == False:
        beseda = beseda[0: len(beseda) - 1]
    return beseda


def se_zacne_z(tvit, c):
    tvit = tvit.split()
    vse_resitve = []
    for beseda in range(len(tvit)):
        if tvit[beseda][0] == c:
            vse_resitve.append(izloci_besedo(tvit[beseda]))
        else:
            continue
    return vse_resitve


def zberi_se_zacne_z(tviti, c):
    at = []
    for t in range(len(tviti)):
        at.extend(se_zacne_z(tviti[t], c))
    return unikati(at)



def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")



def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    vsi_veckrat = []
    vsi_veckrat += vsi_avtorji(tviti) + vse_afne(tviti)
    vsi_veckrat = unikati(vsi_veckrat)
    vsi_veckrat.sort()
    return vsi_veckrat


""" -----------------------------------------------------------------------------------------------------------"""

def custva(tviti, hashtagi):
    custveni_ljudje = []
    for w in range(len(hashtagi)):
        for t in range(len(tviti)):
            for z in range(len(tviti[t].split())):
                if hashtagi[w] in tviti[t].split()[z]:
                    custveni_ljudje.append(avtor(tviti[t]))
    custveni_ljudje.sort()
    return unikati(custveni_ljudje)




def se_poznata(tviti, oseba1, oseba2):
    for t in range(len(tviti)):
        if oseba1 == avtor(tviti[t]) or oseba2 == avtor(tviti[t]):
            if (oseba1 in tviti[t] and "@"+oseba2 in tviti[t]) or ("@"+oseba1 in tviti[t] and oseba2 in tviti[t]):
                return True
    return False



