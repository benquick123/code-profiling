# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
import math
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
    # calls = 0
    # for x0,y0 in mine:
    #     if (abs(x-x0) == 1 and abs(y-y0) == 1)\
    #             or abs(x-x0) == 0 and abs(y-y0) == 1\
    #             or abs(x-x0) == 1 and abs(y-y0) == 0:
    #         calls += 1
    # return calls
    return sum([1 for x0,y0 in mine if (abs(x-x0) == 1 and abs(y-y0) == 1) or
                abs(x-x0) == 0 and abs(y-y0) == 1 or
                abs(x-x0) == 1 and abs(y-y0) == 0])


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
    # a = [(x,y) for (x,y) in vsa_polja(s,v)]
    # seznam = []
    # for x,y in a:
    #     seznam.append([sosedov(x,y,mine), (x,y)])
    # return max(seznam)[1]
    return max([(sosedov(x,y, mine),(x,y)) for x,y in [(i,k) for (i,k) in vsa_polja(s,v)]])[1]


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
    # mnozica = set()
    # a = [(x,y) for (x,y) in vsa_polja(s,v)]
    # b = [sosedov(x,y,mine) for x,y in a]
    # for (x,y), i in zip(a,b):
    #     if not sosedov(x,y,mine):
    #         mnozica.add((x,y))
    # return mnozica
    return {(x,y) for (x,y), i in zip([(h,j) for (h,j) in vsa_polja(s,v)],[sosedov(k,l,mine) for k,l, in [(b,n) for (b,n) in vsa_polja(s,v)]]) if not sosedov(x,y,mine)}


def po_sosedih(mine, s, v):
    """
    Vrni slovar, katerega ključi so možna števila sosednjih polj z minami
    (torej števila od 0 do 8), vrednosti pa množice koordinat polj s toliko
    sosedami.
n
    Args:
        mine (set of tuple of int): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        dict: (glej zgoraj)
    """
    # sez = vsa_polja(s,v)
    # dict_brt = {x: set() for x in range(9)}
    # for x,y in sez:
    #     dict_brt[sosedov(x,y, mine)].add((x,y))
    # return dict_brt
    return {i: {(x,y) for (x,y) in vsa_polja(s,v) if sosedov(x,y, mine) == i} for i in range(9)}

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
    # if pot:
    #     vredx = pot[0][0]
    #     vredy = pot[0][1]
    # else:
    #     return 0
    # dolzina = 0
    # for x,y in pot:
    #     dolzina += abs(vredx-x) + abs(vredy-y)
    #     vredx = x
    #     vredy = y
    # return dolzina
    return sum([(abs(x0-x1) + abs(y0-y1)) for (x0,y0),(x1,y1) in zip(pot, pot[1:])])



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
    # """
    # if x0 == x1:
    #     for y in range(min(y0, y1), max(y0, y1)+1):
    #         if (x0, y) in mine:
    #             return False
    # if y0 == y1:
    #     for x in range(min(x0, x1), max(x0, x1)+1):
    #         if (x, y0) in mine:
    #             return False
    # if x0 == x1 == y0 == y1:
    #     if (x0, y0) in mine:
    #         return False
    # return True
    return all([((x0, y) not in mine) for y in range(min(y0, y1), max(y0,y1)+1)])\
        if (x0 == x1) \
        else all([((x, y0) not in mine) for x in range(min(x0,x1), max(x0,x1)+1)])


def varna_pot(pot, mine):
    """q
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    # return varen_premik(pot[0][0], pot[0][1], pot[-1][-2], pot[-1][-1], mine) if pot else True
    return all([varen_premik(x1,y1,x2,y2,mine) for (x1,y1), (x2,y2) in zip(pot, pot[1:])]) \
        if len(pot) != 1 else varen_premik(pot[0][0], pot[0][1], pot[0][0], pot[0][1], mine) if len(pot) == 1 else True
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
    mnozica = set()
    polje1 = polje.split(" ")
    s = v = 0
    ynum = -1
    a = 0
    for subsection in polje1:
        if subsection:
            a += 1
            xnum = -1
            ynum += 1
            if a == 1:
                s = len(subsection)
            v += 1
            for string in subsection:
                xnum += 1
                if string == "X":
                    mnozica.add((xnum, ynum))
    return mnozica, s, v
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
    if ukazi:
        x = y = 0
        pot = [(0,0)]
        smeri = ["GOR", "DESNO", "DOL", "LEVO"]
        ukazi = ukazi.split("\n")
        trenutna_smer = smeri[0]
        for ukaz in ukazi:
            if ukaz == "DESNO":
                smeri.append(smeri.pop(0))
                trenutna_smer = smeri[0]
            elif ukaz == "LEVO":
                smeri.insert(0, smeri.pop())
                trenutna_smer = smeri[0]        # Osramotil sem svojo familijo, ker ta koda ni lepša in vem, da bi lahko bila.
            else:
                ukaz = int(ukaz)
                if trenutna_smer == "GOR":
                    y -= ukaz
                    pot.append((x,y))
                elif trenutna_smer == "DESNO":
                    x += ukaz
                    pot.append((x,y))
                elif trenutna_smer == "DOL":
                    y += ukaz
                    pot.append((x,y))
                elif trenutna_smer == "LEVO":
                    x -= ukaz
                    pot.append((x,y))
        return pot





def zapisi_pot(pot):
    from itertools import cycle
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    trenutna_smer = "GOR"
    smeri = ["GOR", "DESNO", "DOL", "LEVO"]
    print(pot)
    ukazi = []
    nov_sez = []
    string = ""
    for (x1,y1), (x2,y2) in zip(pot, pot[1:]):
        razlikax = razlikay = 0
        if y1 == y2:
            razlikax = x1-x2
            if razlikax < 0:
                while trenutna_smer != "DESNO":
                    smeri.append(smeri.pop(0))
                    trenutna_smer = smeri[0]
                    ukazi.append(trenutna_smer)
                ukazi.append(abs(x2-x1))
            elif razlikax > 0:
                while trenutna_smer != "LEVO":
                    smeri.insert(0, smeri.pop())
                    trenutna_smer = smeri[0]
                    ukazi.append(trenutna_smer)
                ukazi.append(abs(x2-x1))
        elif x1 == x2:
            razlikax = y1-y2
            if razlikax < 0:
                while trenutna_smer != "GOR":
                    smeri.append(smeri.pop(0))
                    trenutna_smer = smeri[0]
                    ukazi.append(trenutna_smer)
                ukazi.append(abs(x2-x1))
            elif razlikax > 0:
                while trenutna_smer != "DOL":
                    smeri.insert(0, smeri.pop())
                    trenutna_smer = smeri[0]
                    ukazi.append(trenutna_smer)
                ukazi.append(abs(x2-x1))
    for (beseda) in ukazi:
        string += (str(beseda) + "\n")
    print(string)
    return string








