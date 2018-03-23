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
    return len([(i,j) for i in range(x-1,x+2) for j in range (y-1,y+2) if (i,j) in mine and (i,j) != (x,y)])


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
    maks_sosedi = {}
    vsi = []
    for i in range(0,s):
        for j in range(0,v):
            stevilo_sosedov = sosedov(i,j,mine)
            maks_sosedi[stevilo_sosedov] = (i,j)
    for k in maks_sosedi:
        vsi.append(k)
    a = max(vsi)
    return maks_sosedi[a]





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
    return {(i,j) for i in range (0,s) for j in range (0,v) if sosedov(i,j,mine) == 0}


    return list(vse)


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
    seznam = {}
    for i in range(9):
        seznam[i] = set()
        for x, y in list(vsa_polja(s, v)):
            kljuce = sosedov(x, y, mine)
            if kljuce not in seznam and kljuce == i:
                seznam[kljuce] = {(x, y)}
            if kljuce in seznam and kljuce == i:
                seznam[kljuce].add((x, y))

    return seznam





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
    premiki_x = []
    premiki_y = []
    vsi_premiki = []
    for i in range(len(pot)):
        if i+1 != len(pot):
            premiki_x.append((pot[i][0], pot[i+1][0]))
            premiki_y.append((pot[i][1],pot[i+1][1]))
    for j in range(len(premiki_x)):
        premik = 0
        if premiki_x[j][0] > premiki_x[j][1]:
                premik = premiki_x[j][0] - premiki_x[j][1]
                for i in range(premik):
                    vsi_premiki.append((i,premiki_y[j][1]))
        if premiki_x[j][0] < premiki_x[j][1]:
                premik_1 = premiki_x[j][1] - premiki_x[j][0]
                for i in range(premik_1):
                    vsi_premiki.append((i,premiki_y[j][1]))
        if premiki_y[j][0] > premiki_y[j][1]:
            premik2 = premiki_y[j][0] - premiki_y[j][1]
            for i in range(premik2):
                vsi_premiki.append((premiki_x[j][0],i))
        if premiki_y[j][0] < premiki_y[j][1]:
            premik3 = premiki_y[j][1] - premiki_y[j][0]
            for i in range(premik3):
                vsi_premiki.append((premiki_x[j][0],i))

    return len(vsi_premiki)

    """
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """


def varen_premik(x0, y0, x1, y1, mine):
    premiki= []
    premiki.append((x0,y0))
    premiki.append((x1,y1))
    if (x0,y0) in mine or (x1,y1) in mine:
        return False
    if x0== x1:
        if y0> y1:
            premik_y1 = y0-y1
            for i in range (1,premik_y1+1):
                premiki.append((x0,y1+i))
                if (x0,y1+i) in mine:
                    return False
        if y0<y1:
            premik_y2 = y1-y0
            for i in range (1,premik_y2+1):
                premiki.append((x0,y0+i))
                if (x0,y0+i) in mine:
                    return False
    if y0==y1:
        if x0> x1:
            premik_x1 = x0-x1
            for i in range (1,premik_x1+1):
                premiki.append((x1+i,y0))
                if (x1+i,y0) in mine:
                    return False
        if x0<x1:
            premik_x2 = x1-x0
            for i in range (1,premik_x2+1):
                premiki.append((x0+i,y0))
                if (x0+i,y0)in mine:
                    return False
    return True
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
    celotna_Pot = []
    premik_x = []
    premik_y = []
    for (x,y) in pot:
        premik_y.append(y)
        premik_x.append(x)
        if(x,y) in mine:
            return False
    for i in range(len(premik_x)):
            if i+1 != len(premik_y):
                if premik_x[i]==premik_x[i+1]:
                    if premik_y[i] > premik_y[i+1]:
                        premik_za= premik_y[i] - premik_y[i+1]
                        for j in range(1,premik_za+1):
                            celotna_Pot.append((premik_x[i],j))
                            if (premik_x[i], j) in mine:
                                return False
                    if premik_y[i] < premik_y[i+1]:
                        premik_za = premik_y[i+1] - premik_y[i]
                        for j in range(premik_y[i], premik_za + 1):
                            celotna_Pot.append((premik_x[i],j))
                            if (premik_x[i],j) in mine:
                                return False
                if premik_y[i] == premik_y[i+1]:
                    if premik_x[i] > premik_x[i+1]:
                        premik_za = premik_x[i] - premik_x[i + 1]
                        for j in range(premik_x[i], premik_za + 1):
                            celotna_Pot.append((j,premik_y[i]))
                            if (j,premik_y[i]) in mine:
                                return False
                    if premik_x[i] < premik_x[i+1]:
                        premik_za = premik_x[i+1] - premik_x[i]
                        for j in range(premik_x[i], premik_za + 1):
                            celotna_Pot.append((j,premik_y[i]))
                            if (j,premik_y[i]) in mine:
                                return False
    return True

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
    y=-1
    x = 0
    cnt_y = 0
    mine_v_polju= set ()
    for mine in polje.split(" "):
        y+=1
        for i in range(len(mine)):
            if "X" in mine[i]:
                mine_v_polju.add((i,y))
            if i != 0:
                x+= 1
        cnt_y+=1

    for i in polje.split(" "):
        x = len(i)

    if " " not in polje:
        cnt_y = 1



    return mine_v_polju,x,cnt_y
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


