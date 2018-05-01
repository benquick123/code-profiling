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
    count = 0
    i = y-1
    while i <= y+1:
        j = x-1
        while j <= x+1:
            if (j, i) in mine and (j, i) != (x, y):
                count += 1
            j += 1
        i += 1
    return count



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
    i = 0
    max = (0, 0)
    max_sosedov = 0
    while i < s:
        j = 0
        while j < v:
            if sosedov(i, j, mine) > max_sosedov:
                max_sosedov = sosedov(i, j, mine)
                max = (i, j)
            j += 1
        i += 1
    return max

from collections import *

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
    i = 0
    polja = set()
    while i < s:
        j = 0
        while j < v:
            if sosedov(i, j, mine) == 0:
                polja.add((i, j))
            j += 1
        i += 1
    return polja


from collections import *

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
    dict = defaultdict(set)
    i=0
    q = 0
    while q < 9:
        dict[q]
        q += 1
    while i < s:
        j = 0
        while j < v:
            dict[sosedov(i, j, mine)].add((i, j))
            j += 1
        i += 1
    return dict


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
    i = 0
    dolz = 0
    while i < len(pot)-1:
        prejsnjix = pot[i][0]
        prejsnjiy = pot[i][1]
        if prejsnjix != pot[i+1][0]:
            dolz += abs(prejsnjix-pot[i+1][0])
        elif prejsnjiy != pot[i+1][1]:
            dolz += abs(prejsnjiy-pot[i+1][1])
        i += 1
    return dolz


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
        if y1 > y0:
            i = y1
            j = y0
        else:
            i = y0
            j = y1
        while j <= i:
            if (x0, j) in mine:
                return False
            j += 1

    if y0 == y1:
        if x1 > x0:
            i = x1
            j = x0
        else:
            i = x0
            j = x1
        while j <= i:
            if (j, y0) in mine:
                return False
            j += 1
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
    i = 0
    if len(pot) > 1:
        while i < len(pot) - 1:
            prejsnjix = pot[i][0]
            prejsnjiy = pot[i][1]
            if prejsnjix != pot[i + 1][0]:
                if varen_premik(prejsnjix, prejsnjiy, pot[i+1][0], prejsnjiy, mine) == False:
                    return False
            elif prejsnjiy != pot[i + 1][1]:
                if varen_premik(prejsnjix, prejsnjiy, prejsnjix, pot[i+1][1], mine) == False:
                    return False
            i += 1
        return True
    elif len(pot) == 1:
        return not (pot[0][0], pot[0][1]) in mine
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
    vrstice = polje.split(" ")
    count = 0
    for el in vrstice:
        i = 0
        while i < len(el):
            if el[i] == "X":
                mine.add((i, count))
            i += 1
        count += 1
    return (mine, len(el), count)


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
    kot = 90
    pot = [(0, 0)]
    koordinate = (0, 0)
    for el in ukazi.split("\n"):
        if el == "DESNO":
            if kot == -90:
                kot = 180
            else:
                kot = kot - 90
        elif el == "LEVO":
            if kot == 180:
                kot = -90
            else:
                kot += 90
        elif el != "":
            if kot == 0:
                koordinate = (koordinate[0] + int(el), koordinate[1])
            elif kot == 90:
                koordinate = (koordinate[0], koordinate[1] - int(el))
            elif kot == 180:
                koordinate = (koordinate[0] - int(el), koordinate[1])
            elif kot == -90:
                koordinate = (koordinate[0], koordinate[1] + int(el))
            pot.append(koordinate)
    return pot


def spremeni_kot(kot, smer):
    if smer == "DESNO":
        if kot == -90:
            kot = 180
        else:
            kot -= 90
    else:
        if kot == 180:
            kot = -90
        else:
            kot += 90
    return kot

def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    ukazi = ""
    i = 1
    prejsnjix = pot[0][0]
    prejsnjiy = pot[0][1]
    kot = 90
    while i < len(pot):
        if prejsnjix == pot[i][0]:
            if prejsnjiy < pot[i][1]:
                while kot != -90:
                    kot = spremeni_kot(kot, "DESNO")
                    ukazi += "DESNO\n"
                ukazi += str(abs(pot[i][1] - prejsnjiy)) + "\n"
            else:
                while kot != 90:
                    kot = spremeni_kot(kot, "DESNO")
                    ukazi += "DESNO\n"
                ukazi += str(abs(pot[i][1] + prejsnjiy)) + "\n"
        else:
            if prejsnjix < pot[i][0]:
                while kot != 0:
                    kot = spremeni_kot(kot, "DESNO")
                    ukazi += "DESNO\n"
                ukazi += str(abs(pot[i][0] - prejsnjix)) + "\n"
            else:
                while kot != 180:
                    kot = spremeni_kot(kot, "DESNO")
                    ukazi += "DESNO\n"
                ukazi += str(abs(pot[i][0] + prejsnjix)) + "\n"
        prejsnjix = pot[i][0]
        prejsnjiy = pot[i][1]
        i += 1
    return ukazi


