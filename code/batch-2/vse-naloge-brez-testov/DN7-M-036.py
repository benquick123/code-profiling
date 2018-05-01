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
    for (x1, y1) in mine:
        if (x1,y1) != (x, y):
            if abs((x - x1)) <= 1 and abs((y - y1)) <= 1:
                st_sosedov +=  1
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
    vsa_mozna_polja = vsa_polja(s, v)
    naj_kordinate = (0,0)
    naj_st = 0

    for x1, y1 in vsa_mozna_polja:
        if sosedov(x1, y1, mine) < naj_st:
            pass
        else:
            naj_st = sosedov(x1, y1, mine)
            naj_kordinate = (x1, y1)
    return naj_kordinate

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
    
    vsa_mozna_polja = vsa_polja(s, v)
    vsi_brez_sosedov = set()

    for x1, y1 in vsa_mozna_polja:
        if sosedov(x1, y1, mine) == 0:
            sosed = (x1, y1)
            vsi_brez_sosedov.add(sosed)
    return vsi_brez_sosedov

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
    
    vsa_mozna_polja = vsa_polja(s, v)
    sosedje = {}

    for i in  range(9):
        sosedje[i] = set()

    for x1, y1 in vsa_mozna_polja:
        koordinate = (x1, y1)
        kor_sosedov = sosedov(x1, y1, mine)
        sosedje[kor_sosedov].add(koordinate)
    return sosedje


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
    
    dolzina_poti = 0
    razdalja_med_točkama = 0
    for i in range(len(pot[:-1])):
        x1, y1 = pot[i]
        x2, y2 = pot[i + 1]
        if x1 != x2:
            dolzina_poti += abs(x2 - x1)
        elif y1 != y2:
            dolzina_poti += abs(y2 - y1)   
    return dolzina_poti

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

    if x1 > x0:
        return all(([(x, y) not in mine for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)]))
    elif x0 > x1:
        return all(([(x, y) not in mine for x in range(x1, x0 + 1) for y in range(y0, y1 + 1)]))
    elif y1 > y0:
        return all(([(x, y) not in mine for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)]))
    elif y0 > y1:
        return all(([(x, y) not in mine for x in range(x0, x1 + 1) for y in range(y1, y0 + 1)]))

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    varna_pot = []

    for i in range(len(pot[:-1])):
        x0, y0 = pot[i]
        x1, y1 = pot[i + 1]
        varna_pot.append(varen_premik(x0, y0, x1, y1, mine))

    if varna_pot == []:
        varna_pot.append(True)
        for x in range(len(pot)):
            x0, y0 = pot[x]
            if (x0, y0) in mine:
                varna_pot.append(False)
            else:
                varna_pot.append(True)

    return all(varna_pot)


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

    celotno_polje = polje.split()
    mine = set()

    rezultat = list()

    x = 0
    y = 0

    s = 0
    v = len(celotno_polje)

    for i in range(len(celotno_polje)):
        trenutno_polje =  celotno_polje[i]
        x = 0
        s = 0
        for a in range(len(trenutno_polje)):
            trenutne_koordinate = (x, y)
            if trenutno_polje[a] == "X":
                mine.add((trenutne_koordinate))
            x += 1
            s += 1
        y += 1

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

def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """

