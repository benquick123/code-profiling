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

def sosedi(x,y):
    a = list((a,b) for a in (x-1, x, x+1) for b in (y-1, y, y+1))
    a.remove((x,y))
    return a



########################
# Za oceno 6

def sosedov(x, y, mine):
    stevilo = 0
    a = sosedi(x,y)
    for b in a:
        if b in mine:
            stevilo += 1
    return stevilo

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


def najvec_sosedov(mine, s, v):
    najvec = 0
    najvecja = (0,0)
    for x,y in vsa_polja(s,v):
        z = sosedov(x,y,mine)
        if z > najvec:
            najvec = z
            najvecja = (x,y)
    return najvecja
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """


def brez_sosedov(mine, s, v):
    a = set([])
    for x,y in vsa_polja(s,v):
        if sosedov(x,y,mine) == 0:
            a.add((x,y))
    return a

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


def po_sosedih(mine, s, v):
    rezultat = dict([])
    polja = list(vsa_polja(s,v))
    for a in range(0,9):
        print(a)
        rezultat[a] = {}
        proto = set([])
        for x,y in polja:
            print(x,y)
            if sosedov(x,y,mine) == a:
                proto.add((x,y))
        rezultat[a] = proto
    return rezultat



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


########################
# Za oceno 7

def dolzina_poti(pot):
    if not pot:
        return 0
    x2,y2 = pot.pop(0)
    rezultat = 0
    for x,y in pot:
        rezultat += abs(y-y2) + abs(x-x2)
        x2,y2 = x,y
    return  abs(rezultat)

    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    potx = list(range(x0,x1+1)) if x0 < x1 else list(range(x1,x0+1))
    poty = list(range(y0,y1+1)) if y0 < y1 else list(range(y1,y0+1))
    vmesni = set()
    if x1 == x0:
        for i in poty:
            vmesni.add((x0,i))
    elif y1 == y0:
        for i in potx:
            vmesni.add((i,y0))
    if vmesni.intersection(mine) == set():
        return True
    else:
        return False



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


def varna_pot(pot, mine):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    a = list(zip(pot, pot[1::]))
    if not pot:
        return True
    if len(pot) == 1:
        if pot[0] in mine:
            return False
        else:
            return True
    for x,y in a:
        x0,y0 = x
        x1,y1 = y
        if not varen_premik(x0,y0,x1,y1,mine):
            return False
    return True
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """


########################
# Za oceno 8

def polje_v_mine(polje):
    a = polje.split(" ")
    b = set()
    maxx = 0
    countx = 0
    county = 0
    for y in a:
        for x in y:
            if x == "X":
                b.add((countx,county))
            countx += 1
        if y:
            county += 1
        countx = 0
        if len(y) > maxx:
            maxx = len(y)
    return (b,maxx,county)





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


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """


