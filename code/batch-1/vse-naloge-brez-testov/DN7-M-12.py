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
def vsa_polja2(s,v):
    return ((x, y) for y in range(v) for x in range(s))

########################
# Za oceno 6

def sosedov(x, y, mine):
    return len([(a,b) for a, b in mine if (abs(x - a) == 1 or abs(x - a) == 0) and  (abs(y - b) == 1 or abs(y - b) == 0) and ((x,y) != (a,b))])

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
    return {sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)}.get(max({sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)}))


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
    return {x for x in {(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}}


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
    return {i: {(x,y) for (x,y) in {(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)} if {(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}.get((x,y)) == i}for i in range(0, 9)}


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
    return sum(abs(x1 - x0 + y1 - y0) for (x0, y0), (x1, y1) in zip(pot, pot[1:]))


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
    return len([x for x,y in mine if ((x0 <= x  <= x1) or (x0 >= x  >= x1)) and y0 == y1 == y]) == 0 \
            and len([y for x,y in mine if ((y0 <= y <= y1) or (y0 >= y >= y1))and (x0 == x1 == x)]) == 0


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])]) and (pot == [] or pot[0] not in mine)


########################
# Za oceno 8

def polje_v_mine(polje):
    return {x for x, z in zip(vsa_polja2(len(polje.split()[0]), len(polje.split())), polje.replace(" ", "")) if z == "X"}, len(polje.split()[0]), len(polje.split())

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
    x0,y0 = 0,0
    pot = [(x0,y0)]
    smer = "up"
    for ukaz in ukazi.split("\n"):
        if (ukaz == "LEVO" and smer == "right") or (ukaz == "DESNO" and smer == "left"):
            smer = "up"
            continue
        if (ukaz == "LEVO" and smer == "left") or (ukaz == "DESNO" and smer == "right"):
            smer = "down"
            continue
        if (ukaz == "LEVO" and smer == "down") or (ukaz == "DESNO" and smer == "up"):
            smer = "right"
            continue
        if (ukaz == "LEVO" and smer == "up") or (ukaz == "DESNO" and smer == "down"):
            smer = "left"
            continue
        if ukaz != "LEVO" and ukaz != "DESNO" and smer == "right":
            x0, y0 = (x0 + int(ukaz)), y0
            pot.append((x0,y0))
            continue
        if ukaz != "LEVO" and ukaz != "DESNO" and smer == "left":
            x0, y0 = (x0 - int(ukaz)), y0
            pot.append((x0, y0))
            continue
        if ukaz != "LEVO" and ukaz != "DESNO" and smer == "down":
            x0, y0 = x0, (y0 + int(ukaz))
            pot.append((x0,y0))
            continue
        if ukaz != "LEVO" and ukaz != "DESNO" and smer == "up":
            x0, y0 = x0, (y0 - int(ukaz))
            pot.append((x0,y0))
            continue
    return pot




    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """


def zapisi_pot(pot):
    x0, y0 = 0, 0
    pot1 = []
    smer = "up"
    for x1,y1 in pot:
        if x1 != x0 and smer == "right":
            if x1 - x0 >= 0:
                pot1 += str(abs(x1 - x0))
                x0 = x1
                continue
            if x1 - x0 < 0:
                pot1 += "DESNO", "DESNO", str(abs(x1 - x0))
                x0 = x1
                smer = "left"
                continue
        if x1 != x0 and smer == "up":
            if x1-x0 < 0:
                pot1 += "DESNO", "DESNO", "DESNO", str(abs(x1 - x0))
                smer = "left"
            if x1-x0 >= 0:
                pot1 += "DESNO" , str(abs(x1 - x0))
                smer = "right"
            x0 = x1
            continue
        if x1 != x0 and smer == "left":
            if x1-x0 < 0:
                pot1 += str(abs(x1 - x0))
            if x1-x0 >= 0:
                pot1 += "DESNO", "DESNO", str(abs(x1 - x0))
                smer = "right"
            x0 = x1
            continue
        if x1 != x0 and smer == "down":
            if x1-x0 < 0:
                pot1 += "DESNO" ,  str(abs(x1 - x0))
                smer = "left"
            if x1-x0 >= 0:
                pot1 += "DESNO", "DESNO", "DESNO", str(abs(x1 - x0))
                smer = "right"
            x0 = x1
            continue
        if y1 != y0 and smer == "down":
            if y1-y0 >= 0:
                pot1 += str(abs(y1 - y0))
                y0 = y1
                continue
            if y1 - y0 < 0:
                pot1 += "DESNO", "DESNO", str(abs(y1 - y0))
                smer = "up"
                y0 = y1
                continue
        if y1 != y0 and smer == "right":
            if y1-y0 < 0:
                pot1 += "DESNO", "DESNO", "DESNO", str(abs(y1 - y0))
                smer = "up"
            if y1-y0 >= 0:
                pot1 += "DESNO", str(abs(y1 - y0))
                smer = "down"
            y0 = y1
            continue
        if y1 != y0 and smer == "up":
            if y1-y0 < 0:
                pot1 += str(abs(y1 - y0))
                smer = "up"
            if y1-y0 >= 0:
                pot1 += "DESNO", "DESNO", str(abs(y1 - y0))
                smer = "down"
            y0 = y1
            continue
        if y1 != y0 and smer == "left":
            if y1-y0 < 0:
                pot1 += "DESNO", str(abs(y1 - y0))
                smer = "up"
            if y1-y0 >= 0:
                pot1 += "DESNO", "DESNO", "DESNO", str(abs(y1 - y0))
                smer = "down"
            y0 = y1
            continue
    return  '\n'.join(pot1)




    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """




#================================================================== TESTI ==================================================================


