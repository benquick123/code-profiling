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
    st_sosedov = 0

    zgorni_sosed_levi = (x - 1, y - 1)
    zgorni_sosed = (x, y - 1)
    zgorni_sosed_desni = (x + 1, y - 1)

    srednji_sosed_levi = (x - 1, y)
    srednji_sosed_desni = (x + 1, y)

    spodnji_sosed_levi = (x - 1, y + 1)
    spodnji_sosed = (x, y + 1)
    spodnji_sosed_desni = (x + 1, y + 1)

    mozni_sosedi = {zgorni_sosed_levi, zgorni_sosed, zgorni_sosed_desni,
                    srednji_sosed_levi, srednji_sosed_desni,
                    spodnji_sosed_levi, spodnji_sosed, spodnji_sosed_desni}

    for x in mine:
        for y in mozni_sosedi:
            if x == y:
                st_sosedov += 1
                break

    return st_sosedov
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


def najvec_sosedov(mine, s, v):
    najvec_st_sosedov = 0
    koordinate_za_najvec_st_sosedov = (0, 0)

    for x in range(s):
        for y in range(v):
            st_sosedov = sosedov(x, y, mine)
            if st_sosedov > najvec_st_sosedov:
                najvec_st_sosedov = st_sosedov
                koordinate_za_najvec_st_sosedov = (x, y)

    return koordinate_za_najvec_st_sosedov
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """


def brez_sosedov(mine, s, v):
    mnozica_brez_sosedov = set()
    for x in range(s):
        for y in range(v):
            st_sosedov = sosedov(x, y, mine)
            if st_sosedov == 0:
                koordinate_brez_sosedov = (x, y)
                mnozica_brez_sosedov.add(koordinate_brez_sosedov)

    return mnozica_brez_sosedov
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


def po_sosedih(mine, s, v):
    slovar ={0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
    for x in range(s):
        for y in range(v):
            kljuc = sosedov(x, y, mine)
            koordinate = (x, y)
            slovar[kljuc].add(koordinate)
    return slovar

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


########################
# Za oceno 7

def dolzina_poti(pot):
    dolzina = 0
    prejsni_x = 0
    prejsni_y = 0
    i = 0

    for x in pot:
        i += 1
        if (i == 1):
            prejsni_x = x[0]
            prejsni_y = x[1]
        else:
            if x[0] != prejsni_x:
                dolzina += abs(x[0] - prejsni_x)
                prejsni_x = x[0]
            if x[1] != prejsni_y:
                dolzina += abs(x[1] - prejsni_y)
                prejsni_y = x[1]

    return dolzina
    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    ali_je_varno = True
    x = x0
    y = y0

    for i in mine:
        if i[0] == x and i[1] == y:
            ali_je_varno = False
            break

    for i in mine:
        if i[0] == x1 and i[1] == y1:
            ali_je_varno = False
            break

    while x != x1 and ali_je_varno == True:
        for i in mine:
            if i[0] == x and i[1] == y0:
                ali_je_varno = False
                break
        if x > x1:
            x -= 1
        else:
            x += 1

    while y != y1 and ali_je_varno == True:
        for j in mine:
            if j[1] == y and j[0] == x0:
                ali_je_varno = False
                break
        if y > y1:
            y -= 1
        else:
            y += 1

    return ali_je_varno
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
    ali_je_pot_varna = True
    x = None
    y = None

    for i in pot:
        if x != None and y != None:
            ali_je_pot_varna = varen_premik(x,y,i[0],i[1],mine)
            if ali_je_pot_varna == False:
                break
        else:
            for j in mine:
                if j[0] == i[0] and j[1] == i[1]:
                    ali_je_pot_varna = False
                    break
        x = i[0]
        y = i[1]

    return ali_je_pot_varna
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
    s = 0
    v = 0
    seznam_min = (set(), s, v)

    x = 0
    y = 0

    for znak in polje:
        if znak == ' ':
            y += 1
            x = -1
        if znak == 'X':
            mina = (x, y)
            seznam_min[0].add(mina)
        x += 1

    s = x
    v = y + 1
    seznam_min = (seznam_min[0], s, v)

    return seznam_min
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


