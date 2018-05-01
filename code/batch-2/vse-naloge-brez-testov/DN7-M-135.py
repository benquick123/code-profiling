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
    a=0
    for s, v in mine:
        if (abs(x - s) == 0 and abs(y - v) == 1) or (abs(x - s) == 1 and abs(y - v) == 0) or (abs(x - s) == 1 and abs(y - v) == 1):
            a +=1
    return a
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
    return max([[sosedov(x,y,mine),(x,y)] for x,y in vsa_polja(s, v)])[1]

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
    return set(x[1] for x in[[sosedov(x, y, mine), (x, y)] for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0])

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
    slovar = {r: set() for r in range(0,9)}
    for x,y in vsa_polja(s,v):
        a = sosedov(x,y,mine)
        slovar[a].add((x,y))
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
    n = 0
    for x,j in enumerate(pot):
        if j == pot[-1]:
            break
        else:
            if j[0] != pot[x+1][0]:
                n+= abs(pot[x+1][0]-j[0])
            if j[1] != pot[x+1][1]:
                n+= abs(pot[x+1][1]-j[1])
    return n




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
    n1 = x0
    n2 = y0
    n3 = x1
    n4 = y1
    zakljucek = True
    for x in range(abs((x0-x1))+abs((y0+y1))):
        if n1 != n3 and (n1,n2) not in mine:
            if n3 > n1:
                n1+=1
            elif n3 < n1 and (n1,n2) not in mine:
                n1-= 1
            elif (n1, n2) in mine:
                zakljucek = False
                break
        if n2 != n4:
            if n4 > n2 and (n1,n2) not in mine:
                n2+=1
            elif n4 < n2 and (n1,n2) not in mine:
                n2 -= 1
        elif (n1, n2) in mine:
            zakljucek = False
            break
    if (n1, n2) in mine:
        zakljucek = False
    return zakljucek






def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    zakljucek = True
    for x,y in enumerate(pot):
        if y == pot[-1]:
            if y in mine:
                zakljucek = False
            break
        if varen_premik(y[0],y[1],pot[x+1][0],pot[x+1][1],mine) == False:
            zakljucek = False
    return zakljucek

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
    s,t,v =  0,0,1
    sez = []
    for x,j in enumerate(list(polje)):
        if j == "X":
            sez.append((s, t))
        if j is not " ":
            s+=1
        if j is " " and x is not len(polje)-1:
            s = 0
            t+=1
            v+=1
    return tuple((set(sez),s,v))

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


