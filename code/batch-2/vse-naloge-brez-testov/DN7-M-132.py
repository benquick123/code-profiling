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
    return sum(1 for mina in mine if (x-1 <= mina[0] <= x+1) and (y-1 <= mina[1] <= y+1) and (mina[0] != x or mina[1] != y))


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
    return sorted([(sosedov(x, y, mine), (x, y)) for x in range(s) for y in range(v)])[-1][1]


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
    return {sosedi_polje[1] for sosedi_polje in [(sosedov(x, y, mine), (x, y)) for x in range(s) for y in range(v)] if sosedi_polje[0] == 0}


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
    return {n: polja for n in range(9) for polja in [{(x, y)for (x, y) in vsa_polja(s, v) if sosedov(x, y, mine) == n}]}



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
    return sum(abs(parparov[0][0] - parparov[1][0]) + abs(parparov[0][1] - parparov[1][1])
               for parparov in [((x0, y0), (x1, y1)) for ((x0, y0), (x1, y1)) in zip(pot, pot[1:])])


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
    return not any([mina for mina in mine if (((y0 == y1 == mina[1]) and ((x0 <= mina[0] <= x1) if (x0<x1) else (x0 >= mina[0] >= x1)))
                                                or ((x0 == x1 == mina[0]) and ((y0 <= mina[1] <= y1) if (y0<y1) else (y0 >= mina[1] >= y1))))])


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return not any([((x0, y0), (x1, y1)) for (x0, y0), (x1, y1) in zip(pot, pot[1:]) if not varen_premik(x0, y0, x1, y1, mine)] if (len(pot) > 1)
                   else [prestop for prestop in pot if prestop in mine])


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
    vrstice = polje.split()
    mine = set()
    sirina = len(vrstice[0])
    visina = 0
    for vrstica in vrstice:
        for i, c in enumerate(vrstica):
            if c.lower() == 'x':
                mine.add((i, visina))
        visina += 1
    return (mine, sirina, visina)



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
    pot = [(0,0)]
    gor = 0
    desno = 1
    dol = 2
    levo = 3
    smer = gor
    for ukaz in ukazi.split():
        if ukaz == "DESNO":
            if smer == gor:
                smer = desno
            elif smer == desno:
                smer = dol
            elif smer == dol:
                smer = levo
            elif smer == levo:
                smer = gor
        elif ukaz == "LEVO":
            if smer == gor:
                smer = levo
            elif smer == levo:
                smer = dol
            elif smer == dol:
                smer = desno
            elif smer == desno:
                smer = gor
        else:
            if smer == levo or smer == gor:
                premik = -int(ukaz)
            else:
                premik = int(ukaz)
            if smer == levo or smer == desno:
                pot.append((pot[-1][0] + premik, pot[-1][1]))
            else:
                pot.append((pot[-1][0], pot[-1][1] + premik))
    return pot


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    ukazi = ""
    gor = 0
    desno = 1
    dol = 2
    levo = 3
    smer = gor
    prejsnje_polje = None
    for prehod in pot:
        if prejsnje_polje == None:
            prejsnje_polje = prehod
            continue
        premik_x = prehod[0] - prejsnje_polje[0]
        premik_y = prehod[1] - prejsnje_polje[1]
        if premik_x != 0:
            premik_str = str(abs(premik_x))
            if premik_x > 0:
                if smer == gor:
                    ukazi = ukazi + "\nDESNO\n"
                elif smer == desno:
                    ukazi = ukazi + "\n"
                elif smer == dol:
                    ukazi = ukazi + "\nLEVO\n"
                else:
                    ukazi = ukazi + "\nDESNO\nDESNO\n"
                smer = desno
            elif premik_x < 0:
                if smer == gor:
                    ukazi = ukazi + "\nLEVO\n"
                elif smer == desno:
                    ukazi = ukazi + "\nLEVO\nLEVO\n"
                elif smer == dol:
                    ukazi = ukazi + "\nLEVO\n"
                else:
                    ukazi = ukazi + "\n"
                smer = levo
        elif premik_y != 0:
            premik_str = str(abs(premik_y))
            if premik_y > 0:
                if smer == gor:
                    ukazi = ukazi + "\nDESNO\nDESNO\n"
                elif smer == desno:
                    ukazi = ukazi + "\nDESNO\n"
                elif smer == dol:
                    ukazi = ukazi + "\n"
                else:
                    ukazi = ukazi + "\nLEVO\n"
                smer = dol
            elif premik_y < 0:
                if smer == gor:
                    ukazi = ukazi + "\n"
                elif smer == desno:
                    ukazi = ukazi + "\nLEVO\n"
                elif smer == dol:
                    ukazi = ukazi + "\nLEVO\nLEVO\n"
                else:
                    ukazi = ukazi + "\nDESNO\n"
                smer = gor
        ukazi = ukazi + premik_str
        prejsnje_polje = prehod
    return ukazi










