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


    return len([z for z in [(a, b) for a in range(x-1, x+2)  for b in range (y-1, y+2) if a != x or b != y] if z in mine])


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
    najvec_min = 0

    koordinate = (0, 0)

    for x in range(s):
        for y in range(v):
            st_min = sosedov(x, y, mine)
            if st_min > najvec_min:
                najvec_min = st_min
                koordinate = (x, y)

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
    mnozica = set()
    for x in range(s):
        for y in range(v):
            st_min = sosedov(x, y , mine)
            if st_min == 0:
                mnozica.add((x,y))

    return mnozica





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
    slovar = {}

    i = 0
    while i <= 8:
        slovar[i] = set()
        i += 1



    for x in range(s):
        for y in range(v):
            st_min = sosedov(x, y, mine)
            mnozica = slovar[st_min]
            mnozica.add((x, y))
            slovar[st_min] = mnozica



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

    vsota = 0

    for terka1, terka2 in list(zip(pot, pot[1:])):
        x1, y1 = terka1
        x2, y2 = terka2

        if x1 - x2 != 0:
            vsota = vsota + abs(x1 - x2)
        else:
            vsota = vsota + abs(y1 - y2)

    return (vsota)






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

    je_varna = True

    if x0 != x1:
        if x0 < x1:
            while x0 <= x1:
                if(x0, y0) in mine:
                    je_varna = False
                    break
                x0 += 1


        elif x0 > x1:
            while x0 >= x1:
                if (x0, y0) in mine:
                    je_varna = False
                    break
                x0 -= 1

    elif y0 != y1:
        if y0 < y1:
            while y0 <= y1:
                if (x0, y0) in mine:
                    je_varna = False
                    break
                y0 += 1

        elif y0 > y1:
            while y0 >= y1:
                if (x0, y0) in mine:
                    je_varna = False
                    break
                y0 -= 1

    else:
        if (x0, y0) in mine:
            je_varna = False

    return je_varna







def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """

    if(len(pot)) == 1:
        x0, x1 = pot[0]
        if (x0, x1) in mine:
            return False
        else:
            return True

    else:
        for terka1, terka2 in list(zip(pot, pot[1:])):
            x0, y0 = terka1
            x1, y1 = terka2
            if varen_premik(x0, y0, x1, y1, mine) == False:
                return False
                break
        else:
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

    x = 0
    y = 0
    mine = set()

    for znak in polje:
        if znak == " ":
            y += 1
            x = 0

        elif znak == "X":
            mine.add((x, y))
            x += 1
            a = x
            b = y

        elif znak == ".":
            x += 1
            a = x
            b = y


    return (mine, a ,b+1)


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


