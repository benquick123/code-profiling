def unikati(s):
    tab = []
    i = 0
    j = 0
    while i < len(s):
        j = 0
        vsebuje = False
        while j < len(tab):
            if s[i] == tab[j]:
                vsebuje = True
            j = j + 1
        if vsebuje == False:
            tab.append(s[i])
        i = i + 1

    return tab

def avtor(tvit):
    znaki = list(tvit)
    i = 0
    while i < len(znaki):
        if znaki[i] == ":":
            break
        i = i + 1

    tab = []
    j = 0
    while j < i:
        tab.append(znaki[j])
        j = j + 1

    avtor = "".join(tab)

    return avtor

def vsi_avtorji(tviti):
    avtorji = []
    i = 0
    while i < len(tviti):
        x = avtor(tviti[i])
        avtorji.append(x)
        i = i + 1

    avtorji = unikati(avtorji)

    return avtorji


def izloci_besedo(beseda):
    tab = list(beseda)
    i = 0
    while i < len(beseda):
        if tab[i].isalnum() == 1:
            break
        i = i + 1

    j = len(beseda) - 1
    while j > 0:
        if tab[j].isalnum() == 1:
            break
        j = j - 1

    tab2 = []

    while i <= j:
        tab2.append(tab[i])
        i = i + 1

    return "".join(tab2)

def se_zacne_z(tvit, c):
    tab1 = tvit.split()
    tab2 = []
    i = 0
    while i < len(tab1):
        beseda = list(tab1[i])
        if beseda[0] == c:
            tab2.append(tab1[i])
        i = i + 1


    besede = []
    j = 0
    while j < len(tab2):
        besede.append(izloci_besedo(tab2[j]))
        j = j + 1

    return besede

def zberi_se_zacne_z(tviti, c):
    i = 0
    besede = []
    while i < len(tviti):
        besede = list(besede) + list(se_zacne_z(tviti[i], c))
        i = i +1

    return unikati(besede)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    tab = list(vsi_avtorji(tviti))+list(vse_afne(tviti))
    return sorted(unikati(tab), key=str.lower)


































