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
def koordinate_sosedov(x1, y1):
    """
    Funkcija, ki določi vse možne koordinate sosedov
    """
    return [(x, y) for x, y in vsa_polja(x1 + 2, y1 + 2)
            if (abs(x1 - x) == 0 and abs(y1 - y) == 1)
            or (abs(x1 - x) == 1 and abs(y1 - y) == 0)
            or (abs(x1 - x) == 1 and abs(y1 - y) == 1)]

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
    return len([sosed for sosed in koordinate_sosedov(x, y) if sosed in mine])


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
    return max([(sosedov(x, y, mine), x, y)for x, y in vsa_polja(s, v)])[1:]

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
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

import collections
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
    slovar = collections.defaultdict(set)
    for x, y in vsa_polja(s, v):
        stevilo_min = sosedov(x, y, mine)
        slovar[stevilo_min].add((x, y))
    for i in range(1, 9):
        if i not in slovar:
            slovar[i] = set()
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
    return sum([abs(x1 - x2) if x1 != x2 else abs(y1 - y2) for (x1, y1), (x2, y2) in zip(pot, pot[1:])])


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
    sestavi_pot = [(x0, y0)]
    if x0 < x1:
        for i in range(0, x1 - x0 + 1):
            sestavi_pot.append((x0 + i, y0))
    if x0 > x1:
        for i in range(0, x0 - x1 + 1):
            sestavi_pot.append((x0 - i, y0))
    if y0 < y1:
        for i in range(0, y1 - y0 + 1):
            sestavi_pot.append((x0, y0 + i))
    if y0 > y1:
        for i in range(0, y0 - y1 + 1):
            sestavi_pot.append((x0, y0 - i))
    for i in sestavi_pot:
        if i in mine:
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
    varna = []
    if len(pot) == 1:
        if pot[0] in mine:
            varna.append(False)
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        varna.append(varen_premik(x0, y0, x1, y1, mine))
    return all(varna)

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
    koordinate_min = set()
    vrstica = 0
    polje = polje.strip()
    for line in polje.split(" "):
        for indeks, simbol in enumerate(line):
            if simbol == "X":
                koordinate_min.add((indeks, vrstica))
        vrstica += 1
    return koordinate_min, len(line), vrstica

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

    pot = [(0, 0)]
    smer = 0
    koraki = None
    for ukaz in ukazi.split("\n"):
        if ukaz == "DESNO":
            smer += 1
            if smer == 4:
                smer = 0
        if ukaz == "LEVO":
            smer -= 1
            if smer == -4:
                smer = 0
        if ukaz.isnumeric():
            koraki = int(ukaz)
        if koraki:
            nova_pot = None
            xz, yz = pot[-1]
            if smer == 0:
                nova_pot = xz, yz - koraki
            if smer == 1 or smer == -3:
                nova_pot = xz + koraki, yz
            if smer == 2 or smer == -2:
                nova_pot = xz, yz + koraki
            if smer == 3 or smer == -1:
                nova_pot = xz - koraki, yz
            pot.append(nova_pot)
            koraki = None
    return pot

# Pomožna funkcija
def racunaj_smer(smer, kam):
    navodila_desno = 0
    while smer != kam:
        navodila_desno += 1
        smer += 1
        if smer == 4:
            smer = 0
    return navodila_desno * ["DESNO"], smer


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    smer = 0
    navodila = []
    for (x1, y1), (x2, y2) in zip(pot, pot[1:]):
        if x1 < x2:
            navodila_desno, smer = racunaj_smer(smer, 1)
            korak = abs(x1 - x2)
        if x1 > x2:
            navodila_desno, smer = racunaj_smer(smer, 3)
            korak = abs(x1 - x2)
        if y1 > y2:
            navodila_desno, smer = racunaj_smer(smer, 0)
            korak = abs(y1 - y2)
        if y1 < y2:
            navodila_desno, smer = racunaj_smer(smer, 2)
            korak = abs(y1 - y2)
        navodila += navodila_desno
        navodila.append(str(korak))
    return "\n".join(navodila)



