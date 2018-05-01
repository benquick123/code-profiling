def rotate(l, n):
    return l[-n:] + l[:-n]

def preberi(ime_datoteke):
    datoteka=open(ime_datoteke)
    i=1
    krozisca={}
    for vrstica in datoteka:
        vrstica=vrstica.strip()
        vrstice=list(map(int,vrstica.split(" ")))
        if(vrstice[0]!=min(vrstice)):
           pos=vrstice.index(min(vrstice))
           vrstice=rotate(vrstice, -pos)
        krozisca[i]=vrstice
        i=i+1
    datoteka.close()
    return(krozisca)

def mozna_pot(pot, zemljevid):

    #konca in zacne
    konec=pot[(len(pot)-1)]
    zacne = pot[0]
    if(len(zemljevid[konec])!=1 or len(zemljevid[zacne])!=1):
        return False
    #povezani
    for od, do in zip(pot,pot[1:]):
        if(od not in zemljevid[do]):
            return False
    #vmes ven
    for krizisce in pot[1:len(pot)-1]:
        if(len(zemljevid[krizisce])==1):
            return False

    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid) == True:
        seen=[]
        #ponavljanje
        for krizisce in pot:
            if krizisce not in seen:
                seen.append(krizisce)
            else:
                return False
        #dolzina
        if(len(seen)>5):
            if(len(seen)+1==len(zemljevid)-1):
                return True
            else:
                return False
        else:
            if (len(seen)== len(zemljevid)):
                return True
            else:
                return False
    else:
        return False

def navodila(pot, zemljevid):
    return [(zemljevid[y].index(z) - zemljevid[y].index(x)) % len(zemljevid[y]) for x, y, z in zip(pot, pot[1:], pot[2:])]

def prevozi(zacetek, navodila, zemljevid):
    arr=[zacetek]
    navodila.insert(0,0)
    kam=zacetek
    prej=0
    for navodilo in navodila:
        arr.append(zemljevid[kam][(navodilo+prej)%len(zemljevid[kam])])
        kam=zemljevid[kam][(navodilo+prej)%len(zemljevid[kam])]
        prej=zemljevid[kam].index(zacetek)
        zacetek=kam
    return arr

def sosedi(doslej, zemljevid):
    seen=[]
    for krizisce in doslej:
        for izvoz in zemljevid[krizisce]:
            if izvoz not in doslej and izvoz not in seen:
                seen.append(izvoz)
    return {x for x in seen}

def razdalja(x, y, zemljevid):
    x={x}
    for i in range(1, len(zemljevid)):
        x=sosedi(x, zemljevid)
        if(y in x):
            return i

def poisci_pot(zemljevid, x, y, path):
    path = path + [x]
    if x == y:
        return path
    if x not in zemljevid.keys():
        return None
    shortest = None
    for krizisce in zemljevid[x]:
        if krizisce not in path:
            newpath = poisci_pot(zemljevid, krizisce, y, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def najkrajsa_navodila(x, y, zemljevid):
    pot=[]
    pot=poisci_pot(zemljevid, x, y, pot)
    return navodila(pot, zemljevid)


