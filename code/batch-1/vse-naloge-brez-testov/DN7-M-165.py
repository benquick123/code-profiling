from math import *
import collections
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
    count = 0
    for i in mine:
        x1, y1 = i
        if x - 1 == x1 and y - 1 == y1:
            count += 1
        if x - 1 == x1 and y == y1:
            count += 1
        if x - 1 == x1 and y + 1 == y1:
            count += 1
        if x == x1 and y - 1 == y1:
            count += 1
        if x == x1 and y + 1 == y1:
            count += 1
        if x + 1 == x1 and y + 1 == y1:
            count += 1
        if x + 1 == x1 and y == y1:
            count += 1
        if x + 1 == x1 and y - 1 == y1:
            count += 1
    return count

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
    #dont ask what I am doing
    a =[]
    x1, y1 = 0,0
    b = 0
    for x in range(s):
        for y in range(v):
            a.append((x,y))
   # print (a)

    for i in mine:
        if i in a:
            a.remove(i)
    print (a)

    for d,f in a:
        najvec = sosedov(d,f,mine)
        if b < najvec:
            #print (d,f)
            b = najvec
            x1 = d
            y1 = f

    return (x1,y1)

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
    a = []
    j = set()
    b = 0
    for x in range(s):
        for y in range(v):
            a.append((x,y))

    for d,f in a:
        najvec = sosedov(d,f,mine)
        if b == najvec:
            #print (d,f)
            j.add((d,f))

    return j

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
    b = {}
    a = []

    c = set()
    t = set()
    j = set()
    k = set()
    u = set()
    m = set()
    n = set()
    o = set()
    p = set ()

    for x in range(s):
        for y in range(v):
            a.append((x, y))

    for i in range(9):
        b[i] = []

    for d, f in a:
        najvec = sosedov(d, f, mine)
       # kordinate.append((d,f))
       # stevilka.append(najvec)

       # b[najvec].update((d,f))
        #b[najvec].update((d,f))
        #z[has].append(a)
        if 0 == najvec:
            c.add((d, f))

        if 1 == najvec:
            t.add((d, f))
        if 2 == najvec:
            j.add((d, f))

        if 3 == najvec:
            k.add((d, f))
        if 4 == najvec:
            u.add((d, f))
        if 5 == najvec:
            m.add((d, f))
        if 6 == najvec:
            n.add((d, f))
        if 7 == najvec:
            o.add((d, f))
        if 8 == najvec:
            p.add((d, f))

    b[0] = c
    b[1] = t
    b[2] = j
    b[3] = k
    b[4] = u
    b[5] = m
    b[6] = n
    b[7] = o
    b[8] = p










        #b[najvec].extend((d,f))


    #b[najvec] = sorted(b[najvec])           # print (d,f)

    return b








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

3
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


def varna_pot(pot, mine):
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


