
def unikati(s):
    nov_seznam=[]
    for tviti in s:
        if(tviti not in nov_seznam):
            nov_seznam.append(tviti)
    return nov_seznam

def avtor(tviti):
    seznam=[]
    seznam=tviti.split(":")
    return(seznam[0])

def vsi_avtorji(tviti):
    avtorji=[]
    for twit in tviti:
        if(avtor(twit) not in avtorji):
            avtorji.append(avtor(twit))
    return avtorji

def izloci_besedo(beseda):
    x=0
    y=0
    while (x == 0 & y==0):
        dol = len(beseda)
        if(beseda[0].isalnum() == False):
            beseda=beseda[1:]
            dol = len(beseda)
        else:
            x = 1
        if(beseda[dol-1].isalnum()== False):
            beseda=beseda[:-1]
            dol = len(beseda)
        else:
            y = 1
    return beseda
def se_zacne_z(tvit, c):
    a=[]
    b=[]
    a=tvit.split(' ')
    for twitt in a:
        if(twitt.startswith(c)):
            b.append(izloci_besedo(twitt))

    return(b)

def zberi_se_zacne_z(tviti, c):
    seznamek=[]
    for tvits in tviti:
        for x in se_zacne_z(tvits,c):
            if(x not in seznamek):
                seznamek.append(x)
    return seznamek

def vse_afne(tviti):
    return(zberi_se_zacne_z(tviti,'@'))

def vsi_hashtagi(tviti):
    return (zberi_se_zacne_z(tviti, '#'))

def vse_osebe(tviti):
    seznamoseb = []
    seznamafn = []
    merged = []
    seznamoseb.extend(vsi_avtorji(tviti))
    seznamoseb.extend(vse_afne(tviti))
    merged=[*seznamoseb,*seznamafn]
    return(sorted(unikati(merged)))


