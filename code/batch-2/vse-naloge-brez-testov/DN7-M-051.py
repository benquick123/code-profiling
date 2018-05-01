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
    return [(x, y) for x in range(s) for y in range(v)]


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
    return sum(True for mina in mine if
               mina == (x + 1, y) or mina == (x - 1, y) or mina == (x, y + 1) or mina == (x, y - 1) or mina == (
               x - 1, y + 1) or mina == (x + 1, y + 1) or mina == (x + 1, y - 1) or mina == (x - 1, y - 1))



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
    return {sosedov(polje[0], polje[1], mine): polje for polje in vsa_polja(s, v)}[
        max({sosedov(polje[0], polje[1], mine): polje for polje in vsa_polja(s, v)})]

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

    return set(polje for polje in vsa_polja(s, v) if sosedov(polje[0], polje[1], mine) == 0)

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
    return {i:set((x,y) for (x,y) in vsa_polja(s,v) if i == sosedov(x,y,mine)) for i in range(9)}





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
    return sum([abs(k1[0] - k2[0]) + abs(k1[1] - k2[1]) for k1, k2 in zip(pot, pot[1:])])

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
    return all([False for y in range(y0,y1+1) if (x0,y) in mine] if x0 == x1 and y0 < y1 else [False for y in range(y1,y0+1) if (x0,y) in mine] if  x0 == x1 and y0 > y1 else [False for x in range(x0,x1+1) if (x,y0) in mine] if y0 == y1 and x0 < x1 else [False for x in range(x1,x0+1) if (x, y0) in mine] if y0 == y1 and x0 > x1 else [False] if (x1,y1) in mine else "k")

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return True if pot == [] else  False if pot[0] in mine else all([varen_premik(premik1[0],premik1[1],premik2[0],premik2[1],mine) for premik1,premik2 in zip(pot,pot[1:])])

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
    for y in range(len(polje.split())):
        for x in range(len(polje.split()[y])):
            if polje.split()[y][x] == "X":
                a.add((x,y))
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
    zac = (0,0)
    pot = [(0,0)]
    y = -1
    x = 0
    if ukazi != None:
        for ukaz in ukazi.split():
            if ukaz == "DESNO":
                if y == -1:
                    y = 0
                    x = 1
                    continue
                if  x == 1:
                    y = 1
                    x = 0
                    continue
                if y == 1:
                    y= 0
                    x = -1
                    continue
                if  x == -1:
                    y = -1
                    x = 0
                    continue
            if ukaz == "LEVO":
                if y == -1:
                    y = 0
                    x = -1
                    continue
                if  x == -1:
                    y = 1
                    x = 0
                    continue
                if y == 1:
                    y= 0
                    x = 1
                    continue
                if  x == 1:
                    y = -1
                    x = 0
            else:
                zac =(zac[0] + int(ukaz)*x , zac[1] + int(ukaz)*y)
                pot.append(zac)
    return pot

def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """

    zapis = ""
    pozicije_x = [0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,
                  1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,]
    pozicije_y = [-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,
                  -1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,-1,0,1,0,]

    pot = zip(pot,pot[1:])
    for premik_iz, premik_na in pot:

        if premik_iz[0] == premik_na[0]:
            for obratov in range(4):
                if premik_na == (premik_iz[0],premik_iz[1] + (abs((premik_na[1]-premik_iz[1]))*pozicije_y[obratov])):
                    zapis += obratov*" DESNO" +" " + str(abs(premik_na[1]-premik_iz[1]))
                    pozicije_y = pozicije_y[obratov:]
                    pozicije_x = pozicije_x[obratov:]
                    break
        if premik_iz[1] == premik_na[1]:
            for obratov in range(4):
                if premik_na == (premik_iz[0]+ (abs((premik_na[0]-premik_iz[0]))*pozicije_x[obratov]),premik_iz[1] ):
                    zapis += obratov*" DESNO" +" " + str(abs(premik_na[0]-premik_iz[0]))
                    pozicije_x = pozicije_x[obratov:]
                    pozicije_y = pozicije_y[obratov:]
                    break



    return zapis


