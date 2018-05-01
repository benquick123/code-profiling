
def vsa_polja(s, v): #vrne vse točke od (0, 0) do (s, v)
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine): #vrne število min okoli polja (polje samo ne šteje)
    '''sosedi = 0
    if (x-1, y-1) in mine:
        sosedi += 1
    if (x-1, y) in mine:
        sosedi += 1
    if (x-1, y+1) in mine:
        sosedi += 1
    if (x, y-1) in mine:
        sosedi += 1
    if (x, y+1) in mine:
        sosedi += 1
    if (x+1, y-1) in mine:
        sosedi += 1
    if (x+1, y) in mine:
        sosedi += 1
    if (x+1, y+1) in mine:
        sosedi += 1
    return sosedi'''
    return (len([(i, j) for i in range(x-1, x+2) for j in range(y-1, y+2) #dolžina seznama sosednjih polj
                 if (i, j) in mine                                        #ki imajo mine
                 if (i, j) != (x, y)]))                                   #brez trenutnega polja


def najvec_sosedov(mine, s, v): #vrne koordinate polja, ki je obkroženo z največ minami
    '''najvec = 0
    najvec_polje = (0, 0)
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) > najvec: #če ima polje več sosedov kot prejšnji največji
                najvec = sosedov(i, j, mine)
                najvec_polje = (i, j) #se zamenjata
    return najvec_polje'''
    return max({(x, y): sosedov(x, y, mine) for x in range(s) for y in range(v)},           #slovar vseh polj in njihovih sosedov
               key = {(x, y): sosedov(x, y, mine) for x in range(s) for y in range(v)}.get) #vrne ključ največje vrednosti(polje z največ sosedi)
    #slovar = {(x, y): sosedov(x, y, mine) for x in range(s) for y in range(v)} #slovar vseh polj in njihovih sosedov
    #return max(slovar, key=slovar.get)


def brez_sosedov(mine, s, v): #vrne množico polj, ki nimajo na sosednjih poljih nobene mine
    '''brez = set()
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) == 0: #če je brez sosedov
                brez.add((i, j)) #polje dodamo v množico
    return brez'''
    return {(x, y) for x in range(s) for y in range(v) #vrne množico polj
            if sosedov(x, y, mine) == 0}               #ki okoli nimajo nobene mine


def po_sosedih(mine, s, v): #vrne slovar s ključi od 0 do 8, ki vsebujejo množice polj z ustreznim številom sosedov
    '''slovar = {}
    for i in range(9):
        slovar[i] = set() #napolni slovar s praznimi množicami
    for i in range(s):
        for j in range(v):
            slovar[sosedov(i, j, mine)].add((i, j)) #doda polje z 'x' sosedi v ustrezno množico v slovarju
    return slovar'''
    return {i: {(x, y) for x in range(s) for y in range(v) #vrne slovar množic
                if sosedov(x, y, mine) == i}               #kjer so ključi število sosedov
                for i in range(9)}                         #vrednosti pa polja s tolikimi sosedi (če takih polj ni, vrne prazno množico)


########################
# Za oceno 7

def dolzina_poti(pot): #vrne dolžino poti
    '''dolzina = 0
    if pot: #če list ni prazen
        zacetek = pot[0]
        for i in pot[1:]: #vedno primerja s prejšnjim
            dolzina += abs(zacetek[0] - i[0]) #premik vodoravno
            dolzina += abs(zacetek[1] - i[1]) #premik navpično
            zacetek = i #nastavi novo pozicijo
    return dolzina'''
    return sum((abs(x0 - x1)) + abs(y0 - y1)                #vsota razlik med trenutno in naslednjo pozicijo (premik)
               for (x0, y0), (x1, y1) in zip(pot, pot[1:])) #za vse korake na poti


def varen_premik(x0, y0, x1, y1, mine): #vrne False, če ob premiku naletimo na mino (drugače True)
    '''if y0 == y1: #vodoraven premik
        if x0 < x1: #v desno
            for i in range(x0, x1+1):
                if (i, y0) in mine: #če je na poti mina
                    return False #R.I.P.
        else: #v levo
            for i in range(x1, x0+1):
                if (i, y0) in mine:
                    return False
    if x0 == x1: #navpičen premik
        if y0 < y1: #v desno
            for i in range(y0, y1+1):
                if (x0, i) in mine:
                    return False
        else: #v desno
            for i in range(y1, y0+1):
                if (x0, i) in mine:
                    return False
    return True'''
    return [(x, y) for x in range(min(x0, x1), max(x0+1, x1+1)) #vrne True, če je seznam polj z minami na poti prazen
            for y in range(min(y0, y1), max(y0+1, y1+1))        #min() in max(), ker ne vemo ali se premikamo gor ali dol (x0 je lahko manjši kot x1)
            if (x, y) in mine] == []                            #pri max() je +1, zaradi indeksiranja


