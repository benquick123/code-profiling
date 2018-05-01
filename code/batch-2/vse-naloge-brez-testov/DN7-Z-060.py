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
def imamoMino(x,y,mine):
    """
        Vrni 1, če je na polju s koordinatami `(x, y)` mina.
        Vrne 0, če na polju ni mine.

        Args:
            x (int): koordinata x
            y (int): koordinata y
            mine (set of tuple of int): koordinate min

        Returns:
            1: imamo mino
            0: nimamo mine
        """
    item = (x,y)
    if item in mine: #
        return 1
    else: return 0


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
    stevec_min = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i > -1 and j > -1 and not (i == x and j == y):
                stevec_min += imamoMino(i, j, mine)
    return stevec_min


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
    iskano_polje = (0, 0)
    max_stevilo_sosedov = 0
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) > max_stevilo_sosedov:
                max_stevilo_sosedov = sosedov(i, j, mine)
                iskano_polje = (i, j)
                # print("(",i,",",j,") - stevilo sosedov",sosedov(i,j,mine))
    return iskano_polje


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
    iskano_polje = set()
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) == 0:  # nimamo mobene mine na sosednjih poljih
                item = (i, j)
                iskano_polje.add(item)  # dodamo polje v množico iskanih polj
    return iskano_polje

def sosedi_s_stevilom_min(mine, s, v, stevilomin):
    iskano_polje = set()
    for i in range(s):
        for j in range(v):
            if sosedov(i, j, mine) == stevilomin:  # imamo stevilo min na sosednjih poljih
                item = (i, j)
                iskano_polje.add(item) #dodamo polje v množico iskanih polj
    return iskano_polje

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
    rezultat = {}
    for k in range(9):  # števila od 0 do 8
        rezultat[k] = sosedi_s_stevilom_min(mine, s, v, k)
    return rezultat

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
    rezultat = 0
    if (len(pot) > 0):
        zacetek_x = pot[0][0]
        zacetek_y = pot[0][1]
        for x, y in pot:
            rezultat += abs(x - zacetek_x) + abs(y - zacetek_y)
            zacetek_y = y
            zacetek_x = x
    return rezultat


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
    if (x0 == x1):  # x sta enaka
        if (y0 > y1):
            for i in range(y1, y0 + 1):
                if imamoMino(x0, i, mine):
                    return False
        else:
            for i in range(y0, y1 + 1):
                if imamoMino(x0, i, mine):
                    return False
    if (y0 == y1):  # y sta enaka
        if (x0 > x1):
            for i in range(x1, x0 + 1):
                if imamoMino(i, y0, mine):
                    return False
        else:
            for i in range(x0, x1 + 1):
                if imamoMino(i, y0, mine):
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
    if (len(pot) > 0): #pot mora obstajati
        x0 = pot[0][0]
        y0 = pot[0][1]
        for x, y in pot: #za vsako koordinato v poti
            if not varen_premik(x0, y0, x, y, mine1): # če je premik varen, če ni varen zaključimo
                return False
            x0 = x #nastavimo nove koordinate za x0 in y0
            y0 = y
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
    polje = polje.strip()  # odstranimo zadnji presledek
    mine = set()
    stevec_x = 0
    stevec_y = 0
    for string in polje:
        if string == 'X':
            mine.add((stevec_x, stevec_y))
            stevec_x += 1
        elif string == '.':
            stevec_x += 1
        elif string == ' ':
            stevec_x = 0
            stevec_y += 1
    return mine, stevec_x, stevec_y + 1


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


