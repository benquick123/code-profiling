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
    return len([(a,b) for a,b in mine if a in range(x-1,x+2) and b in range(y-1,y+2) and (x,y) != (a,b)])


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
    return max(vsa_polja(s,v), key=lambda x: sosedov(x[0],x[1],mine))

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
    return set(filter(lambda x: sosedov(x[0],x[1],mine)==0,vsa_polja(s,v)))


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
    return dict(enumerate(set(filter(lambda x: sosedov(x[0],x[1],mine)==i,vsa_polja(s,v))) for i in range(0,9)))


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
    return sum(abs(x1-x0+(y1-y0)) for (x0, y0), (x1, y1) in zip(pot, pot[1:]))


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
    return not (list(filter(lambda x: ((y0<=x[1]<=y1 or y0>=x[1]>=y1) and x0 == x1 == x[0]) or (x0<=x[0]<=x1 or x0>=x[0]>=x1) and y0 == y1 == x[1], mine)))

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return all(varen_premik(x0,y0,x1,y1,mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])) and (len(pot) == 0 or pot[0] not in mine)


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
    a = set()
    for y,x in enumerate(polje):
        if x == "X":
            a.add( ((y%((polje+" ").find(" ")+1)),y//((polje+" ").find(" ")+1)))
    return a,len(polje.split()[0]),len(polje.split())




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
    pot = [(0,0)]
    stopinje = 0
    slovarb = {"DESNO": 90, "LEVO":-90}
    slovar = {90: (1,0), 270: (-1,0), 180: (0,+1), 0: (0,-1)}
    for x in ukazi.split():
        if not x.isnumeric():
            stopinje = stopinje+slovarb[x]
        elif x.isnumeric():
            x = int(x) # pretvori stevilo, ki ga preberv int
            xk = pot[-1][0] # v xk shrani zadnjo x koordinato iz terke pot
            yk = pot[-1][1] # v xy shrani zadnjo y koordinato iz terke pot
            pot.append((xk+(slovar[stopinje%360][0]*x), yk+(slovar[stopinje%360][1]*x))) # po slovarju poišče ključe, ki je stopinje/360 za x in y koordinati in to pomnozi z x (stevilo korakov) + trenutna vrednost koordinat
    return pot  


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """


