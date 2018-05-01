# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
import math
import collections
import itertools
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
    stevec = 0
    for x1,y1 in mine:
        if abs(x1-x) == 1 and abs(y1-y) == 1 or 0 < math.hypot(x1-x, y1-y) < math.sqrt(2):
            stevec = stevec + 1
    return stevec

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
    o = collections.defaultdict(list)
    for x,y in vsa_polja(s,v):
        o[sosedov(x,y,mine)].extend((x,y))
        a = o[max(o, key=int)]
    return (a[0],a[1])

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
    t = set()
    for x,y in vsa_polja(s,v):
        if sosedov(x,y,mine) == 0:
            t.add((x,y))
    return t


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
    slovar = {}
    for i in range(0, 9):
        slovar[i] = set()
        for x,y in vsa_polja(s,v):
            if i == sosedov(x,y,mine):
                slovar[i].update({(x,y)})
    return slovar

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
    razdalja = 0
    for (x,y),(x1,y1) in zip(pot, pot[1:]): #zipa po dva para skupaj (p1,p2), (p2,p3) ....
        razdalja += math.hypot(x1-x,y1-y)
    return razdalja

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
    polja = [(x0,y0),(x1,y1)] #seznam polj od (x0,y0) do (x1,y1)

    if x0 < x1 or y0 < y1:  #v primeru, da je prva točka MANJŠA od druge
        os_x = range(x0 + 1, x1) or [x0]
        os_y = range(y0 + 1, y1) or [y0]
        for x in os_x:
            for y in os_y:
                polja.append((x,y))

    elif x1 < x0 or y1 < y0:#v primeru, da je prva točka VEČJA od druge
        os_x1 = range(x1, x0+1) or [x1]
        os_y1 = range(y1, y0+1) or [y1]
        for x3 in os_x1:
            for y3 in os_y1:
                polja.append((x3, y3))

    if not list(set(polja).intersection(mine)): #če ni noben element v preseku vrni True
        return True


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    t = []
    for p in pot:   #v primeru, da je začetna točka mina(zadnji test)
        if p in mine:
            return False

    for (x, y), (x1, y1) in zip(pot, pot[1:]):  #združi po dve točki
        if varen_premik(x, y, x1, y1, mine) == True: #pogleda ali je premik varen
            t.append(True)  #če je v "t" zapiše True
        else:
            t.append(False) #če ni v "t" zapiše False

    return all(vrednost == True for vrednost in t)  #če so vse vrednosti v "t" True, vrne True


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
    t = polje.split(" ")
    mine = []
    for y,element in enumerate(t):
        for x, znak in enumerate(list(element)):
            if znak == 'X':
                mine.append((x,y))
    return set(mine),len(element),len(t)
            #for element in t:
            #s = len(element)
            #v = len(t)"""


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


