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
    return len([(s,v) for s,v in mine if s >= x-1 and s <= x+1 and v >= y-1 and v <= y+1 and (s != x or v != y) ])


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
    return sorted(zip(list(vsa_polja(s, v)), [sosedov(x, y, mine) for x, y in list(vsa_polja(s, v))]), key=lambda x: x[1])[-1][0] # sortira po drugem


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
    return {(x,y) for x,y in list(vsa_polja(s,v)) if sosedov(x,y,mine) == 0}


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
    return {k:set([(x,y) for (x,y),ss in zip(list(vsa_polja(s, v)), [sosedov(x, y, mine) for x, y in list(vsa_polja(s, v))]) if ss == k]) for k in range(0,9)}


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
    return sum(abs(y1-y2)+abs(x1-x2) for (x1, y1),(x2, y2) in zip([(x,y) for x, y in pot], [(x,y) for x, y in pot][1:]))



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
    #return [False for (mx,my) in mine if mx == x0 and x1 == mx and ((my >= y0 and my <= y1) or (my >= y1 and my <= y0))]
    return not sum([(x,y) in mine for x,y in zip(list(range(x1,x0+1)) + list(range(x0,x1+1))+[x0]*abs(y0-y1), list(range(y1,y0+1)) + list(range(y0,y1+1)) + [y0]*abs(x0-x1))])


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return not bool(sum([not varen_premik(x1,y1,x2,y2,mine) for (x1, y1),(x2, y2) in zip([(x,y) for x, y in pot], [(x,y) for x, y in pot][1:])] + [(xt,yt) in mine for xt,yt in pot]))


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
    #print(polje)
    #print(list(enumerate([list(enumerate(list(vrstica))) for vrstica in polje.split(" ")])))
    #print([(x,y) for znak in [vrstica for vrstica in polje.split(" ")] if znak == "X"])
    #( [[(x,y) for x,znak in enumerate(vrsta) if znak == "X"] for y,vrsta in list(enumerate(polje.split(" ")))] )
    #print(list( (x,y) for skup in [[(x,y) for x,znak in enumerate(vrsta) if znak == "X"] for y,vrsta in list(enumerate(polje.split(" ")))] for (x,y) in skup))
    return set((x,y) for skup in [[(x,y) for x,znak in enumerate(vrsta) if znak == "X"] for y,vrsta in list(enumerate(polje.split(" ")))] for (x,y) in skup), len(list(polje.split(" ")[0])), len([znak for znak in polje.split(" ") if znak != ""])


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
    smer = 1
    x = 0
    y = 0
    smer_d = {1:(0,-1), 2:(1,0), 3:(0,1), 4:(-1,0)}
    pot = [(0,0)]
    for ukaz in ukazi.split("\n"):
        if ukaz == "DESNO":
            smer = smer + 1 if smer < 4 else 1
        elif ukaz == "LEVO":
            smer = smer - 1 if smer > 1 else 4
        else:
            (x,y) = (smer_d[smer][0] * int(ukaz) + x, smer_d[smer][1] * int(ukaz) + y)
            pot += [(x, y)]
    return pot

def sign(n):
    return (n > 0) - (n < 0)


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    ukazi = ""
    smer_d = {(0,-1):1, (1,0):2, (0,1):3, (-1,0):4}
    print(pot)
    smer = 1
    print(list((smer_d[sign(x2-x1),sign(y2-y1)],abs(x1-x2)+abs(y1-y2)) for (x1,y1),(x2,y2) in zip(pot, pot[1:])))
    for nova_smer, koraki in list((smer_d[sign(x2-x1),sign(y2-y1)],abs(x1-x2)+abs(y1-y2)) for (x1,y1),(x2,y2) in zip(pot, pot[1:])):
        stara_smer = smer
        smer = nova_smer
        while nova_smer != stara_smer:
            nova_smer = nova_smer - 1 if nova_smer > 1 else 4
            ukazi += "DESNO"+"\n"
        ukazi += str(koraki)+"\n"
    print(ukazi)
    return ukazi[:-1]



