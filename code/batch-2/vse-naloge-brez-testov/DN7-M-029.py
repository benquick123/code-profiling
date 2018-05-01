# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
import collections
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

def sosedov(x, y, mine):
    k = 0
    for x1, y1, in mine:
        if abs(x - x1) <= 1 and abs(y - y1) <= 1 and (x, y) != (x1, y1):
            k += 1
    return k


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

def najvec_sosedov(mine, s, v):
    sl = collections.defaultdict(list)
    for x, y in vsa_polja(s, v):
            sl[sosedov(x, y, mine)].append((x, y))
    return sl[max(sl)][0]



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

def brez_sosedov(mine, s, v):
    sl = collections.defaultdict(set)
    for x, y in vsa_polja(s, v):
            sl[sosedov(x, y, mine)].add((x, y))
    return sl[0]


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

def po_sosedih(mine, s, v):
    sl = {}
    for i in range(9):
        sl[i] = set()
    for x, y in vsa_polja(s, v):
        sl[sosedov(x, y, mine)].add((x, y))
    return sl

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


def dolzina_poti(pot):
    k = 0
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if x0 != x1:
            k += abs(x1 - x0)
        if y0 != y1:
            k += abs(y1 - y0)
    return k


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

def varen_premik(x0, y0, x1, y1, mine):
    if (x0, y0) in mine or (x1, y1) in mine:
        return False
    if x0 != x1:
        if x1 < x0:
            while x1 != x0:
                x0 -= 1
                if(x0, y0) in mine:
                    return False
        else:
            while x1 != x0:
                x0 += 1
                if(x0, y0) in mine:
                    return False
    else:
        if y1 < y0:
            while y1 != y0:
                y0 -= 1
                if(x0, y0) in mine:
                    return False
        else:
            while y1 != y0:
                y0 += 1
                if(x0, y0) in mine:
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

def varna_pot(pot, mine):

    if len(pot) == 1 and pot[0] in mine:
        return False
    for pot1, pot2 in zip(pot, pot[1:]):
        if not varen_premik(pot1[0], pot1[1], pot2[0], pot2[1], mine):
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
def polje_v_mine(polje):
    kor = set()
    v = -1
    for pole in polje.split():
        v += 1
        for s in range(len(pole)):
            if pole[s] == "X":
                kor.add((s, v))
    return kor, s + 1, v + 1


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.
def sosedov(x, y, mine):
    return sum([1 for x1, y1 in mine if abs(x - x1) <= 1 and abs(y - y1) <= 1 and (x, y) != (x1, y1)])

def dolzina_poti(pot):
    return sum([abs(x1 - x0) + abs(y1 - y0) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])

def brez_sosedov(mine, s, v):
    return {a for a, b in {(x, y):sosedov(x, y, mine) for x, y in vsa_polja(s, v)}.items() if b == 0}

def varna_pot(pot, mine):
    return all([not (len(pot) == 1 and pot[0] in mine1)] +
               [varen_premik(pot1[0], pot1[1], pot2[0], pot2[1], mine1)
                for pot1, pot2 in zip(pot, pot[1:])])

def varen_premik(x0, y0, x1, y1, mine):
    return all([not((x0, y0) in mine or (x1, y1) in mine)] + \
           [not((x, y0) in mine) for x in range(x0, x1) if x0 < x1] + \
           [not((x, y0) in mine) for x in range(x0, x1, -1) if x0 > x1] +  \
            [not ((x0, y) in mine) for y in range(y0, y1) if y0 < y1] +  \
            [not((x0, y) in mine) for y in range(y0, y1, -1) if y0 > y1])

def najvec_sosedov(mine, s, v):
    return max({sosedov(x, y, mine):(x, y) for x, y in vsa_polja(s, v)}.items())[1]


def po_sosedih(mine, s, v):
    return {a:{(x, y)for x, y in vsa_polja(s, v) if a == sosedov(x, y, mine)} for a, b in {i:{1, 2, 3} for i in range(9)}.items()}

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
def preberi_pot(ukazi):
    x = y = nasoka = 0
    pot = [(x, y)]
    for ukaz in ukazi.split():
        if ukaz.isalpha():
            if ukaz == "DESNO":
                nasoka += 1
            else:
                nasoka -= 1
            if nasoka < -3 or nasoka > 3:
                nasoka = 0
        else:
            if nasoka == 1 or nasoka == -3: #360
                x += int(ukaz)
            elif nasoka == 2 or nasoka == -2: #270
                y += int(ukaz)
            elif nasoka == 3 or nasoka == -1: #180
                x -= int(ukaz)
            else:
                y -= int(ukaz)
            pot.append((x, y))
    return pot


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
def zapisi_pot(pot):
    potmoj = []
    ukazi = ""
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if (x0, y0) not in potmoj:
            potmoj.append((x0, y0))
        if (x1, y1) not in potmoj:
            potmoj.append((x1, y1))
        k = abs(x1 - x0) + abs(y1 - y0)
        while preberi_pot(ukazi + str(k)) != potmoj:
            ukazi += " LEVO "
        ukazi += str(k)
    return ukazi


