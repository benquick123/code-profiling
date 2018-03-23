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

def sosedov(x, y, mine):
    stevec=0
    for x1, y1 in mine:
        if ((x1 + 1) == x) and y1 == y:
            stevec = stevec + 1
        if ((x1 - 1) == x) and y1 == y:
            stevec = stevec + 1
        if (((x1 + 1) == x) and (y1 + 1 == y)):
            stevec = stevec + 1
        if (((x1 - 1) == x) and (y1 + 1 == y)):
            stevec = stevec + 1
        if ((x1 == x) and (y1 + 1 == y)):
            stevec = stevec + 1
        if (((x1 + 1) == x) and (y1 - 1 == y)):
            stevec = stevec + 1
        if (((x1 - 1) == x) and (y1 - 1 == y)):
            stevec = stevec + 1
        if ((x1 == x) and (y1 - 1 == y)):
            stevec = stevec + 1
    return stevec
def najvec_sosedov(mine, s, v):
    največ_min=0
    maskimum_koordinate=0,0
    for x,y in vsa_polja(s,v):
        vsota_min=sosedov(x,y,mine)
        if vsota_min>največ_min:
            največ_min=vsota_min
            maskimum_koordinate=x,y
    return maskimum_koordinate
def brez_sosedov(mine, s, v):
    seznam_koordinat=set()
    koordinate_brez_min=0,0
    for x,y in vsa_polja(s,v):
        brez_min=sosedov(x,y,mine)
        if brez_min==0:
            koordinate_brez_min=x,y
            seznam_koordinat.add(koordinate_brez_min)
    return seznam_koordinat
def po_sosedih(mine, s, v):
    slovar_sosedi={}
    i=0
    while i <= 8:
        seznam_koordinat = set()
        for x, y in vsa_polja(s, v):
            brez_min = sosedov(x, y, mine)
            if brez_min == i:
                seznam_koordinat.add((x,y))
            slovar_sosedi[i]=seznam_koordinat
        i=i+1
    return slovar_sosedi
def dolzina_poti(pot):
    dolzina = 0
    razdalja2 = 0
    razdalja1 = 0
    for x, y in pot:
        x1 = x
        y1 = y
        break
    for x, y in pot:
        razdalja1 = y - y1
        if razdalja1 < 0:
            razdalja1 = razdalja1 + 2 * (-razdalja1)
        dolzina = dolzina + razdalja1
        razdalja2 = x - x1
        if razdalja2 < 0:
            razdalja2 = razdalja2 + 2 * (-razdalja2)
        dolzina = dolzina + razdalja2
        x1 = x
        y1 = y
    return (dolzina)
def varen_premik(x0, y0, x1, y1, mine):
    for a, b in mine:
        if (x0 <= a <= x1 or x1 <= a <= x0) and (y0 <= b <= y1 or y1 <= b <= y0):
            return False
    return True
def varna_pot(pot, mine):
    for x0, y0 in pot:
        for a, b in mine:
            if x0 == a and y0 == b:
                return False
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        for a, b in mine:
            if (x0 <= a <= x1 or x1 <= a <= x0) and (y0 <= b <= y1 or y1 <= b <= y0):
                return False
    return True
def polje_v_mine(polje):
    sirina=len(polje.split()[0])
    visina=len(polje.split())
    x = 0
    y = 0
    stevec_y = 1
    mnozica_min=set()
    for p in polje:
        if p == ".":
            x = x + 1
        if p == " ":
            y = y + 1
            x = 0
        if p == "X":
            mina = x, y
            x = x + 1
            mnozica_min.add(mina)
    return (mnozica_min,sirina,visina)
