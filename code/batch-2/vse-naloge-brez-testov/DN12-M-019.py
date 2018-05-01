

from random import randint
from itertools import permutations
import os

def uredi(seta):
    if not seta:
        return seta
    najmanjsi = min(seta)
    if seta[0] == najmanjsi:
        return seta
    prvi = seta[0]
    if seta[0] != najmanjsi:
        seta.append(prvi)
        seta.remove(seta[0])

        #seta[0] =  seta[-1]
        ##set[0] = prvi
        #print(seta)
    uredi(seta)



def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    vrst = 1
    slover ={}
    for vrstica in datoteka.read().split("\n"):

        seznam= []
        #print(vrstica)

        for element in vrstica.split():
            if not element == "":
                seznam.append(int(element))
        uredi(seznam)
        #print(seznam)
        if seznam != []:
          slover[vrst] = seznam
        vrst += 1

        #zadnja stvar


    return slover

def mozna_pot(pot, zemljevid):

    #poti = preberi(zemljevid)
    pari = zip(pot, pot[1:])
    #print(zemljevid)
    #print(pot)
    #ali iz prva lahjko grem v drugo oz ali ima prva v keh drugo:
    if not (len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1):
        return False

    for prva , druga in pari:
        if prva == druga:#;e grem iz samega sebe v sebe
            return False
        if druga not in zemljevid[prva]:
            return False
    for konec in pot[1:-1]:
        if len(zemljevid[konec]) == 1:
            return False
    return True


#preberi("zemljevid.txt")
def hamiltonova(pot, zemljevid):
    #pot je mo\na
    #vsebuje vsa krozisca
    #nobeno se ne ponovi
    if not mozna_pot(pot, zemljevid):
        return False
    #presek med potjo in key = key
    a = set(pot)
    #for kez in zemljevid:

    b = set( kez for kez in zemljevid.keys() if len(zemljevid[kez]) >1 )        #brez tistih ki niso korzisca
    #print("svsdvsdv", len(b))
    if not  a>=b:
        return False
    if len(pot) != len(b)+2:
        return False
    #print(len(pot))
    return True

def navodila(pot, zemljevid):
    seznam =[]
    pot3 =zip(pot, pot[1:], pot[2:])
    for noter, ven , naprej in pot3:
        #print(noter, ven, naprej)
        #print('Krozisce ', zemljevid[ven])
        #print("indeks od noter ", zemljevid[ven].index(noter))
        #print("indeks od naprej ", zemljevid[ven].index(naprej))
        a=zemljevid[ven].index(noter)
        b=zemljevid[ven].index(naprej)
        if b-a <0:
            seznam.append(abs((b-a) % len(zemljevid[ven])))

        else:
            seznam.append(abs(b-a))

    #print("Seznam je ",seznam)
    return seznam

def prevozi(zacetek, navodila, zemljevid):
    #navodila: 1, 1, 1
    #seznam:  [1, 3, 6, 11, 14, 16, 15]
    seznam = [zacetek]
    seznam.append(zemljevid[seznam[-1]][0])
    for pot in navodila:
        #print('Trenutno sem v ', seznam[-1], 'kroziscu, prisel sem iz ', seznam[-2], "in grem ven v ", pot,"na seznamu ", zemljevid[seznam[-1]])
        indexnoter = zemljevid[seznam[-1]].index(seznam[-2])
        dolzina = len(zemljevid[seznam[-1]])
        popravek = pot+indexnoter
        if popravek >= dolzina:
            popravek = popravek - dolzina
        seznam.append(zemljevid[seznam[-1]][popravek])
        #print('GREM NA', zemljevid[seznam[-1]][popravek])

    #indexven = zemljevid[seznam[-1]].index(seznam[-2])



    return seznam

def sosedi(doslej, zemljevid):
    mnozica = set()
    for st in doslej:
        for element in zemljevid[st]:
            if element not in doslej:
                mnozica.add(element)

    return mnozica

def razdalja(x, y, zemljevid):
    if y in zemljevid[x]:
        return 1
    n=2
    #print(sosedi({x,y}, zemljevid))
    kandidati = sosedi({x}, zemljevid)
    while True:
        if y in sosedi(kandidati, zemljevid):
            return n
        else:
            kandidati =kandidati.union( sosedi(kandidati, zemljevid))
            n+=1

    #neznam z rekurzijo sori, k slascicarim

def najkrajsa_navodila(x, y, zemljevid):
    #slovar key : vrednosti:
    #vse mo\ne poti med dvema uvozoma in najti najkrajso
    print(zemljevid)
    uvozi = [key for key in zemljevid if len(zemljevid[key]) == 1 ]
    print('Uvozi so ', uvozi)
    povezave =permutations(uvozi,2)
    print(povezave)
    pari=[]
    for povezava in povezave:
        if povezava not in pari and str(povezava)[::-1] not in pari:
            pari.append(povezava)

    print(pari)
    najvecja_radalja ={}
    for xx,yy in pari:
        najvecja_radalja[(xx,yy)] = razdalja(xx, yy, zemljevid)-1
    print(najvecja_radalja)
    #generator krizisc
    #pot = [x,y]
    pot = genpoti(x, y, zemljevid)
    pot.append(y)
    pot.insert(0, x)

    print("Pot je ", pot)
    print('Navodila so ' ,navodila(pot, zemljevid))
    return navodila(pot, zemljevid)

def genpoti(x, y, zemljevid):
    print(x)
    print(y)
    #ali imata prvi dve kriziski kaj skupnega
    a = sosedi(zemljevid[x], zemljevid)
    b = sosedi(zemljevid[y], zemljevid)
    print(a)
    print(b)
    print(zemljevid[x]+zemljevid[y])
    print(razdalja(x, y, zemljevid), 'Razdalja je bila')
    preko=[]
    if razdalja(x, y, zemljevid) == 3:
        preko.append(zemljevid[x][0])
        preko.append(zemljevid[y][0])
        print(preko, "Preko")
        return preko
    if
    return 0


    '''
    skupna = list(a & b)
    
    
    
    if y in a:
        skupna = [b]
        skupna.append(y)
        skupna.insert(0, x)
        return skupna
    elif len(skupna) >0:

        skupna.append(zemljevid[y][0])
        skupna.insert(0, zemljevid[x][0])
        
        return skupna

     '''







