# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.

from math import sqrt
from enum import Enum

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


    st_sosedov = 0
    for tx,ty in mine:
        if tx != x or ty != y:
            rx = abs(tx - x)
            ry = abs(ty - y)
            if (rx == 1 or rx == 0) and (ry == 1 or ry == 0):
                st_sosedov += 1
    return st_sosedov
    """


def sosedov(x, y, mine):
    return len( [(x1,y1) for (x1,y1) in mine if sqrt((x1-x)**2 + (y1-y)**2) < 2 and (x1 is not x or y1 is not y)] )

def najvec_sosedov(mine, s, v):
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja
    maxi = (0, 0)
        for y in range(v):
            for x in range(s):
                if sosedov(x, y, mine) > sosedov(maxi[0], maxi[1], mine):
                    maxi = (x, y)
    """

    return list(vsa_polja(s,v))[[sosedov(x, y, mine) for x, y in vsa_polja(s,v)].index(max((sosedov(x, y, mine) for x, y in vsa_polja(s,v))))]



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
     polja = set()
    for y in range(v):
        for x in range(s):
            if sosedov(x, y, mine) == 0:
                polja.add((x, y))
    return polja

    """
    return {(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine) is 0}



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
    #mozna_st = dict().fromkeys(range(9), set())
    mozna_st = dict()
    for i in range(9):
        mozna_st[i] = set()
    for y in range(v):
        for x in range(s):
            mozna_st[sosedov(x, y, mine)].add((x,y))
    return mozna_st
    """


    return {k: {(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine) == k } for k in range(9)}





########################
# Za oceno 7

def dolzina_poti(pot):
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    dolzina = 0
    first_loop = True
    for x,y in pot:
        if not first_loop:
            dolzina += abs(x-prevx) + abs(y-prevy)
        first_loop = False
        prevx = x
        prevy = y

    return dolzina
    """
    return len(range(int(sum ([sqrt((x1-x2)**2 + (y1-y2)**2) for (x1,y1),(x2,y2) in zip(pot,pot[1:])]))))

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

    if x0 == x1:
        if y0 > y1:
            y0, y1 = y1, y0

        for i in range(y0,y1+1):
            if (x0,i) in mine:
                return False
    if y1 == y0:
        if x0 > x1:
            x0, x1 = x1, x0
        for i in range(x0, x1+1):
            if (i, y0) in mine:
                return False
    return True
    """
    return False if len({ (x,y) for x,y in zip( list(range(x0,x1,-1 if x0> x1 else 1)), [y0]* len(range(x0,x1, -1 if x0 > x1 else 1)) )  }.intersection(mine)) >0 or len({(x,y) for x,y in zip([x0] * len(range(y0,y1,-1 if y0 > y1 else 1 )), list(range(y0,y1,-1 if y0 > y1 else 1)))}.intersection(mine)) > 0 or (x1,y1) in mine or (x0,y0) in mine else True



def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    if len(pot) == 1:
        if pot[0] in mine:
            return False
    else:
        first_loop = True
        for x,y in pot:
            if not first_loop:
                if not varen_premik(prevx, prevy, x, y, mine):
                    return False
            first_loop = False
            prevx = x
            prevy = y
    return True
    """
    return True if len({varen_premik(x0,y0,x1,y1,mine) for (x0,y0), (x1,y1) in zip(pot,pot[1:])}.intersection({False})) is 0 and len(set(pot).intersection(mine)) is 0 else False



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
    x = 0
    y = 0
    s = polje.split()
    for vrstica in s:
        for p in vrstica:
            if p == 'X':
                mine.add((x, y))
            x += 1
        y += 1
        x = 0
    x = len(vrstica)
    y = len(polje.split())
    return mine,x,y



########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    orientation = 1 # kam je obrnjen ( 1 - gor, 2 - desno, 3 - dol, 4 - levo)
    x = 0
    y = 0
    pot = []
    pot.append((x,y))
    ukazi = ukazi.split()
    for ukaz in ukazi:
        if ukaz == 'LEVO' or ukaz == 'DESNO':
            if ukaz == 'LEVO':
                if orientation == 4:
                    orientation = 1
                else:
                    orientation += 1
            else:
                if orientation == 0:
                    orientation = 3
                else:
                    orientation -= 1
        else:
            if orientation == 1:
                y -= int(ukaz)
            elif orientation == 2:
                x -= int(ukaz)
            elif orientation == 3:
                y += int(ukaz)
            else:
                x += int(ukaz)
            pot.append((x,y))
    return pot
    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """




def zapisi_pot(pot):
    orientation = 1 #isto kot pri zgornji nalogi
    ukazi = []
    prevX, prevY = pot[0]
    for x,y in pot[1:]:
        tmpX = prevX - x
        tmpY = prevY - y
        if tmpY < 0:
            des_ori = 3
        elif tmpY > 0:
            des_ori = 1
        if tmpX < 0:
            des_ori = 4
        elif tmpX > 0:
            des_ori = 2
        while orientation != des_ori:
            if orientation == 4:
                orientation = 1
            else:
                orientation +=1
            ukazi.append("LEVO")

        if tmpX == 0:
           ukazi.append(str(abs(tmpY)))
        else:
            ukazi.append(str(abs(tmpX)))
        prevX = x
        prevY = y
    ukazi= "\n".join(ukazi)
    print(ukazi)
    return ukazi


    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """


