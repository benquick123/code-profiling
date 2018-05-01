# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
from math import sqrt
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

def mine_stevilke(mine):
    mines = {}
    polja= vsa_polja(s,v)
    for polje in polja:
        if pilje in mine:
            mines[polje] = 1
        else:
            mines[polje] = 0
    return mines

def sospolja(s,v):
    return ((x,y) for x,y in vsa_polja(100, 100) if sqrt((s - x)**2 + (v - y)**2) <= sqrt(2))

def sospoljx(s,v):
    return ((x,y) for x,y in vsa_polja(s, v) if sqrt((s - x)**2 + (v - y)**2) <= sqrt(2))

########################
# Za oceno 6

def sosedov(x, y, mine):
    #print(sospolja(x,y))
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
    po=0
    for polja in sospolja(x,y):
        if polja in mine:
            if not polja == (x,y):
                po +=1
    return po
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
    max = 0
    neki = (0,0)
    for pol in vsa_polja(s,v):
        x, y = pol
        temp = sosedov(x,y, mine)
        if  temp > max:
            max = temp
            #print(temp)
            #print(pol)
            neki = pol
    return neki


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
    return {(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y, mine) ==0}

from collections import defaultdict
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
    slo ={0: set(),1: set(),2: set(),3: set(),4: set(),5: set(),6: set(),7: set(),8: set() }
    for x,y in vsa_polja(s,v):
        slo[sosedov(x,y,mine)].add((x,y))
    return slo
#def po_sosedih(mine, s, v):
 #   return {[sosedov(x,y,mine)].add((x,y)) for x,y in vsa_polja(s,v)}
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
    #vsi koraki
    razdalje = 0
    pari = zip(pot, pot[1:])
    for (a, b), (c, d) in pari:
        if a == c:
            razdalje += abs(b - d)
        else:
            razdalje += abs(c - a)
    return razdalje

#def dolzina_poti(pot):
 #   return razdalje += abs(b - d) for (a, b), (c, d) in pari if if a == c else razdalje += abs(c - a)

def vsikoraki(pot):
    razdalje =0
    pari = zip(pot, pot[1:])
    for (a,b), (c,d) in pari:
        if a ==c:
            razdalje += abs(d-a)
        else:
            razdalje += (c-d)
    return razdalje


def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1:
        for y in range(min([y0,y1]),(max([y0,y1]))+1):
            if (x1, y) in mine:
                return False
    if y0==y1:
        for x in range(min([x0,x1]),(max([x0,x1]))+1):
            if (x, y0) in mine:
                return False
    return True
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
    if dolzina_poti(pot) > 1:
        pari = zip(pot, pot[1:])
        for (x0,y0) ,(x1,y1) in pari:
            if not varen_premik(x0, y0, x1, y1, mine):
                return False
    else:
        for xxxx in pot:
            if xxxx in mine:
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

    mine={}
    slovar={}
    for st in range(0,len(polje)):
         slovar[st] = polje.split(" ")[st]
    for x in range(len(slovar)):
        for y in slovar[a].split():
            if y =='X':
                mine.add(x,y)
    return mine
    """
    mine =[]
    vrstica = 0
    pol = 0
    maxpol=0
    for beseda in polje.split(" "):

        for crka in beseda:
            if crka == "X":
                mine.append((pol, vrstica))
            pol +=1
        vrstica +=1
        if pol > maxpol:
            maxpol = pol
        pol = 0




    minek = set(mine)
    mine = (minek, maxpol, vrstica)
    return mine



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


