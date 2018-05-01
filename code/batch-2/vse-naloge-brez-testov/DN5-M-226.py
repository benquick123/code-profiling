def unikati(s):
    r = 0
    tab = []
    while r < len(s):
        if s[r] not in tab:
            tab.append(s[r])
        r = r+1
    return tab

def avtor(tvit):
    i = 0
    tab1 = []
    tab2 = list(tvit)
    while i < len(tab2):
        if tab2[i] != ":":
            tab1.append(tab2[i])
        else:
            break
        i=i+1
    ime = "".join(tab1)
    return ime

def vsi_avtorji(tviti):
    tab = []
    for ime in tviti:
        avt = avtor(ime)
        if avt not in tab:
            tab.append(avt)
    return tab

def izloci_besedo(beseda):
    a=False
    b=False
    bes = list(beseda)
    while a == False:
        if bes[0].isalnum() == False:
            bes = bes[1:]
        else:
            a=True
    while b==False:
        i = len(bes)-1
        if bes[i].isalnum() == False:
            bes = bes[:-1]
        else:
            b=True
    bess = "".join(bes)
    return bess

def se_zacne_z(tvit, c):
    tab = []
    tab1= []
    i=0
    besede = tvit.split(" ")
    while i < len(besede):
        bes = list(besede[i])
        if bes[0] == c:
            tab.append(besede[i])
        i=i+1
    for x in tab:
        bese = izloci_besedo(x)
        tab1.append(bese)
    return tab1

def zberi_se_zacne_z(tviti, c):
    abc = []
    for a in tviti:
        abc = abc + se_zacne_z(a, c)
    d = unikati(abc)
    return d

def vse_afne(tviti):
    abc = []
    for a in tviti:
        abc = abc + se_zacne_z(a, "@")
    d = unikati(abc)
    return d

def vsi_hashtagi(tviti):
    abc = []
    for a in tviti:
        abc = abc + se_zacne_z(a, "#")
    d = unikati(abc)
    return d

def vse_osebe(tviti):
    tab = list(vsi_avtorji(tviti))+list(vse_afne(tviti))
    aaa = sorted(unikati(tab), key=str.lower)
    return aaa

