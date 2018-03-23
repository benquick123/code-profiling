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
    st = 0
    for terka in mine:
        if abs(terka[0] - x) <= 1 and abs(terka[1] - y) <= 1:
            if terka != (x, y):
                st += 1
    return st

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
    """
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

    """
    max = 0
    (n, m) = (0, 0)
    for i in range(s):
        for j in range(v):
            for mina in mine:
                st_min = sosedov(i, j, mine)
                if st_min > max:
                    max = st_min
                    (n, m) = (i, j)
    return (n, m)

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

    brez = set()
    for i in range(s):
        for j in range(v):
            if mine != set():
                for mina in mine:
                    if sosedov(i, j, mine) == 0:
                        brez.add((i, j))
            elif mine == set():
                brez.add((i, j))
    return brez

def dodaj_kljuce():
    dict = {}
    for i in range(9):
        dict[i] = set()
    return dict

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
    mnozica = set()
    slovar = dodaj_kljuce()
    for m in range(9):
        mnozica.clear()
        for i in range(s):
            for j in range(v):
                 if sosedov(i, j, mine) == m:
                    mnozica.add((i, j))
        for element in mnozica:
            slovar[m].add(element)
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
    for i in range(len(pot)):
        if i < (len(pot))-1:
            x1 = pot[i][0]
            y1 = pot[i][1]
            x2 = pot[i+1][0]
            y2 = pot[i+1][1]
            if x1 == x2:
                dolzina += abs(y1 - y2)
            if y1 == y2:
                dolzina += abs(x1 - x2)
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
        print("a11")
        if y0 > y1:
            print("b11")
            premik = y0 - y1
            while premik > 0:
                print("c11")
                for terka in mine:
                    print("d11")
                    if (x0, y0) == terka:
                        print("e11")
                        print((x0, y0), terka)
                        return False
                premik -= 1
                y1 += 1
        if y1 > y0:
            print("b12")
            premik = y1 - y0
            while premik > 0:
                print("c12")
                for terka in mine:
                    print("d12")
                    if (x0, y0) == terka:
                        print("e12")
                        print((x0, y0), terka)
                        return False
                premik -= 1
                y0 += 1

    if y0 == y1:
        print("a2")
        if x0 > x1:
            print("b21")
            premik = x0 - x1
            while premik > 0:
                print("c21")
                for terka in mine:
                    print("d21")
                    if (x0, y0) == terka:
                        print("e21")
                        print((x0, y0), terka)
                        return False
                premik -= 1
                x1 += 1
        if x1 > x0:
            print("b22")
            premik = x1 - x0
            while premik > 0:
                print("c22")
                for terka in mine:
                    print("d22")
                    if (x0, y0) == terka:
                        print("e22")
                        print((x0, y0), terka)
                        return False
                premik -= 1
                x0 += 1
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



