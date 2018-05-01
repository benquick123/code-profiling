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
import math

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
    """
    stevec = 0
    for k1, k2 in mine:
        if math.sqrt((x-k1)**2+(y-k2)**2) < 1.5 and math.sqrt((x-k1)**2+(y-k2)**2) > 0:
            stevec += 1
    return stevec
    """
    return len([(k1, k2) for k1, k2 in mine if math.sqrt((x-k1)**2 + (y-k2)**2) <= math.sqrt(2) and math.sqrt((x-k1)**2 + (y - k2)**2) > 0])

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
    '''
    trenutni_stevec = 0
    koordinate = (0, 0)
    for x in range(s):
        for y in range(v):
            stevec = sosedov(x, y, mine)
            if stevec > trenutni_stevec:
                trenutni_stevec = stevec
                koordinate = (x, y)
    return koordinate
    '''

    return tuple((x, y) for x in range(s) for y in range(v) if sosedov(x, y, mine) == max([sosedov(x1, y1, mine) for x1 in range(s) for y1 in range(v)]))[0]



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
    """
    m = set()
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) == 0:
                m.add((x, y))
    return m
    """
    return set((x, y) for x in range(s) for y in range(v) if sosedov(x, y, mine) == 0)

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
    """
    slovar = {}
    for x, y in vsa_polja(s, v):
        for i in range(9):
            if i not in slovar:
                slovar[i] = set()
        slovar[sosedov(x, y, mine)].add((x, y))
    return slovar
    """
    return {i: {(x, y) for x, y in vsa_polja(s, v) if i == sosedov(x, y, mine)} or set() for i in range(9)}


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
    """
    vsota = 0
    for i in range(1, len(pot)):
        vsota += abs((pot[i][0]-pot[i-1][0])+(pot[i][1]-pot[i-1][1]))
    return vsota
    """
    return sum([abs((pot[i][0]-pot[i-1][0])+(pot[i][1]-pot[i-1][1])) for i in range(1, len(pot))])





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
    if (x0, y0) in mine or (x1, y1) in mine:
        return False
    elif x0 == x1 and y0 != y1:
        koraky = 1
        if y1 < y0:
            koraky = -1
        for i in range(y0, y1, koraky):
            if (x0, i) in mine:
                return False
        else:
            return True
    elif y0 == y1 and x0 != x1:
        korakx = 1
        if x1 < x0:
            korakx = -1
        for j in range(x0, x1, korakx):
            if (j, y0) in mine:
                return False
        else:
            return True
    else:
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
    '''
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if not varen_premik(x0, y0, x1, y1, mine):
            return False
    else:
        if len(pot) == 0:
            return True
        elif (pot[0][0], pot[0][1]) in mine:
            return False
        else:
            return True
    '''
    return (len(pot) == 0 or not (pot[0][0], pot[0][1]) in mine and all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])]))

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
    polje = polje.split()
    m = set()
    s = len(polje[0])
    v = len(polje)
    for vrstica in range(len(polje)):
        for i in range(len(polje[vrstica])):
            if polje[vrstica][i] == 'X':
                m.add((i, vrstica))
    return (m, s, v)



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


