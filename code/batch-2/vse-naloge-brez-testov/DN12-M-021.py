import collections

def obrni(zaporedje):
    zaporList=zaporedje.split()
    zaporList=list(map(int, zaporList))
    najmanjse=zaporList.index(min(zaporList))
    if najmanjse != 0:
        novList= collections.deque(zaporList)
        novList.rotate(len(zaporList)-najmanjse)
        return list(novList)
    return zaporList

def obrni2(zaporedje,vhod,izhod):
    novList= collections.deque(zaporedje[vhod])
    while novList.index(izhod) != 0:
        novList.rotate(1)
    return list(novList)

def preberi(ime_datoteke):
    file = open(ime_datoteke, "r", encoding='utf-8')
    t = file.readlines()
    slovar = {}
    i = 1
    for neki in t:
        slovar[i]=neki
        slovar[i]=obrni(slovar[i])
        i+=1
    file.close()
    return slovar

def mozna_pot(pot, zemljevid):
    i = 0
    while i < len(pot)-1:
        if pot[i] in zemljevid[pot[i+1]] and pot[i] != pot[i+1] and len(zemljevid[pot[0]]) == 1  and len(zemljevid[pot[len(pot)-1]]) == 1:
            if i != 0 and i != len(pot)-1 and len(zemljevid[pot[i]]) == 1:
                return False
            znak= True
        else:
            return False
        i+=1
    return znak

def hamiltonova(pot, zemljevid):
    i = 0
    for neki in zemljevid:
        if len(zemljevid[neki]) == 1:
            i = i + 1
    i=i-2
    if mozna_pot(pot, zemljevid) and len(pot) == len(zemljevid)-i:
        znak= True
    else:
        return False
    return znak

def navodila(pot, zemljevid):
    t=[]
    i=0
    while i < len(pot)-2:
        vhod=zemljevid[pot[i+1]].index(pot[i])
        izhod=zemljevid[pot[i+1]].index(pot[i+2])
        rez=(izhod+1)-(vhod+1)
        t.append(rez % len(zemljevid[pot[i+1]]))
        i+=1
    return t

def prevozi(zacetek, navodila, zemljevid):
    vhod=0
    i=0
    seznam=[zacetek]
    while i < len(navodila):
        if i == 0:
            for kljuc in zemljevid:
                if zacetek in zemljevid[kljuc]:
                    vhod = kljuc
            seznam.append(vhod)
        t=obrni2(zemljevid,vhod,zacetek)
        vred=t[navodila[i]]
        seznam.append(vred)
        zacetek = vhod
        vhod = vred
        i+=1
    return seznam

def sosedi(doslej, zemljevid):
    mnozica= set(doslej)
    novmno=set()
    for neki in mnozica:
        for neki2 in zemljevid[neki]:
            novmno.add(neki2)
    return novmno - mnozica



