

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







import unittest

class Test06(unittest.TestCase):
    maxDiff = 100000

    def test_01_preberi(self):
        self.assertEqual(
            preberi("zemljevid.txt"),
            {1: [3],
             2: [4],
             3: [1, 8, 7, 6, 4],
             4: [2, 3, 6, 5],
             5: [4, 11, 10],
             6: [3, 11, 4],
             7: [3, 8, 11],
             8: [3, 16, 9, 7],
             9: [8, 16, 14, 11],
             10: [5, 11, 13],
             11: [5, 6, 7, 9, 14, 10],
             12: [13],
             13: [10, 14, 12],
             14: [9, 16, 13, 11],
             15: [16],
             16: [8, 15, 14, 9]})

        fname = "z{:05}.bla".format(randint(10000, 99999))
        with open(fname, "w") as f:
            f.write("2\n3 1\n2")
        try:
            self.assertEqual(preberi(fname), {1:[2], 2: [1, 3], 3: [2]})
        finally:
            try:
                os.remove(fname)
            except:
                print("Ne morem pobrisati {}. (Je na Dropboxu?) Briši sam(a).".format(fname))

    def test_02_mozna_pot(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertTrue(mozna_pot([1, 3, 7, 3, 4, 2], zemljevid))
        self.assertTrue(mozna_pot([1, 3, 7, 3, 4, 2][::-1], zemljevid))
        self.assertTrue(mozna_pot([1, 3, 7, 3, 4, 5, 4, 3, 1], zemljevid))
        self.assertTrue(mozna_pot([1, 3, 7, 3, 4, 5, 4, 3, 1][::-1], zemljevid))
        self.assertTrue(mozna_pot([1, 3, 8, 16, 15], zemljevid))
        self.assertTrue(mozna_pot([1, 3, 8, 16, 15][::-1], zemljevid))
        self.assertTrue(mozna_pot([15, 16, 15], zemljevid))

        # Ne začne/konča se na vhodih/izhodih
        self.assertFalse(mozna_pot([1, 3, 7, 11, 14, 16], zemljevid))
        self.assertFalse(mozna_pot([3, 7, 11, 14, 16, 15], zemljevid))

        # Vmes gre ven
        self.assertFalse(mozna_pot([1, 3, 6, 4, 2, 4, 5, 11, 14, 13, 12], zemljevid))
        self.assertFalse(mozna_pot([1, 3, 6, 4, 2, 2, 4, 5, 11, 14, 13, 12], zemljevid))

        # Ponovi eno križišče
        self.assertFalse(mozna_pot([1, 3, 8, 8, 16, 15], zemljevid))

        # Ni povezave
        self.assertFalse(mozna_pot([1, 3, 16, 15], zemljevid))
        self.assertFalse(mozna_pot([1, 15], zemljevid))

        zemljevid2 = {1: [2], 2: [1, 3], 3: [2]}
        self.assertTrue(mozna_pot([1, 2, 3], zemljevid2))
        self.assertFalse(mozna_pot([1, 3], zemljevid2))

        zemljevid2 = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
        self.assertTrue(mozna_pot([1, 2, 3, 4], zemljevid2))
        self.assertTrue(mozna_pot([4, 3, 2, 1], zemljevid2))
        self.assertFalse(mozna_pot([1, 3, 4], zemljevid2))
        self.assertFalse(mozna_pot([1, 4], zemljevid2))

    def test_03_hamiltonova(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertTrue(hamiltonova([1, 3, 7, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12], zemljevid))
        self.assertTrue(hamiltonova([1, 3, 7, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12][::-1], zemljevid))

        # Ena manjka
        self.assertFalse(hamiltonova([1, 3, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12], zemljevid))

        # Ni začetka/konca
        self.assertFalse(hamiltonova([3, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12], zemljevid))
        self.assertFalse(hamiltonova([1, 3, 7, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13], zemljevid))

        # Ponavljenje
        self.assertFalse(hamiltonova([1, 3, 8, 16, 9, 14, 11, 6, 4, 5, 10, 11, 14, 13, 12], zemljevid))
        self.assertFalse(hamiltonova([1, 3, 7, 8, 16, 9, 14, 11, 6, 3, 4, 5, 10, 13, 12], zemljevid))

        zemljevid2 = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
        self.assertTrue(hamiltonova([1, 2, 3, 4], zemljevid2))
        self.assertTrue(hamiltonova([4, 3, 2, 1], zemljevid2))
        self.assertFalse(hamiltonova([1, 2, 4], zemljevid2))


class Test07(unittest.TestCase):
    maxDiff = 100000

    def test_01_navodila(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertEqual(navodila([1, 3, 8, 16, 15], zemljevid), [1, 1, 1])
        self.assertEqual(navodila([1, 3, 6, 4, 2], zemljevid), [3, 2, 2])
        self.assertEqual(navodila([1, 3, 6, 11, 14, 16, 15], zemljevid), [3, 1, 3, 2, 3])
        self.assertEqual(navodila([12, 13, 14, 11, 9, 8, 7, 3, 4, 2], zemljevid), [2, 1, 5, 1, 1, 2, 2, 3])
        self.assertEqual(navodila([2, 4, 2], zemljevid), [0])
        self.assertEqual(navodila([15, 16, 14, 11, 9, 16, 14, 11, 9, 16, 15], zemljevid), [1, 2, 5, 2, 3, 2, 5, 2, 2])


class Test08(unittest.TestCase):
    maxDiff = 100000

    def test_01_prevozi(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertEqual(prevozi(1, [1, 1, 1], zemljevid), [1, 3, 8, 16, 15])
        self.assertEqual(prevozi(1, [3, 2, 2], zemljevid), [1, 3, 6, 4, 2])
        self.assertEqual(prevozi(1, [3, 1, 3, 2, 3], zemljevid), [1, 3, 6, 11, 14, 16, 15])
        self.assertEqual(prevozi(12, [2, 1, 5, 1, 1, 2, 2, 3], zemljevid), [12, 13, 14, 11, 9, 8, 7, 3, 4, 2])
        self.assertEqual(prevozi(2, [0], zemljevid), [2, 4, 2])
        self.assertEqual(prevozi(15, [1, 2, 5, 2, 3, 2, 5, 2, 2], zemljevid), [15, 16, 14, 11, 9, 16, 14, 11, 9, 16, 15])

class Test09(unittest.TestCase):
    maxDiff = 100000

    def test_01_sosedi(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertEqual(sosedi({15}, zemljevid), {16})
        self.assertEqual(sosedi({15, 16}, zemljevid), {14, 9, 8})
        self.assertEqual(sosedi({15, 16, 14, 9, 8}, zemljevid), {3, 7, 11, 13})
        self.assertEqual(sosedi({15, 16, 14, 9, 8, 3, 7, 11, 13}, zemljevid), {1, 4, 6, 5, 10, 12})
        self.assertEqual(sosedi({15, 16, 14, 9, 8, 3, 7, 11, 13, 1, 4, 6, 5, 10, 12}, zemljevid), {2})
        self.assertEqual(sosedi({15, 16, 14, 9, 8, 3, 7, 11, 13, 1, 4, 6, 5, 10, 12, 2}, zemljevid), set())

        self.assertEqual(sosedi({6}, zemljevid), {4, 3, 11})
        self.assertEqual(sosedi({6, 4, 3, 11}, zemljevid), {2, 5, 1, 7, 8, 9, 14, 10})

    def test_02_razdalja(self):
        zemljevid = preberi("zemljevid.txt")
        self.assertEqual(razdalja(15, 16, zemljevid), 1)

        self.assertEqual(razdalja(15, 14, zemljevid), 2)
        self.assertEqual(razdalja(15, 9, zemljevid), 2)
        self.assertEqual(razdalja(15, 8, zemljevid), 2)

        self.assertEqual(razdalja(15, 7, zemljevid), 3)
        self.assertEqual(razdalja(15, 13, zemljevid), 3)

        self.assertEqual(razdalja(15, 5, zemljevid), 4)
        self.assertEqual(razdalja(15, 10, zemljevid), 4)

        self.assertEqual(razdalja(15, 2, zemljevid), 5)

        self.assertEqual(razdalja(6, 4, zemljevid), 1)
        self.assertEqual(razdalja(6, 5, zemljevid), 2)
        self.assertEqual(razdalja(6, 10, zemljevid), 2)
        self.assertEqual(razdalja(6, 13, zemljevid), 3)
        self.assertEqual(razdalja(6, 12, zemljevid), 4)


class Test10(unittest.TestCase):
    maxDiff = 100000

    def test_01_najkrajsa_pot(self):
        zemljevid = preberi("zemljevid.txt")
#        self.assertEqual(najkrajsa_navodila(1, 15, zemljevid), [1, 1, 1])
        self.assertEqual(najkrajsa_navodila(1, 2, zemljevid), [4, 3])
        self.assertEqual(najkrajsa_navodila(2, 15, zemljevid), [1, 2, 1, 1])
        self.assertEqual(najkrajsa_navodila(2, 12, zemljevid), [3, 2, 2, 2])
        self.assertEqual(najkrajsa_navodila(15, 12, zemljevid), [1, 1, 1])

        self.assertEqual(najkrajsa_navodila(15, 1, zemljevid), [3, 3, 4])
        self.assertEqual(najkrajsa_navodila(2, 1, zemljevid), [1, 1])
        self.assertEqual(najkrajsa_navodila(15, 2, zemljevid), [3, 3, 3, 3])
        self.assertEqual(najkrajsa_navodila(12, 2, zemljevid), [1, 1, 1, 1])
        self.assertEqual(najkrajsa_navodila(12, 15, zemljevid), [2, 3, 3])

        navodila = najkrajsa_navodila(1, 12, zemljevid)
        self.assertEqual(len(navodila), 5)
        self.assertEqual(prevozi(1, navodila, zemljevid)[-1], 12)

        navodila = najkrajsa_navodila(12, 1, zemljevid)
        self.assertEqual(len(navodila), 5)
        self.assertEqual(prevozi(12, navodila, zemljevid)[-1], 1)


if __name__ == "__main__":
    unittest.main()
