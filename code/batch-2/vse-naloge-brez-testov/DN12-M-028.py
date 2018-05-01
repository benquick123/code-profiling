def uredi(seznam):
    najmanjsa=min(seznam)
    index=seznam.index(najmanjsa)
    nov_seznam=[]
    for element in seznam:
        if seznam.index(element)>=index:
            nov_seznam.append(element)
    for element in seznam:
        if seznam.index(element)<index:
            nov_seznam.append(element)
    return nov_seznam

def preberi(ime_datoteke):
    zemljevid=open(ime_datoteke,"r")
    n=1
    d={}
    l=[]
    for vrstica in zemljevid:
        vrstica=vrstica.split("\n")[0]
        vrstica=vrstica.split(" ")
        for stevilka in vrstica:
            if stevilka.isdigit():
                l.append(int(stevilka))
        d[n]=uredi(l)
        n=n+1
        l=[]
    return d



def koncna_povezava(zemljevid):
    n=1
    seznam=[]
    pojavi_enkrat=[]
    while n in zemljevid:
        if len(zemljevid[n])==1:
            seznam.append(n)
        n=n+1
    return seznam

def nima_dvojna_krozisca(pot):
    for element in pot:
        n=0
        c=0
        while n<len(pot)-1:
            if pot[n]==element:
                c=c+1
            if c>=2:
                return False
            n=n+1
    return True

zemljevid=preberi("zemljevid.txt")
def mozna_pot(pot,zemljevid):
    krajisca=koncna_povezava(zemljevid)
    if pot[0] not in krajisca or pot[len(pot)-1] not in krajisca:
        return False
    n=1
    while n<len(pot)-2:
        if pot[n] in krajisca:
            return False
        if pot[n]==pot[n+1]:
            return False
        n=n+1
    n=0
    while n<len(pot)-1:
        if pot[n] not in zemljevid[pot[n+1]]:
            return False
        n=n+1
    return True

def uporabljeno_vsako_krozisce(pot,zemljevid):
    vsa_krozisca=[]
    krajisca=koncna_povezava(zemljevid)
    n=1
    while n in zemljevid:
        vsa_krozisca.append(zemljevid[n])
        n=n+1
    if len(pot)==len(vsa_krozisca)-len(krajisca)+2:
        return True
    else:
        return False

def hamiltonova(pot,zemljevid):
    return mozna_pot(pot,zemljevid) and nima_dvojna_krozisca(pot) and uporabljeno_vsako_krozisce(pot,zemljevid)

