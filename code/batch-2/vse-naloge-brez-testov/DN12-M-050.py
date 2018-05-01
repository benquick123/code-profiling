def spremeni(seznam):
    nov1=[]

    nov=seznam

    for el in seznam:
        if el!=min(seznam):
            nov.append(el)
        if el==min(seznam):
            break

    preveri = False
    for st in nov:
        if st==min(seznam):
            preveri=True
        if preveri:
            nov1.append(st)

    return nov1



def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    slovar = {}
    stevec=1
    for vrstica in datoteka:
        vr = vrstica.strip()
        seznam = vr.split(" ")

        sezna = list(map(int, seznam))

        nov = spremeni(sezna)

        slovar[stevec]=nov
        stevec=stevec+1

    datoteka.close()
    return slovar

def mozna_pot(pot,zemljevid):

    #prvi del
    for el in zip(pot,pot[1:]):
        if el[0] not in zemljevid[el[1]]:
            return False

    # Ne začne/konča se na vhodih/izhodih
    vhod = pot[0]
    izhod = pot[-1:]

    if len(zemljevid[vhod])>1 or len(zemljevid[izhod[0]])>1 :
        return False

    brez_prvega = pot[1:]
    brez_obeh =brez_prvega[:-1]

    for el in brez_obeh:
        if len(zemljevid[el])==1:
            return False

    return True


def hamiltonova(pot,zemljevid):
    vrni = True
    if not mozna_pot(pot,zemljevid):
        return False


    seznam =[] #seznam krozisc na zemljevidu

    brez_prvega = pot[1:]
    brez_obeh = brez_prvega[:-1]
    vhod = pot[0]
    izhod = pot[-1:]
    izhod = izhod[0]

    for krozisce in zemljevid.keys():
        if len(zemljevid[krozisce])>1:
            seznam.append(krozisce)



    seznam_zacetkov_koncov=[]

    for krozisce in zemljevid.keys():
        if len(zemljevid[krozisce])==1:
            seznam_zacetkov_koncov.append(krozisce)

    for k1 in seznam:
        if k1 not in brez_obeh:
            return False

    if vhod not in seznam_zacetkov_koncov:
        return False
    if izhod not in seznam_zacetkov_koncov:
        return False

    for element in pot:
        if pot.count(element)>1:
            return False


    return True


def navodila(pot,zemljevid):
    prvi=[]
    drugi=[]
    tretji=[]



