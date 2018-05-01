# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
from operator import itemgetter


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


def sosedov(x,y,mine):
    return sum([1 for mina in mine if x-1 <= mina[0] <= x+1 and y-1 <= mina[1] <= y+1 and mina != (x,y)])


def najvec_sosedov(mine,s,v):
    return max([(sosedov(x,y,mine),(x,y)) for x in range(0,s)  for y in range(0,v)],key=itemgetter(0))[1]


def brez_sosedov(mine,s,v):
    return set([(x,y) for x in range(0,s) for y in range(0,v) if sosedov(x,y,mine)==0])




def po_sosedih(mine,s,v):
    slovar = {}
    for kljuc in range(0,9):
        slovar[kljuc] = set()
    slovar[0]=brez_sosedov(mine,s,v)
    for x in range(0,s): #gremo po sirini
        for y in range(0,v): #gremo po visini
            sosedi = sosedov(x,y,mine)
            if 1<=sosedi <= 8:
                slovar[sosedi].add((x,y))
    return slovar



def dolzina_poti(pot):
    vsota = 0
    if pot == []:
        return vsota
    else:
        zacetna = pot[0][0]
        zacetna1= pot[0][1]
        for x,y in pot:
            pristej = 0
            pristej = (zacetna-x) + (zacetna1-y)
            vsota +=abs(pristej)



            zacetna=x
            zacetna1=y

        return vsota


def je_mina(x,y, mine):
    t = (x,y)
    if t in mine:
        return True

    else:
        return False


def varen_premik(x0, y0, x1, y1, mine):

    if(x0<=x1):

        for premik_x in range(x0, x1 + 1):

            if je_mina(premik_x, y0, mine):

                return False


        if (y0 > y1):
            b = y1
            y1 = y0
            y0 = b
            for premik_y in range(y0, y1 + 1):
                if je_mina(x1, premik_y, mine):

                    return False
        else:
            for premik_y in range(y0, y1 + 1):

                if je_mina(x1, premik_y, mine):

                    return False
        return True

    if( x0>=x1):
        a=x1
        x1=x0
        x0=a

        for premik_x in range(x0, x1 + 1):

            if je_mina(premik_x, y0, mine):

                return False
        if(y0>y1):
            b = y1
            y1 = y0
            y0 = b
            for premik_y in range(y0, y1 + 1):

                if je_mina(x1, premik_y, mine):
                    return False
    return True

def varna_pot(pot, mine):


    if len(pot)>1:
        for xi,yi in zip(pot[:-1], pot[1:]):


            if varen_premik(xi[0],yi[0],xi[1],yi[1],mine):

                vrni = True
            if varen_premik(xi[0], yi[0], xi[1], yi[1], mine) is False:

                return False


    elif len(pot)==0:
        vrni = True
    else:
        if je_mina(pot[0][0],pot[0][1],mine)is False:
            vrni = True
        if je_mina(pot[0][0], pot[0][1], mine):

            vrni = False
    return vrni

def polje_v_mine(polje):
    nov = polje.split(" ")
    razcleni=[]
    for n in nov:
        if n != "":
            razcleni.append(n)
    st_vrstic = len(razcleni)
    mine = set()
    trenutna = 0  #trenutna vrstica v kateri smo
    for vrstica in razcleni:
        v = len(vrstica)
        trenutni = 0
        for znak in vrstica:
            if znak == "X":
                mine.add((trenutni,trenutna))
            trenutni += 1
        trenutna+=1
    return mine,v,st_vrstic

