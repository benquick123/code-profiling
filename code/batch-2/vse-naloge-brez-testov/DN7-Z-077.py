
    




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
    return len(mine.intersection({(x-1,y-1),(x-1,y),(x-1,y+1), (x,y+1), (x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)}))

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
    vsi = dict()
    y = v
    for x in range(0,s):
        for y in range(0,v):
            vsi[sosedov(x,y,mine)] = (x,y)
    najvecji = max(vsi.keys())
    return vsi[najvecji]

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
    vsi = dict()
    brezS = set()
    y = v
    for x in range(0,s):
        for y in range(0,v):
            vsi[(x,y)] = sosedov(x,y,mine)
    for kljuc, vrednost in vsi.items():
        if vrednost == 0:
            brezS.add(kljuc)
        
    return brezS
    

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
    vsi = dict()
    for el in range(0,9):
        vsi[el] = set()
    for x in range(0,s):
        for y in range(0,v):
            sosed = sosedov(x,y,mine)
            if sosed not in vsi.keys():
                vsi[sosed] = set()
                vsi[sosed].add((x,y))
            else:
                vsi[sosed].add((x,y))
        
    return vsi

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
    x = 0
    y = 0
    for el in range(1,len(pot)):
        x += abs(pot[el-1][0] - pot[el][0])
        y += abs(pot[el-1][1] - pot[el][1])
    return x+y

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
    koordinate = set()
    if x0 != x1 and y0 == y1:
        manjsi = min(x0,x1)
        vecji = max(x0,x1)
        for x in range (manjsi, vecji+1):
            koordinate.add((x,y0))
    elif y0!=y1 and x0 == x1:
        manjsi = min(y0,y1)
        vecji = max(y0,y1)
        for y in range (manjsi, vecji+1):
            koordinate.add((x0,y))
    elif x0==x1 and y0==y1:
        mn = {(x0, y0)}
        if len(mn.intersection(mine)) == 1:
            return False
    
        return True
    if len(koordinate.intersection(mine)) == 0:
        return True
    else:
        return False


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    vsi = set()
    if len(pot) == 1 and pot[0] in mine:
        return False
    for el in range(1,len(pot)):
        if varen_premik(pot[el-1][0],pot[el-1][1],pot[el][0],pot[el][1],mine) == False:
            return False
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
    razdeli = polje.split(" ")
    a = len(razdeli)
    b = len(razdeli[0])
    tocke = set()
    for y in range(0,len(razdeli)):
        for el in range(0,len(list(razdeli[y]))):
            if list(razdeli[y])[el] == 'X':
                tocke.add((el, y))
                
    return tocke,b, a


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.
def sosedov1(x, y, mine):
    return len(mine.intersection({(x-1,y-1),(x-1,y),(x-1,y+1), (x,y+1), (x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)}))

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


