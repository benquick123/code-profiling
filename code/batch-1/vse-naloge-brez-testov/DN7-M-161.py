def vsa_polja(s, v):
    return ((x, y) for x in range ( s ) for y in range ( v ))
########################
# Za oceno 6
def sosedov(x, y, mine):
    a = set ()
    b = set ()
    for e in mine:
        if e[0] == x or e[0] == x + 1 or e[0] == x - 1:
            a.add ( e )
        if e[1] == y or e[1] == y + 1 or e[1] == y - 1:
            b.add ( e )
        if e[0] == x and e[1] == y:
            a.remove ( e )
    return (len ( a.intersection ( b ) ))

from collections import Counter

def najvec_sosedov(mine, s, v):
    a = []
    if len ( mine ) == 0:
        return (0, 0)
    if len ( mine ) == 1:
        for e in mine:
            return (e)
    else:
        for e in mine:
            x, y = e
            levo = (x - 1, y)
            if x - 1 in range ( s ):
                a.append ( levo )
            desno = (x + 1, y)
            if x + 1 in range ( s ):
                a.append ( desno )
            gor = (x, y - 1)
            if y - 1 in range ( v ):
                a.append ( gor )
            dol = (x, y + 1)
            if y + 1 in range ( v ):
                a.append ( dol )
            levagor_d = (x - 1, y - 1)
            if x - 1 in range ( s ) and y - 1 in range ( v ):
                a.append ( levagor_d )
            desnagor_d = (x + 1, y - 1)
            if x + 1 in range ( s ) and y - 1 in range ( v ):
                a.append ( desnagor_d )
            levadol_d = (x - 1, y + 1)
            if x - 1 in range ( s ) and y + 1 in range ( v ):
                a.append ( levadol_d )
            desnadol_d = (x + 1, y + 1)
            if x + 1 in range ( s ) and y + 1 in range ( v ):
                a.append ( desnadol_d )
        d = {}
        for elm in a:
            d[elm] = d.get ( elm, 0 ) + 1
        counts = [(j, i) for i, j in d.items ()]
        count, max_elm = max ( counts )
        return max_elm


def brez_sosedov(mine, s, v):
    polja = [(x, y) for x in range ( s ) for y in range ( v )]
    a = []
    if len ( mine ) == 0:
        return set ( polja )
    else:
        for e in mine:
            x, y = e
            levo = (x - 1, y)
            if x - 1 in range ( s ):
                a.append ( levo )
            desno = (x + 1, y)
            if x + 1 in range ( s ):
                a.append ( desno )
            gor = (x, y - 1)
            if y - 1 in range ( v ):
                a.append ( gor )
            dol = (x, y + 1)
            if y + 1 in range ( v ):
                a.append ( dol )
            levagor_d = (x - 1, y - 1)
            if x - 1 in range ( s ) and y - 1 in range ( v ):
                a.append ( levagor_d )
            desnagor_d = (x + 1, y - 1)
            if x + 1 in range ( s ) and y - 1 in range ( v ):
                a.append ( desnagor_d )
            levadol_d = (x - 1, y + 1)
            if x - 1 in range ( s ) and y + 1 in range ( v ):
                a.append ( levadol_d )
            desnadol_d = (x + 1, y + 1)
            if x + 1 in range ( s ) and y + 1 in range ( v ):
                a.append ( desnadol_d )
        if len ( set ( polja ).difference ( set ( a ) ) ) == 0:
            return ( 0, 0 )
        else:
            return set ( polja).difference ( set ( a ) )


def po_sosedih(mine, s, v):
    polja = [(x, y) for x in range (s) for y in range (v)]
    sosedi = dict()
    a = []
    for i in range (9):
        sosedi[i] = set()
    for e in mine:
        x, y = e
        levo = (x - 1, y)
        if x - 1 in range(s):
            a.append(levo)
        desno = (x + 1, y)
        if x + 1 in range(s):
            a.append(desno)
        gor = (x, y - 1)
        if y - 1 in range(v):
            a.append(gor)
        dol = (x, y + 1)
        if y + 1 in range(v):
            a.append(dol)
        levagor_d = (x - 1, y - 1)
        if x - 1 in range(s) and y - 1 in range(v):
            a.append(levagor_d)
        desnagor_d = (x + 1, y - 1)
        if x + 1 in range(s) and y - 1 in range(v):
            a.append (desnagor_d)
        levadol_d = (x - 1, y + 1)
        if x - 1 in range (s) and y + 1 in range(v):
            a.append ( levadol_d )
        desnadol_d = (x + 1, y + 1)
        if x + 1 in range (s) and y + 1 in range (v):
            a.append(desnadol_d)
    d = {}
    for element in a:
        d[element] = d.get(element, 0) + 1
        stetje = [(j, i) for i, j in d.items()]
        presteto, max_element = max(stetje)
    for e in d:
        if d[e] == 1:
            sosedi[1].add(e)
        if d[e] == 2:
            sosedi[2].add(e)
        if d[e] == 3:
            sosedi[3].add(e)
        if d[e] == 4:
            sosedi[4].add(e)
        if d[e] == 5:
            sosedi[5].add (e)
        if d[e] == 6:
            sosedi[6].add(e)
        if d[e] == 7:
            sosedi[7].add(e)
        if d[e] == 8:
            sosedi[8].add(e)
    brez = set(polja).difference(set(a))
    for e in brez:
        sosedi[0].add(e)
    return sosedi


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


