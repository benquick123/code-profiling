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
    stevilo = 0
    for xmine, ymine in mine:
        if x+1 == xmine:
            if y==ymine or y-1==ymine or y+1==ymine:
                stevilo+=1
        elif x == xmine:
            if y-1==ymine or y+1==ymine:
                stevilo+=1
        elif x-1==xmine:
            if y==ymine or y-1==ymine or y+1==ymine:
                stevilo+=1
    return stevilo

def najvec_sosedov(mine, s, v):
    max=0
    najx=0
    najy=0
    for x in range(0, s):
        for y in range(0, v):
            stevilo = sosedov(x, y, mine)
            if stevilo>max:
                max=stevilo
                najx =x
                najy =y
    terka= (najx, najy)
    return terka


def brez_sosedov(mine, s, v):
    mnozica = set()
    for x in range(0, s):
        for y in range(0, v):
            stevilo = sosedov(x, y, mine)
            if stevilo == 0:
                mnozica.add ((x,y))

    return mnozica

def po_sosedih(mine, s, v):
    dict = {}
    mn0= set()
    mn1=set()
    mn2=set()
    mn3=set()
    mn4=set()
    mn5=set()
    mn6=set()
    mn7=set()
    mn8=set()
    for k in range(0, 9):
        dict.setdefault(k, set())
    for x in range (0, s):
        for y in range (0, v):
            stev = sosedov(x, y, mine)
            terka = (x, y)
            if stev==0:
                mn0.add(terka)

            elif stev==1:
                mn1.add(terka)
            elif stev==2:
                mn2.add(terka)
            elif stev==3:
                mn3.add(terka)
            elif stev==4:
                mn4.add(terka)
            elif stev==5:
                mn5.add(terka)
            elif stev==6:
                mn6.add(terka)
            elif stev==7:
                mn7.add(terka)
            elif stev==8:
                mn8.add(terka)
    dict[0].update(mn0)
    dict[1].update(mn1)
    dict[2].update(mn2)
    dict[3].update(mn3)
    dict[4].update(mn4)
    dict[5].update(mn5)
    dict[6].update(mn6)
    dict[7].update(mn7)
    dict[8].update(mn8)
    return dict


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


def varna_pot(pot, mine):
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


