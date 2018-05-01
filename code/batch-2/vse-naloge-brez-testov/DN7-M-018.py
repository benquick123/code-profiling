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
    st = 0
    for mina in mine:
        m_x, m_y = mina
        if (x - 1 == m_x or x == m_x or x + 1 == m_x) and (y - 1 == m_y or y == m_y or y + 1 == m_y):
            if not (x == m_x and y == m_y):
                st += 1
    return st




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
    naj_polje = (0, 0)
    naj_st = 0
    for polje in vsa_polja(s, v):
        x, y = polje
        st = sosedov(x, y, mine)
        if st > naj_st:
            naj_st = st
            naj_polje = polje
    return naj_polje


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
    polja_brez = set()
    for polje in vsa_polja(s, v):
        x, y = polje
        st = sosedov(x, y, mine)
        if st == 0:
            polja_brez.add(polje)
    return polja_brez



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
    slovar = dict()
    for i in range(0, 9):
        slovar[i] = set()

    for polje in vsa_polja(s, v):
        x, y = polje
        st = sosedov(x, y, mine)
        slovar[st].add(polje)

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
    dolzina = 0
    for i in range(0, len(pot) - 1):
        x0, y0 = pot[i]
        x1, y1 = pot[i + 1]
        x = x0 - x1
        if x < 0:
            x *= -1
        dolzina += x
        y = y0 - y1
        if y < 0:
            y *= -1
        dolzina += y
    return dolzina

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
    if x0 == x1:
        if y0 > y1:
            temp = y0
            y0 = y1
            y1 = temp
        for y in range(y0, y1 + 1):
            for mina in mine:
                m_x, m_y = mina
                if x0 == m_x and y == m_y:
                    return False
    elif y0 == y1:
        if x0 > x1:
            temp = x0
            x0 = x1
            x1 = temp
        for x in range(x0, x1 + 1):
            for mina in mine:
                m_x, m_y = mina
                if x == m_x and y0 == m_y:
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
    if len(pot) == 1:
        x0, y0 = pot[0]
        if not varen_premik(x0, y0, x0, y0, mine):
            return False

    for i in range(0, len(pot) - 1):
        x0, y0 = pot[i]
        x1, y1 = pot[i + 1]
        if not varen_premik(x0, y0, x1, y1, mine):
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
    mine = set()
    for y in range(len(polje.split())):
        vrstica = polje.split()[y]
        for x in range(len(vrstica)):
            if vrstica[x] == "X":
                mine.add((x, y))

    return mine, len(polje.split()[0]), len(polje.split())

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


