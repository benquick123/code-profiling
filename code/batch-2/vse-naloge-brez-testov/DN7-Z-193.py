# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    sosednje = {(x-1,y-1), (x, y-1), (x+1,y-1),
                (x-1,y), (x+1,y),
                (x-1,y+1), (x,y+1), (x+1,y+1)}
    polne = set()
    for m in mine:
        for e in sosednje:
            if e == m:
                polne.add(e)
    return len(list(polne))


def najvec_sosedov(mine, s, v):
    naj = 0
    p = 0,0
    for e in vsa_polja(s, v):
        x,y = e
        if sosedov(x,y,mine) > naj:
            naj = sosedov(x,y,mine)
            p = (x,y)
    return p

def brez_sosedov(mine,s,v):
    k = set()
    for e in vsa_polja(s,v):
        x,y = e
        if sosedov(x,y,mine) == 0:
            k.add(e)
    return k


def po_sosedih(mine, s, v):
    b = {}
    for c in range(0,9):
        b[c] = set()
    for koordinate in vsa_polja(s,v):
        x, y = koordinate
        c = sosedov(x,y,mine)
        b[c].add(koordinate)
    return b

########################
# Za oceno 7

def dolzina_poti(pot):
    razdalja = 0
    iksi = []
    ipsi = []
    for x, y in pot:
        iksi.append(x)
        ipsi.append(y)
        zx = zip(iksi, iksi[1:])
        zy = zip(ipsi, ipsi[1:])
        rvx = (sum(abs(x - i) for x, i in zx))
        rvy = (sum(abs(y - j) for y, j in zy))
        razdalja = rvx + rvy
    return razdalja


def varen_premik(x0, y0, x1, y1, mine):
    mn = set()
    for x in range(min(x0,x1), max(x0,x1)+1):
        for y in range(min(y0,y1), max(y0,y1)+1):
            mn.add((x,y))
    for n in mn:
        if n in mine:
            return False
    else:
        return True


def varna_pot(pot, mine):
    if len(pot) < 1:
        return True
    if len(pot) == 1:
        return not pot[0] in mine
    for e in range(0, len(pot)-1):
        x0, y0 = pot[e]
        x1, y1 = pot[e+1]
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


