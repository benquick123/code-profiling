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
    return sum([True for kx, ky in mine if ky in {y, y-1, y+1} and kx in {x, x-1, x+1} and (x != kx or y != ky)])

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
    return max([(sosedov(kx, ky, mine), kx, ky) for kx, ky in vsa_polja(s, v)])[1:]

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
    return {(kx, ky) for kx, ky in vsa_polja(s, v) if sosedov(kx, ky, mine) == 0}

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
    return {i: {(kx, ky) for kx, ky in vsa_polja(s, v) if sosedov(kx, ky, mine) == i} for i in range(0, 9)}

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
    return sum([abs(pot[i + 1][0] - pot[i][0]) + abs(pot[i + 1][1] - pot[i][1]) for i in range(len(pot)-1)])

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
    #return True if dolzina_poti([(x0, y0), (x1, y1)]) == sum([
    #    True for x, y in [
    #        ((kx if x0 < x1 else -kx) + x0, (ky if y0 < y1 else -ky) + y0)
    #        for kx, ky in vsa_polja(abs(x1 - x0) + 1, abs(y1 - y0) + 1)
    #    ] if (x, y) not in mine
    #]) - 1 else False
    return True if all([True for ky in range(dolzina_poti([(x0, y0), (x1, y1)])+1) if x0 == x1 and (x0, y0 + (ky if y1 > y0 else -ky)) not in mine] +
                       [False for ky in range(dolzina_poti([(x0, y0), (x1, y1)])+1) if x0 == x1 and (x0, y0 + (ky if y1 > y0 else -ky)) in mine] +
                       [True for kx in range(dolzina_poti([(x0, y0), (x1, y1)])+1) if y0 == y1 and (x0 + (kx if x1 > x0 else -kx), y0) not in mine] +
                       [False for kx in range(dolzina_poti([(x0, y0), (x1, y1)])+1) if y0 == y1 and (x0 + (kx if x1 > x0 else -kx), y0) in mine]) else False

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return True if all(
        [True for i in range(len(pot) - 1) if varen_premik(pot[i][0], pot[i][1], pot[i + 1][0], pot[i + 1][1], mine)] +
        [False for i in range(len(pot) - 1) if not varen_premik(pot[i][0], pot[i][1], pot[i + 1][0], pot[i + 1][1], mine)] +
        [False for i in range(len(pot)) if (pot[i][0], pot[i][1]) in mine]
    ) else False

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
    sez = []
    for ky, y in enumerate(polje.split(" ")):
        for kx, x in enumerate(y):
            if x == "X":
                sez.append((kx, ky))
    v = len(polje.split())
    s = len(max(polje.split()))
    slov = {(x, y) for x, y in sez}
    return slov, s, v

########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.

#ok

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
    tab = []
    x = y = 0
    tab.append((x, y))
    smer = 0 #0: gor, 1: desno, 2: dol, 3: levo -> smer = smer % 4
    for ukaz in ukazi.split("\n"):
        smer %= 4
        if ukaz == "DESNO":
            smer += 1
        elif ukaz == "LEVO":
            smer -= 1
        else:
            if smer == 0:
                y -= int(ukaz)
            elif smer == 1:
                x += int(ukaz)
            elif smer == 2:
                y += int(ukaz)
            else:
                x -= int(ukaz)
            tab.append((x, y))
    return tab

def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    tab = []
    smer = 0
    for i in range(len(pot)-1):
        if pot[i][0] < pot[i+1][0]:
            nova_smer = 1
        elif pot[i][0] > pot[i+1][0]:
            nova_smer = 3
        elif pot[i][1] < pot[i+1][1]:
            nova_smer = 2
        else:
            nova_smer = 0
        for k in range(abs(nova_smer - smer)):
            if nova_smer - smer >= 0:
                tab.append("DESNO")
            else:
                tab.append("LEVO")
        tab.append(str(dolzina_poti([(pot[i][0], pot[i][1]), (pot[i+1][0], pot[i+1][1])])))
        smer = nova_smer
    return "\n".join(tab)