def varna_pot(pot, mine): #vrne False, če po poti naletimo na mino (drugače True)
    '''if pot: #če list ni prazen
        if pot[0] in mine: #in če ne začnemo na mini
            return False
        zacetek = pot[0]
        for i in pot[1:]: #gremo po poti
            if not varen_premik(zacetek[0], zacetek[1], i[0], i[1], mine): #če je kjerkoli na poti mina
                return False #ded
            zacetek = i #nova pozicija
    return True'''
    return True if pot == []\
            else False if pot[0] in mine\
            else all([varen_premik(x0, y0, x1, y1, mine)  #vrne True, če so vsi premiki po poti varni (brez min)
            for (x0, y0), (x1, y1) in zip(pot, pot[1:])]) #True, če je pot prazna in False, če je začetno polje mina


########################
# Za oceno 8

def polje_v_mine(polje): #vrne množico koordinat polj z minami, ter širino in višino polja
    mreza = polje.split(' ') #razdeli polje po vrsticah
    sirina = 0 #x
    visina = 0 #y
    mine = set()
    for i in mreza: #i = vrstica
        if i: #če ni prazna vrstica, lahko resetira širino in prišteje višino (problem pri i = [] -> širina = 0, višina 1 preveč)
            sirina = 0
            for j in i: #j = stolpec
                if j == 'X': #če je na polju 'X'
                    mine.add((sirina, visina)) #zabeleži mino
                sirina += 1
            visina += 1
    return (mine, sirina, visina)


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi): #navodila za pot pretvori v seznam terk, ki kažejo premik po koordinatnem sistemu
    smer = 0 #0 = gor, 1 = desno, 2 = dol, 3 = levo (v smeri urinega kazalca)
    pot = [(0, 0)]
    x = 0 #x in y ne kot tuple (0, 0), saj se terk ne da spreminjati
    y = 0
    for i in ukazi.split():
        if i == 'DESNO': #obrat
            smer += 1
            smer = abs(smer % 4) #poskrbi, da ne gre pod 0 ali preko 3
        if i == 'LEVO': #obrat
            smer -= 1
            smer = abs(smer % 4)
        if i != 'DESNO' and i != 'LEVO': #premik (samo else ne dela)
            if smer == 0: #gor
                y -= int(i)
            if smer == 1: #desno
                x += int(i)
            if smer == 2: #dol
                y += int(i)
            if smer == 3: #levo
                x -= int(i)
            pot.append((x, y)) #v seznam pripne lokacijo po premiku
    return pot


def zapisi_pot(pot): #pot pretvori v ukaze
    navodila = []
    trenutno_polje = pot[0]
    smer = 0 #0 = gor, 1 = desno, 2 = dol, 3 = levo
    for i in pot[1:]:
        if trenutno_polje[0] == i[0]: #ni spremembe po x
            if trenutno_polje[1] < i[1]: #premik dol
                while smer != 2: #dokler ni poravnan v pravo smer
                    smer += 1
                    smer = smer % 4
                    navodila.append('DESNO') #se obrača v desno
                navodila += str(i[1] - trenutno_polje[1]) #in doda dolžino premika
                trenutno_polje = i #po premiku ponastavimo trenutno polje
            if trenutno_polje[1] > i[1]: #gor
                while smer != 0:
                    smer += 1
                    smer = smer % 4
                    navodila.append('DESNO')
                navodila += str(trenutno_polje[1] - i[1])
                trenutno_polje = i
        if trenutno_polje[1] == i[1]: #ni spremembe po y
            if trenutno_polje[0] < i[0]: #desno
                while smer != 1:
                    smer += 1
                    smer = smer % 4
                    navodila.append('DESNO')
                navodila += str(i[0] - trenutno_polje[0])
                trenutno_polje = i
            if trenutno_polje[0] > i[0]: #levo
                while smer != 3:
                    smer += 1
                    smer = smer % 4
                    navodila.append('DESNO')
                navodila += str(trenutno_polje[0] - i[0])
                trenutno_polje = i
    return ' '.join(navodila)


########################
#Testi (ne spreminjaj)
