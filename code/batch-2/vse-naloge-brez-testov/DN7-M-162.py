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
    return len([(x1, y1) for x1 in range((x - 1), (x + 2)) for y1 in range((y - 1), (y + 2))
                if (x1, y1) in mine and (x1, y1) != (x, y)])


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
    return max([(sosedov(x, y, mine), (x, y)) for (x, y) in vsa_polja(s, v)])[1]


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
    return {(x, y) for (x, y) in vsa_polja(s, v) if sosedov(x, y, mine) == 0}


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
    return {z: {(x, y) for (x, y) in vsa_polja(s, v) if sosedov(x, y, mine) == z} for z in range(9)}


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
    return sum([(abs(x1 - x0) + abs(y1 - y0)) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])


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
    return min([not (z, u) in mine for (z, u) in [(x, y) for x in range(min(x0, x1), max(x0, x1) + 1)
                                                  for y in range(min(y0, y1), max(y0, y1) + 1)]])


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return min([varen_premik(x00, y00, x11, y11, mine) for
                (x00, y00), (x11, y11) in zip(pot, pot[1:] or pot)] or [True])


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
    polja = polje.split()
    s = len(polja[0])
    v = len(polja)
    tacno = []
    yco = -1
    for y in polja:
        yco += 1
        xco = -1
        for x in y:
            xco += 1
            if x == "X":
                tacno.append((xco, yco))
    return set(tacno), s, v


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
    s = 0
    az = (0, 0)
    finalna_lista = [(0, 0)]

    def pravac(v):
        if v <= 0:
            return x, abs(y - z)
        elif v == 1:
            return (x + z), y
        elif v == 2:
            return x, (y + z)
        elif v >= 3:
            return abs(x - z), y

    def smjerovi(vrijednost, smjer):
        if smjer == "DESNO":
            if vrijednost >= 3:
                return 0
            k = vrijednost + 1
            return k
        elif smjer == "LEVO":
            if vrijednost <= 0:
                return 3
            k = vrijednost - 1
            return k

    kreativnost = list(ukazi.split("\n"))
    for k in kreativnost:
        if k == "DESNO" or k == "LEVO":
            s = smjerovi(s, k)
        else:
            z = int(k)
            (x, y) = az
            az = pravac(s)
            finalna_lista.append(az)
    return finalna_lista


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    lista = []
    dolzina = 0
    zadnji = 1
    novi = 0

    def desno(zs, ns):
        if ns > zs:
            return ns - zs
        else:
            return ns + 4 - zs

    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if x0 == x1:
            dolzina = abs(y0 - y1)
            if y0 > y1:
                novi = 1
            else:
                novi = 3
        elif y0 == y1:
            dolzina = abs(x0 - x1)
            if x0 > x1:
                novi = 4
            else:
                novi = 2
        for krat in range(desno(zadnji, novi)):
            lista.append("DESNO")
        lista.append(str(dolzina))
        zadnji = novi
    return "\n".join(lista)


