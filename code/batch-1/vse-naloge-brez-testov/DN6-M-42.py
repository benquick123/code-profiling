def besedilo(tvit):
    tvit=tvit.split(': ',1)[1]
    return tvit

def zadnji_tvit(tviti):
    slovar={}
    for t in tviti:
        avtor=t.split(': ',1)[0]
        text=t.split(': ',1)[1]
        slovar[avtor]=text
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for t in tviti:
        avtor = t.split(': ', 1)[0]
        text = t.split(': ', 1)[1]
        if (avtor not in slovar):
            slovar[avtor] = text
    return slovar

def prestej_tvite(tviti):
    slovar={}
    for t in tviti:
        avtor = t.split(': ', 1)[0]
        if(avtor in slovar):
            x=slovar[avtor]+1
            slovar[avtor] = x
        else:
            slovar[avtor]=1
    return slovar
def se_zacne_z(tvit, c):
    a=[]
    b=[]
    a=tvit.split(' ')
    for twitt in a:
        if(twitt.startswith(c)):
            b.append(izloci_besedo(twitt))

    return(b)
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
def omembe(tviti):
    slovar={}
    seznam=[]
    for t in tviti:
        avtor = t.split(': ', 1)[0]
        seznam=se_zacne_z(t,'@')
        if (avtor in slovar):
            x=slovar[avtor]
            slovar[avtor]=x+seznam
        else:
            slovar[avtor]=seznam
    return slovar

def neomembe(ime, omembe):
    slovar={}
    seznam=[]
    x=slovar = omembe[ime]
    for t in omembe:
        if t not in x:
            if t != ime:
                seznam.append(t)
    return seznam

