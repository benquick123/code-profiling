from collections import deque



def preberi(file):
    f = open(file, "r")

    dict = {}
    st = 1
    for line in f.readlines():
        line = line.replace("\n", "")
        vrsta = line.split(" ")

        vrstica = list(map(int, vrsta))

        minim = vrstica[0]
        for i in vrstica:
            if i < minim:
                minim = i
        index_min = vrstica.index(minim) * (-1)

        items = deque(vrstica)
        items.rotate(index_min)

        vrstica2 = list(items)




        dict.update({st: vrstica2})
        st += 1

    return dict

#print(preberi("zemljevid.txt"))

def mozna_pot(pot, zemljevid):
    #skillz
    ne_ponovi = True
    st = 0
    for i in pot:
        if st != 0 and pot[st] == pot[st-1]:
            ne_ponovi = False

        st += 1

    vmes_ni_kon_povezav = True
    st = 0
    for krozisce in pot:
        if st != 0 and st != len(pot) - 1 and len(zemljevid.get(krozisce)) == 1:
            vmes_ni_kon_povezav = False
        st += 1

    mozno_prevoziti = True
    st = 0
    for i in range(len(pot)-1):
        if i != len(pot) - 1 and pot[i+1] not in zemljevid.get(pot[i]):
            mozno_prevoziti = False

    if (len(zemljevid.get(pot[0])) == 1) and (len(zemljevid.get(pot[-1])) == 1) and ne_ponovi == True and vmes_ni_kon_povezav == True and mozno_prevoziti == True:
        return True

    else:
        return False

def hamiltonova(pot, zemljevid):

    je_mozna = True
    if mozna_pot(pot, zemljevid) == False:
        je_mozna = False

    ne_ponovi = True
    if len(set(pot)) != len(pot):
        ne_ponovi = False



    gre_cez_vse = True

    st_koncnih = 0
    for krozisce in zemljevid.keys():
        if len(zemljevid.get(krozisce)) == 1:
            st_koncnih += 1

    if len(pot) != len(zemljevid.keys())-st_koncnih+2:
        gre_cez_vse = False

    x = len(pot)
    y = len(zemljevid)

    if je_mozna== True and ne_ponovi == True and gre_cez_vse == True:
        return True
    else:
        return False

zemljevid = {1: [3],
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
             16: [8, 15, 14, 9]}

def navodila(pot, zemljevid):
    navodila = []

    for i in range(len(pot) - 1):

        #dobi trenutno krizisce
        krizisce = pot[i]
        #dobi odseke trenutnega krizisca
        odseki = zemljevid.get(krizisce)

        #ce krizisce ni prvo ali zadnje
        if i > 0 and i < (len(pot) - 1):
            vstopni_indeks = odseki.index(pot[i - 1])

            #pretvori odseke v deque objekt za lazje obracanje
            deque_odseki = deque(odseki)
            #zasuci prasico za vstopni index nazaj
            deque_odseki.rotate(vstopni_indeks * (-1))

            #nazaj v array
            zasukani_odseki = list(deque_odseki)

            stevec = 0
            for o in zasukani_odseki:
                if o == pot[i+1]:
                    navodila.append(stevec)
                stevec += 1
    return navodila


print(navodila([1, 3, 6, 4, 2], zemljevid))

def prevozi(zacetek, navodila, zemljevid):
    #dobi osnovno krožisce do katerega pridemo iz zacetka
    krozisce = zemljevid.get(zacetek)[0]

    #arrayu prevoz deklarira prva dva elementa: zacetek in prvo kroz
    prevoz = [zacetek, krozisce]

    #zato ker je index zadnjega elementa 1
    stevec_krozisc = 1
    for i in range(len(navodila)):
        ukaz = navodila[i]
        #dobi zadnji kurcov element
        odseki = zemljevid.get(prevoz[stevec_krozisc])
        #index osnovnega krozisca
        vstopni_indeks = odseki.index(prevoz[stevec_krozisc - 1])

        # pretvori odseke v deque objekt za lazje obracanje
        deque_odseki = deque(odseki)
        # zasuci prasico za vstopni index nazaj
        deque_odseki.rotate(vstopni_indeks * (-1))

        # nazaj v array
        zasukani_odseki = list(deque_odseki)

        prevoz.append(zasukani_odseki[ukaz])

        stevec_krozisc += 1
        #print("dick")
    print(prevoz)
    return prevoz
#print(prevozi(1, [3, 2, 2], zemljevid))


def sosedi(doslej, zemljevid):

    povezani = []

    for krozisce in doslej:
        povezave = zemljevid.get(krozisce)
        for p in povezave:
            if p not in doslej:
                povezani.append(p)

    sos = set(povezani)
    return sos

def razdalja(x, y, zemljevid):

    st = 0

    mnozica = {x}

    while y not in mnozica:
        mnozica.update(sosedi(mnozica, zemljevid))
        st += 1

    return st

