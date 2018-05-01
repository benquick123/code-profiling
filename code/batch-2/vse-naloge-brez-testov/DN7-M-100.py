import math
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
    return len([(x1, y1) for x1, y1 in mine if (x == x1 +1 and y == y1)or(x == x1 - 1 and y == y1)or(x == x1 and y == y1 + 1)or(x == x1 and y == y1 -1)or(x == x1 - 1 and y == y1 +1)or(x == x1 - 1 and y == y1 - 1)or(x == x1 + 1 and y == y1 - 1)or(x == x1 + 1 and y == y1 + 1 )])


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
    slovar = collections.defaultdict(list)

    for x, y in vsa_polja(s, v):
        slovar[sosedov(x, y, mine)].extend([(x, y)])

    for x, y in slovar[max(slovar)]:
        odgovor = (x, y)

    return odgovor




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
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}


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

    slovar  = collections.defaultdict(set)

    for x, y in vsa_polja(s, v):
        slovar[sosedov(x, y, mine)].update({(x, y)})

    for x in range(9):
        if x not in slovar:
            slovar[x] = set()

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
    if len(pot) > 2:
        odgovor = 0
        neki = zip(pot, pot[1::])
        for a, b in neki:
            x1, y1 = a
            x2, y2 = b
            odgovor += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    else:
        odgovor = 0
        neki = zip(pot, pot[1::])
        for a, b in neki:
            x1, y1 = a
            x2, y2 = b
            odgovor += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    return odgovor


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
    pot = []
    if x0 == x1 and y0 < y1:
        for y in range(y0, y1+1):
            pot.append((x0, y))

    elif x0 == x1 and y0 > y1:
        for y in range(y1, y0+1):
            pot.append((x0, y))

    elif y0 == y1 and x0 < x1:
        for x in range(x0, x1+1):
            pot.append((x, y0))

    elif y0 == y1 and x0 > x1:
        for x in range(x1, x0+1):
            pot.append((x, y0))

    elif y0 == y1 and x0 == x1:
        if (x0, y0) in mine:
            return False
        else:
            return True

    for x, y in pot:
        if(x, y) in mine:
            return False

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
    if len(pot) > 1:
        premiki = zip(pot, pot[1::])
        odgovor = True
        for a, b in premiki:
            x0, y0 = a
            x1, y1 = b
            if varen_premik(x0, y0, x1, y1, mine) == True:
                odgovor = True
            else:
                return False
    elif len(pot) == 1:
        for a in pot:
            x1, y1 = a
            if (x1, y1) in mine:
                return False
            else:
                return True
    elif len(pot) == 0:
        return True
    return odgovor


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
    dolzina = 0
    for t in polje:
        if t == "." or t == "X":
            dolzina = dolzina + 1
        elif t == " ":
            break

    visina = polje.count(" ") + 1

    x = 0
    y = 0
    mine = set()
    tabelca = []
    for g in polje:
        if g == ".":
            x = x + 1
        elif g == " ":
            y = y + 1
            x = 0
        elif g == "X":
            mina = (x, y)
            tabelca.append(mina)
            x = x + 1

    for element in tabelca:
        mine.update({element})

    return((mine, dolzina, visina))


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


