'''
    Opis: Naloge na temo krožišč
    Avtor: Blaž Kumer
    Datum: 2. 1. 2018
'''
def preberi(ime_datoteke):
    sez=[]
    kon={}
    f=open(ime_datoteke,"r").readlines()
    for vrstica in f:
        sez.append([int(i) for i in vrstica.strip().split()])
    for x in range(len(sez)):
        min1, index_min = min((sez[x][i],i) for i in range(len(sez[x])))
        sez[x]=sez[x][index_min:]+sez[x][:index_min]
    for i  in range(len(sez)):
        kon.update({i+1:sez[i]})
    return kon

def mozna_pot(pot,zemljevid):
    if len(zemljevid[pot[0]])>1 or len(zemljevid[pot[-1]])>1:
        return False
    for x in range(len(pot)-1):
        if pot[x+1] not in zemljevid[pot[x]]:
            return False
        if 1<x<len(pot)-2:
            if len(zemljevid[pot[x]])<2:
                return False
    return True

def hamiltonova(pot,zemljevid):
    if len(pot)!=len(set(pot)):
        return False
    count=0
    for el in zemljevid:
        if len(zemljevid[el])>1:
            count+=1
    if len(pot)<count+2:
        return False
    return mozna_pot(pot,zemljevid)

def navodila(pot,zemljevid):
    return [(zemljevid[pot[x]].index(pot[x+1])-zemljevid[pot[x]].index(pot[x-1]))%len(zemljevid[pot[x]]) for x in range(1,len(pot)-1)]

def prevozi(zacetek,navodila,zemljevid):
    sez=[zacetek,zemljevid[zacetek][0]]
    prejsnji=zacetek
    for x in range(len(navodila)):
        sez.append(zemljevid[sez[x+1]][(zemljevid[sez[x+1]].index(prejsnji)+navodila[x])%len(zemljevid[sez[x+1]])])
        prejsnji=sez[x+1]
    return sez

def sosedi(doslej,zemljevid):
    vsi=set()
    for el in doslej:
        s=set(zemljevid[el])
        vsi.update(s)
    return vsi-doslej

def razdalja(x,y,zemljevid):
    count=1
    temp=set()
    sosedi=set(zemljevid[x])
    if y in sosedi:
        return count
    while True:
        for el in sosedi:
            temp.update(set(zemljevid[el]))
        sosedi.update(temp)
        count+=1
        if y in sosedi:
            return count



