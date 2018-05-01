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
    for a, b in mine:
        if (a == x or a == x - 1 or a == x + 1) and (b == y or b == y - 1 or b == y + 1) and (a != x or b != y):
            count += 1
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
    sir = 0
    vis = 0
    koordinate = (0, 0)
    st_min = 0
    while sir < s and vis < v:
        tr = sosedov(sir, vis, mine)
        if tr > st_min:
            st_min = tr
            koordinate = (sir, vis)
        if sir < s - 1:
            sir += 1
        else:
            sir = 0
            vis += 1
    return koordinate

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
    sir = 0
    vis = 0
    ni_sosedov = {(404, 404)}
    while sir < s and vis < v:
        if sosedov(sir, vis, mine) == 0:
            ni_sosedov.add((sir, vis))
        if vis < v - 1:
            vis += 1
        else:
            vis = 0
            sir += 1
    ni_sosedov.remove((404, 404))
    return ni_sosedov

def n_sosedov(mine, s, v, n):
    sir = 0
    vis = 0
    n_sosedov = {(404, 404)}
    while sir < s and vis < v:
        if sosedov(sir, vis, mine) == n:
            n_sosedov.add((sir, vis))
        if vis < v - 1:
            vis += 1
        else:
            vis = 0
            sir += 1
    n_sosedov.remove((404, 404))
    return n_sosedov

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
    sez = {}

    slov0 = brez_sosedov(mine, s, v)
    slov1 = n_sosedov(mine, s, v, 1)
    slov2 = n_sosedov(mine, s, v, 2)
    slov3 = n_sosedov(mine, s, v, 3)
    slov4 = n_sosedov(mine, s, v, 4)
    slov5 = n_sosedov(mine, s, v, 5)
    slov6 = n_sosedov(mine, s, v, 6)
    slov7 = n_sosedov(mine, s, v, 7)
    slov8 = n_sosedov(mine, s, v, 8)

    sez[0] = slov0
    sez[1] = slov1
    sez[2] = slov2
    sez[3] = slov3
    sez[4] = slov4
    sez[5] = slov5
    sez[6] = slov6
    sez[7] = slov7
    sez[8] = slov8

    return sez

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
    if pot == []:
        trex, trey = 0, 0
    else:
        trex, trey = pot[0]
    for x, y in pot:
        if y != trey:
            dolzina += abs(y - trey)
            trey = y
        else:
            if x != trex:
                dolzina += abs(x - trex)
                trex = x
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
    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0
    tf = True
    sez = {(404, 404)}
    if x0 != x1:
        for i in range(x0, x1+1):
            sez.add((i, y0))
    if y0 != y1:
        for i in range(y0, y1+1):
            sez.add((x0, i))
    sez.remove((404, 404))
    for e in sez:
        if e in mine:
            tf = False
    if (x0, y0) in mine or (x1, y1) in mine:
        tf = False

    return tf

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    totval = True
    sez = []
    for e in pot:
        sez.append(e)
    sez1 = zip(sez, sez[1:])
    for i in sez1:
        x0, y0 = i[0]
        x1, y1 = i[1]
        val = varen_premik(x0, y0, x1, y1, mine)
        if val == False:
            totval = False
    for e in sez:
        if e in mine:
            totval = False

    return totval


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
    mine = {(404, 404)}
    sv = (polje.split(" ")[0])
    sirina = sv.count(".") + sv.count("X")
    po_vrstici = polje.split(" ")
    for e in po_vrstici:
        if e == "":
            po_vrstici.remove(e)
    visina = len(po_vrstici)
    # visina = polje.count(" ") + 1
    index = 0
    for e in po_vrstici:
        ind_vrstice = index
        ind = 0
        for i in e:
            if i == "X":
                mine.add((ind, ind_vrstice))
            ind += 1
        index += 1
    mine.remove((404, 404))
    vse_skupaj = (mine, sirina, visina)
    return vse_skupaj

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


