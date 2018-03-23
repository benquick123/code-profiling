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

#def sosedi(x, y):
#    return ([(a, b) for a in range(x-1, x+2) for b in range(y-1, y+2) if (a, b) != (x,y)])

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
    return len([s for s in [(a, b) for a in range(x-1, x+2) for b in range(y-1, y+2) if (a, b) != (x,y)] if s in mine])

def najvec_sosedov(mine, s, v):
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """
    return max({(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}, key={(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}.get)



def brez_sosedov(mine, s, v):
    """
    Vrni množico koordinat polj brez min na sosednjih poljih. Polje samo lahko
    vsebuje mino.

    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        set of tuple: polja brez min na sosednjih poljih
    """




    return {(x, y) for (x,y) in {(x,y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)} if {(x,y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}[(x, y)] == 0}

def po_sosedih(mine, s, v):
    """
    Vrni slovar, katerega ključi so možna števila sosednjih polj z minami
    (torej števila od 0 do 8), vrednosti pa množice koordinat polj s toliko
    sosedami.

    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        dict: (glej zgoraj)
    """

    #sez = collections.defaultdict(set)

    #for i in range(9):
    #    mnozica = set()
    #    for x, y in vsa_polja(s, v):
    #        st = sosedov(x, y, mine)
    #        if st == i:
    #            mnozica.add((x, y))
    #    sez[i] = mnozica
    #return sez

    return {i: {(x, y) for (x, y) in vsa_polja(s, v) if sosedov(x, y, mine) == i} for i in range(9) }


   # return {i: (x, y) for x, y in vsa_polja(s, v) for i in range(9) if {(x,y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}[(x, y)] == i}



########################
# Za oceno 7

def dolzina_poti(pot):
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """
    return sum([(abs(pot[e][0] - pot[e + 1][0])) + abs(pot[e][1] - pot[e + 1][1]) for e in range(len(pot)) if e + 2 <= len(pot)])


def varen_premik(x0, y0, x1, y1, mine):
    """
    Vrni `True`, če je pomik z (x0, y0) and (x1, y1) varen, `False`, če ni.

    Args:
        x0 (int): koordinata x začetnega polja
        y0 (int): koordinata y začetnega polja
        x1 (int): koordinata x končnega polja
        y1 (int): koordinata y končnega polja
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je premik varen, `False`, če ni.
    """
    return {(x0, y0 + e + 1) for e in range(y1-y0) if y1-y0 > 0} & mine == set() and {(x0, y0 - e - 1) for e in range(y0-y1) if y1-y0 < 0} & mine == set() and {(x0 + f + 1, y0) for f in range(x1-x0) if x1-x0 > 0} & mine == set() and {(x0 - f - 1, y0) for f in range(x0-x1) if x1-x0 < 0} & mine == set() and (x0, y0) not in mine and (x1,y1) not in mine

#    iksi = set()
#    ipsi = set()
#    if y1-y0 > 0 or x1-x0 > 0:
#        for e in range(y1-y0):
#            ipsi.add((x0, y0 + e +1))
#        for f in range(x1-x0):
#            iksi.add((x0 + f + 1, y0))
#    if y1-y0 < 0 or x1-x0 < 0:
#        for e in range(y0-y1):
#            ipsi.add((x0, y0 - e - 1))
#        for f in range(x0-x1):
#            iksi.add((x0 - f - 1, y0))

#    return iksi & mine == set() and ipsi & mine == set() and (x0,y0) not in mine and (x1,y1) not in mine

import itertools

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """


    return False not in [varen_premik(a[0], a[1], b[0], b[1], mine) for a, b in [(a, b) for a, b in zip(pot[:-1], pot[1:])]] and set(pot) & mine == set()



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
    m = set()
    for a, b in enumerate(polje.split()):
        for c, d in enumerate(b):
            if d == "X":
                m.add((c, a))
    return m, len(polje.split()[0]), len(polje.split())


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """
    u = ukazi.split()
    smer = 0 #0 - gor, 1 - desno, 2 - dol, 3 - levo
    s = [(0, 0)]
    p = (0, 0) # 0 - x, 1 - y
    for ukaz in u:
        if smer == 4:
            smer = 0
        if smer == -1:
            smer = 3
        if ukaz == "DESNO":
            smer += 1
        if ukaz == "LEVO":
            smer -= 1
        if ukaz == "1" or ukaz == "2" or ukaz == "3" or ukaz == "4" or ukaz == "5" or ukaz == "6" or ukaz == "7" or ukaz == "8" or ukaz == "9" or ukaz == "10":
            ukaz = int(ukaz)
            if smer == 0:
                p = (p[0], p[1] - ukaz)
            if smer == 1:
                p = (p[0] + ukaz, p[1])
            if smer == 2:
                p = (p[0], p[1] + ukaz)
            if smer == 3:
                p = (p[0] - ukaz, p[1])
            s.append(p)
    return s

def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    ukazi = []
    smer = 0 # 0 - gor, 1 - desno, 2 - dol, 3 - levo
    p = pot[0]
    for i in range(len(pot) - 1):
        if smer == 4:
            smer = 0
        if pot[i][0] < pot[i+1][0]:
            while smer != 1:
                smer += 1
                ukazi.append("DESNO")
                if smer == 4:
                    smer = 0
            ukazi.append(str(pot[i+1][0] - pot[i][0]))
        if pot[i][1] < pot[i+1][1]:
            while smer != 2:
                smer += 1
                ukazi.append("DESNO")
                if smer == 4:
                    smer = 0
            ukazi.append(str(pot[i+1][1] - pot[i][1]))
        if pot[i][0] > pot[i+1][0]:
            while smer != 3:
                smer += 1
                ukazi.append("DESNO")
                if smer == 4:
                    smer = 0
            ukazi.append(str(pot[i][0] - pot[i+1][0]))
        if pot[i][1] > pot[i+1][1]:
            while smer != 0:
                smer += 1
                ukazi.append("DESNO")
                if smer == 4:
                    smer = 0
            ukazi.append(str(pot[i][1] - pot[i+1][1]))
    return " ".join(ukazi)
