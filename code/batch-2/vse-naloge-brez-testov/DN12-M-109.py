def preberi(ime_datoteke):
    i=1
    slovar={}
    with open(ime_datoteke,"r") as file:
        for x in file:
            a=[]
            b= x.split()
            for y in b:
                a.append(int(y))
            b = min(a)
            while a[0] != b:
                a.insert(0,a.pop())
            slovar[i] = a
            i+=1
    file.close()
    return slovar

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[-1]]) > 1 or len(zemljevid[pot[0]]) > 1:
        return False
    x=1
    while x < len(pot):
        if pot[x-1] not in zemljevid[pot[x]]:
            return False
        if len(zemljevid[pot[x]]) == 1 and x != len(pot)-1:
            return False
        x+=1
    return True

def hamiltonova(pot, zemljevid):
    seznam = []
    list = zemljevid.keys()
    for x in list:
        if len(zemljevid[x]) > 1:
            seznam.append(x)
        if pot.count(x) > 1:
            return False
    if mozna_pot(pot, zemljevid) and len(pot) == len(seznam)+2:
        return True

def navodila(pot, zemljevid):
    seznam = []
    x = 1
    while x < len(pot)-1:
        indeks1=zemljevid[pot[x]].index(pot[x-1])
        indeks2=zemljevid[pot[x]].index(pot[x+1])
        seznam.append((indeks2-indeks1)%len(zemljevid[pot[x]]))
        x+=1
    return seznam

def prevozi(zacetek, navodila, zemljevid):
   seznam=[]
   seznam.append(zacetek)
   seznam.append(zemljevid[zacetek][0])
   x = 0
   i = 0
   while x < len(navodila):
       indeks = zemljevid[seznam[-1]].index(seznam[-2])
       if indeks+navodila[x] > len(zemljevid[seznam[-1]])-1:
           seznam.append(zemljevid[seznam[-1]][indeks + navodila[x]-len(zemljevid[seznam[-1]])])
       else:
           seznam.append(zemljevid[seznam[-1]][indeks+navodila[x]])
       x += 1
       i += 1
   return seznam
