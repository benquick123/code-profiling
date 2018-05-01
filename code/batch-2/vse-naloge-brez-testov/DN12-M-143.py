def preberi(ime_datoteke):
    i=1
    slovar_k={}
    integerji=[]
    file = open(ime_datoteke)
    for vrstica in file:
        vrstica=vrstica.strip("\n")
        splited=vrstica.split(' ')
        for vrednost in splited:
            integerji.append(int(vrednost))
        slovar_k[i]=integerji
        integerji=[]
        i+=1
    file.close()
    for index in slovar_k:
        seznam=slovar_k[index]
        while seznam[0]!=min(seznam):
                sprememba=seznam[-1]
                del seznam[-1]
                seznam.insert(0,sprememba)
    return slovar_k

def mozna_pot(pot,zemljevid):
    seznam_izhodov=[]
    for x in zemljevid:
        if len(zemljevid[x])==1:
            seznam_izhodov.append(x)
    if pot[0] not in seznam_izhodov or pot[-1]not in seznam_izhodov:
        return False
    else:
        if pot[0] in zemljevid[pot[1]]:
            for current,next in zip(pot[1:],pot[2:]):
                if current in seznam_izhodov :
                    return False
                if(current not in zemljevid[next]):
                    return False
            return True
        else:
            return False

def hamiltonova(pot, zemljevid):
    for x in zemljevid:
        if pot.count(x)!= 1:
            if len(zemljevid[x]) != 1:
                return False
    if mozna_pot(pot,zemljevid)== True:
        return True

def navodila(pot, zemljevid):
    gps=[]
    for previous,current, next in zip(pot,pot[1:], pot[2:]):
        gps.append((zemljevid[current].index(next)-zemljevid[current].index(previous))%len(zemljevid[current]))
    return gps

