import math

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

    #print(sum([abs((x-v))<= 1 and abs((y-c))<= 1 and (abs((x-v))!= 0 or abs((y-c))!=0)  for v, c in mine]))
    return (sum([abs((x-v))<= 1 and abs((y-c))<= 1 and (abs((x-v))!= 0 or abs((y-c))!=0)  for v, c in mine]))

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
    naj_vred = 0
    koor = (0,0)
   # print(mine, s, v)
    for x in range(s):
        for y in range(v):
            if naj_vred<sosedov(x, y, mine):
                naj_vred = sosedov(x, y, mine)
                koor=(x, y)
    #return max(sosedov(x, y mine) for x in range(s))

    return koor

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
    koordinate_brez_sosedov=set()
    for x in range(s):
        for y in range(v):
            if sosedov(x, y, mine) == 0:
                koordinate_brez_sosedov.add((x, y))
    return koordinate_brez_sosedov

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
    slov = {}
    for i in range(0,9):
        slov[i] = set()
    for x in range(s):
        for y in range(v):
            ele = set()
            st = sosedov(x, y, mine)
            if st in slov:
                ele = slov[st]
                ele.add((x,y))
                slov[st] = ele

    return slov




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
    return int(sum((math.hypot(x[0] - y[0], x[1] - y[1]) for x, y in zip(pot, pot[1:]))))
    # razdalja = (math.hypot(x[0] - y[0], x[1] - y[1]) for x, y in zip(pot, pot[1:]))
    # ses_raz = sum(razdalja)
    # return (int(ses_raz))


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
   # plusminus=1
    n0 = 0
    n1 = 0

    aliX = True

    if x0 == x1:
       # plusminus = -1
        n0 = max((y0, y1))
        n1 = min((y0, y1))
        aliX = True
    elif y0 == y1:
        #plusminus = -1
        n0 = max((x0, x1))
        n1 = min((x0, x1))
        aliX = False

    dane = True
    for i in range(n1, n0):
        if aliX==True and sosedov(x0, i, mine) != 0:
            dane = True
        elif aliX==False and sosedov(i, y0, mine) != 0:
            dane = True
        else:
            dane = False
        if dane == False:
            break
    return dane


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


