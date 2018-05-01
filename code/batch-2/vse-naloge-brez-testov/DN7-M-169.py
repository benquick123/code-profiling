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
    i = 0
    for x1,y1 in mine:
        if x1 == x and y1 == y:
            continue
        if abs(x1 - x) <= 1 and abs(y1 - y) <= 1:
            i += 1
    return i

def sosedov(x, y, mine):
    return sum(1 for x1,y1 in mine  if not(x1 == x and y1 == y) and (abs(x1 - x) <= 1 and abs(y1 - y) <= 1))


def najvec_sosedov(mine, s, v):
    naj = 0
    n = (0, 0)
    for x1, y1 in vsa_polja(s, v):
        if sosedov(x1, y1, mine) > naj:
            naj = sosedov(x1, y1, mine)
            n = (x1, y1)
    return n

def najvec_sosedov(mine, s, v):
    return tuple((x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == (max(sosedov(x1, y1, mine) for x1, y1 in vsa_polja(s, v))))[0]

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
    polja = vsa_polja(s, v)
    i = 0
    xs = set()
    for x1, y1 in polja:
        if sosedov(x1, y1, mine) == 0:
            xs.add((x1, y1))
    return xs

def brez_sosedov(mine, s, v):
    return set((x1, y1) for x1, y1 in vsa_polja(s, v) if sosedov(x1, y1, mine) == 0)
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
    xs = {}
    polja = vsa_polja(s, v)
    for x1, y1 in polja:
        for i in range(9):
            if i not in xs:
                xs[i] = set()
            if sosedov(x1, y1, mine) == i:
                xs[i].add((x1, y1))

def po_sosedih(mine, s, v):
    return {i: (set((x1, y1)
            for x1, y1 in vsa_polja(s, v)
                if sosedov(x1, y1, mine) == i))for i in range(0,9)}


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
    v = 0
    if pot == []:
        return v
    x1 = pot[0][0]
    y1 = pot[0][1]
    for x, y in pot:
        v += (abs(x - x1) + abs(y - y1))
        x1 = x
        y1 = y
    return v

def dolzina_poti(pot):
    return sum((abs(x - x1) + abs(y - y1)) for (x, y), (x1, y1) in zip(pot[:], pot[1:]))

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
    m = set(((x0,y0), (x1, y1)))
    for i in range(abs(y1 - y0)):
        if (y1 - y0 > 0):
            y0 += 1
            m.add((x0, y0))
        else:
            y0 -= 1
            m.add((x0, y0))
    for i in range(abs(x1 - x0)):
        if (x1 - x0 > 0):
            x0 += 1
            m.add((x0, y0))
        else:
            x0 -= 1
            m.add((x0, y0))
    return m & mine == set()
def varen_premik(x0, y0, x1, y1, mine):
    return (set((x0 + i, y0) if x0 < x1 else (x0 - i, y0) for i in range(abs(x1 - x0)))
            | set((x0, y0 + 1) if y0 < y1 else (x0, y0 - i)
            for i in range(abs(y1 - y0))) | {(x1, y1),(x0,y0)}) & mine == set()



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
    seznam = []
    if len(pot) == 1:
        for x, y in pot:
            if (x, y) in mine:
                return False
        return True
    for (x0,y0), (x1, y1) in zip(pot[:], pot[1:]):
        seznam.append(varen_premik(x0, y0, x1, y1, mine))
    return all(seznam)



def varna_pot(pot, mine):
    return all([varen_premik(x0, y0, x1, y1, mine)
                for (x0,y0), (x1, y1) in zip(pot[:], pot[1:]) if
                len(pot) > 1]) and all((x, y) not in mine for x, y in pot if len(pot) == 1)
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
    i = 0
    st = 1
    s = set()
    y = 0
    for e in polje:
        if e != " " and e != "X":
            i += 1
        elif e == "X":
            i += 1
            s.add((i-1, y))
        elif e == " ":
            i = 0
            y += 1
    if " " in polje:
        p = polje.index(" ")
        st = len(polje[:p])
    else:
        st = len(polje)
    if polje[-1] == " ":
        y -= 1
    return (s, st, y+1)
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
def preberi_pot(ukazi):
    x = 0
    y = 0
    ukazi = ukazi.split()
    s = [(0, 0)]
    puscica = 90
    for ukaz in ukazi:
        if puscica == 360 or puscica == -360:
            puscica = 0
        if ukaz == "DESNO":
            puscica -= 90
            continue
        if ukaz == "LEVO":
            puscica += 90
            continue
        else:
            if puscica == 0:
                x += int(ukaz)
                s.append((x, y))
            if puscica == -90 or puscica == 270:
                y += int(ukaz)
                s.append((x, y))
            if puscica == -180 or puscica == 180:
                x -= int(ukaz)
                s.append((x, y))
            if puscica == 90 or puscica == -270:
                y -= int(ukaz)
                s.append((x, y))
    return s


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
def zapisi_pot(ukazi):
    niz = """"""
    s = []
    for (x0, y0), (x1, y1) in zip(ukazi, ukazi[1:]):
        rx = x1 - x0
        ry = y1 - y0
        de = "DESNO"
        n = niz.splitext(int)
        if ry > 0:
            niz += 2 * de
            niz += str(ry)
            niz += 2 * de
        if ry < 0:
            niz += 4 * de
            niz += str(abs(rx))
        if rx > 0:
            niz += de
            niz += str(rx)
            niz += 3 * de
        if rx < 0:
            niz += 3 * de
            niz += str(abs(rx))
            niz += de
    return niz

