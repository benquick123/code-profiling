# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    """
    Generiraj vse koordinate (x, y) za polje s podano širino in višino
    Args:
        s (int): širina
        v (int): višina

    Returns:
        generator parov polj
    """
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    min = 0
    for ena, druga in mine:
        if x-1<=ena<= x+1 and y-1 <= druga <= y+1:
            min+=1
        if ena==x and druga==y:
            min-=1
    return min
def sosedov(x, y, mine):
    """
    Vrni število sosedov polja s koordinatami `(x, y)` na katerih je mina.
    Polje samo ne šteje.

    Args:
        x (int): koordinata x
        y (int): koordinata y
        mine (set of tuple of int): koordinate min

    Returns:
        int: število sosedov
    """
    return sum([1 for koorx, koory in mine
              if x-1 <= koorx <= x+1 and y-1 <= koory <= y+1
                                  and (koorx, koory) != (x, y)])

def najvec_sosedov(mine, s, v):

    najvec = 0
    z_najvec = ()

    for x in range(s):
        for y in range(v):
            koliko = sosedov(x, y, mine)
            if koliko >= najvec:
                najvec = koliko
                z_najvec = x, y
    return z_najvec

def brez_sosedov(mine, s, v):
    varna = set()
    for x in range(s):
        for y in range(v):
            koliko = sosedov(x, y, mine)
            if koliko == 0:
                varna.add((x, y))
    return varna
def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}


def po_sosedih(mine, s, v):
    """
    Vrni slovar, katerega ključi so možna števila sosednjih polj z minami
    (torej števila od 0 do 8), vrednosti pa množice koordinat polj s toliko
    sosedami.
    """

    min = {}
    for i in range(9):
        min[i] = set()
    for x in range(s):
        for y in range(v):
            koliko = sosedov(x, y, mine)
            for i in min:
                if i == koliko:
                    min[i].add((x, y))
    return min
def po_sosedih(mine, s, v):
    return {i: {(x, y) for (x, y) in vsa_polja(s, v) if i == sosedov(x, y, mine)} for i in range(9)}

########################
# Za oceno 7

def dolzina_poti(pot):
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    """
    potka = 0
    korak = 0
    for i in range(len(pot)-1):
        x, y = pot[i]
        xi, yi = pot[i+1]
        if x!=xi:
            korak = xi-x
        if y!=yi:
            korak = yi-y
        potka+=abs(korak)
    return potka
from math import sqrt


def dolzina_poti(pot):
    return sum(abs(x1 - x0) + abs(y1 - y0) for (x0, y0), (x1, y1) in zip(pot, pot[1:]))


def varen_premik(x0, y0, x1, y1, mine):
    if (x0, y0) in mine or (x1, y1) in mine:
        return False
    if x0 < x1:
        for x in range(x0, x1):
            if (x, y1) in mine:
                return False
    else:
        for x in range(x1, x0):
            if (x, y1) in mine:
                return False
    if y0 < y1:
        for y in range(y0, y1):
            if (x0, y) in mine:
                return False
    else:
        for y in range(y1, y0):
            if (x0, y) in mine:
                return False
    return True

def varna_pot(pot, mine):
    for korak in pot:
        if korak in mine:
            return False
    for i in range(len(pot)-1):
        x0, y0 = pot[i]
        x1, y1 = pot[i+1]
        if not varen_premik(x0, y0, x1, y1, mine):
            return False

    return True

########################
# Za oceno 8

def polje_v_mine(polje):
    """
    Vrni koordinate min v podanem polju.

    Niz polje opisuje polje tako, da so vodoravne "vrstice" polja ločene s
    presledki. Prosta polja so označena z znako `.`, mine z `X`.

    Args:
        polje (str): polje

    Returns:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja.
    """
    mine = set()
    v = 0
    s = 0
    polja = polje.split(" ")
    for polje in polja:
        s = len(polje)
        v += 1
        for i, e in enumerate(polje):
            if e == "X":
                x = i
                y = v-1
                mine.add((x, y))
    return mine, s, v




########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    potka = [(0, 0)]
    smer = [0,1,2,3]
    X = 0
    for i, ukaz in enumerate(ukazi.split("\n")):
        if ukaz == "LEVO" or ukaz == "DESNO":
                if ukaz == "LEVO":
                    for n, s in enumerate(smer):
                        if n == X:
                            X = abs(s - 1)
                            break
                elif ukaz == "DESNO":
                    for n, s in enumerate(smer):
                        if n == X:
                            X = abs(s + 1)
                            if X == 4:
                                X = 0
                            break
        else:
            x = potka[-1][0]
            y = potka[-1][1]
            if X == 0:            #GOR
                x1 = ukaz
                potka.append((x, y-int(x1)))
            if X == 1:           #DESNO
                y2 = ukaz
                potka.append((x+int(y2), y))
            if X == 2:             #DOL
                x3 = ukaz
                potka.append((x, y+int(x3)))
            if X == 3:         #dlevo
                y4 = ukaz
                potka.append((x-int(y4), y))
    return potka

def zapisi_pot(pot):
    navodila = []
    smer = [0,1,2,3]
    X = 0
    for i, (x, y) in enumerate(pot):

        if (x, y) == (0, 0):
            navodila.append("DESNO")
        elif i != len(pot)-1:
            x1, y1 = pot[i+1]
            x0, y0 = pot[i - 1]
            for n, s in enumerate(smer):
                if n == X:
                    if x == 0:
                        nevem = 0


                if x1 != x or i <= 1:
                    if x0 < x :
                        navodila.append("DESNO")
                    else:
                        navodila.append("LEVO")
            if x0 != x:
                navodila.append(str(x - x0))
            if y0 != y:
                navodila.append(str(y-y0))
                for n, s in enumerate(smer):
                    if n == X:
                        nevem = 0


                if y != y1 or i <= 1:
                    if y0 < y:
                        navodila.append("LEVO")
                    else:
                        navodila.append("DESNO")
        elif i == len(pot)-1:
            x1, y1 = pot[i - 1]
            if x != x1:
                navodila.append(str(x-x1))
            elif y != y1:
                navodila.append(str(y-y1))
    return "\n".join(navodila)








