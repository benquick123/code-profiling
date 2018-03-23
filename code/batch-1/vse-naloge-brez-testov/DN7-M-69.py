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
    st_sosedov = 0
    for mina in mine:
        for addX in range(-1, 2):
            for addY in range(-1, 2):
                if(addX !=0 or addY != 0):
                    if mina[0]+addX == x and mina[1]+addY == y:
                        st_sosedov += 1
    return st_sosedov


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
    maxX = 0
    maxY = 0
    max_sosedov = 0
    for currX in range(0, s):
        for currY in range(0, v):
            currSosedov = sosedov(currX, currY, mine)
            if currSosedov > max_sosedov:
                maxX = currX
                maxY = currY
                max_sosedov = currSosedov
    return (maxX, maxY)

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
    brez_sos = set()
    for currX in range(0, s):
        for currY in range(0, v):
            if sosedov(currX, currY, mine) == 0:
                brez_sos.add((currX, currY))
    return brez_sos


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
    slovar_sos = {}
    for x in range(0, 9):
        slovar_sos[x] = set()
    for currX in range(0, s):
        for currY in range(0, v):
            slovar_sos[sosedov(currX, currY, mine)].add((currX, currY))
    return slovar_sos



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
    if pot.__len__() > 0:
        prevPolje = pot[0]
    else: return 0
    for currPolje in pot:
        dolzina += abs(currPolje[0]-prevPolje[0]) + abs(currPolje[1]-prevPolje[1])
        prevPolje = currPolje
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
        for currY in range(min(y0, y1), max(y0, y1)+1):
            if (x0, currY) in mine:
                return False
    else:
        for currX in range(min(x0, x1), max(x0, x1)+1):
            if (currX, y0) in mine:
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
    if pot.__len__() > 0:
        prevPot = pot[0]
    else: return True
    for currPot in pot:
        if not varen_premik(prevPot[0], prevPot[1], currPot[0], currPot[1], mine):
            return False
        prevPot = currPot
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
    s = polje.split()[0].__len__()
    v = polje.split().__len__()
    currRowIdx = 0
    mine = set()
    for currLine in polje.split():
        currColIdx = 0
        for currChar in currLine:
            if(currChar == "X"):
                mine.add((currColIdx, currRowIdx))
            currColIdx+=1
        currRowIdx +=1
    return (mine, s, v)


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
    currDir = 0
    pot = [(0, 0)]
    for currLine in ukazi.splitlines():
        if currLine == "DESNO":
            currDir+=1
            if(currDir == 4):
                currDir = 1
        elif currLine == "LEVO":
            currDir-=1
            if(currDir == -1):
                currDir = 3
        else:
            if currDir == 0:
                pot.append((pot[pot.__len__()-1][0], pot[pot.__len__()-1][1]-int(currLine)))
            if currDir == 1:
                pot.append((pot[pot.__len__()-1][0]+int(currLine), pot[pot.__len__()-1][1]))
            if currDir == 2:
                pot.append((pot[pot.__len__()-1][0], pot[pot.__len__()-1][1]+int(currLine)))
            if currDir == 3:
                pot.append((pot[pot.__len__()-1][0]-int(currLine), pot[pot.__len__()-1][1]))
    return pot




def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """


