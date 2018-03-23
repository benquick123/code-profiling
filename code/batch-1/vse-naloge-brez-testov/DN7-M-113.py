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
    b = 0
    for i in mine:
        if i[1] == y or i[1]==y-1 or i[1]==y+1:
            if i[0] == x-1 or i[0] == x or i[0] == x+1:
                b+=1
                if i[0] == x and i[1] == y:
                    b-=1
    return(b)

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
    #return ((x,y) for x,y in mine for j in range(s) for g in range(v) if max(sosedov(x, y, mine)))
    a = (0,0)
    i = 0
    for j in range (s):
        for g in range(v):
            if sosedov(j, g, mine) > i:
                i = sosedov(j, g, mine)
                a = (j,g)
    return(a)

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
    a = []
    i = 0
    for j in range(s):
        for g in range(v):
            if sosedov(j, g, mine) == i:
                a.append((j,g))
    return (set(a))

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
    a = {j: set() for j in range(9)}
    for j in range(s):
        for g in range(v):
            i = sosedov(j, g, mine)
            if i in a:
                b = a[i]
                b.add((j, g))
                a[i] = (b)
            else:
                b = []
                b.append((j,g))
                b = set(b)
                a[i] = (b)
    return(a)

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
    i=0
    if len(pot) == 0:
        a = 0
        b = 0
    else:
        a = pot[0][0]
        b = pot[0][1]
    for x,y in pot:
        if x > a and y == b or x < a and y == b:
            i = i + abs(x-a)
        if y > b and x == a or y < b and x == a :
            i = i + abs(y-b)
        a = x
        b = y
    return(i)


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
    sez = []
    if x0 == x1:
        if y0 < y1:
            while y0 < y1:
                sez.append((x0,y0))
                y0+=1
        else:
            while y0 > y1:
                sez.append((x0,y0))
                y0-=1
    else:
        if x0 < x1:
            while x0 < x1:
                sez.append((x0,y0))
                x0+=1
        else:
            while x0 > x1:
                sez.append((x0,y0))
                x0-=1
    for i in sez:
        if i in mine:
            return(False)
            break
    if (x0,y0) in mine or (x1,y1) in mine:
        return(False)
    else:
        return(True)
def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    if len(pot) > 1:
        a = pot[0][0]
        b = pot[0][1]
        for x,y in pot:
            if x==a and y ==b:
                a = x
            else:
                if varen_premik(a, b, x, y, mine):
                    a = x
                    b = y
                else:
                    return(False)
        return(True)
    elif len(pot)==1:
        if pot[0] in mine:
            return(False)
        else:
            return(True)
    else:
        return(True)
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
    sez = []
    a = polje.split()
    s = len(a[0])
    v = len(a)
    for y in range (0,len(a)):
        for x in range (0,len(a[y])):
            if a[y][x] == "X":
                polje = (x,y)
                sez.append(polje)
    return((set(sez),s,v))




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


