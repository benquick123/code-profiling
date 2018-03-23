# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.


'''
Ko odpreš navodila za nalogo, in vidiš, da mora bit vse v eni vrstici.

Malo za šalo.


░░░▄▄▄▄▄▄▄▄░░░░░░░
░▄▀░▄░░░▄░░▀▄░░░░░
█░░░█░░░█░░░░█░░░░
█░░░▀░░░▀░░░░█▄░░░
▀▄░░▄▄▄▄░░░░▄▀██▄░
░░▀▄▄▄▄▄▄▄▄▀░░░██▀
░░░░░░░█░░░░░░███░
░░░░░░░█░░░░░░░░█░
░░░░░▄▄█▄▄▄▄▄▄▄▀░░
░░░░█░░█░░░░░░░░░░
░░░░█░░█░░░░░░░░░░
░░░░▀░░█░░░░░░░░░░
░░░░░▄▀▀▀▄░░░░░░░░
░░░░░█░░░█░░░░░░░░
░░░░░█░░░█░░░░░░░░

'''


from math import sqrt
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
    return sum([1 for a, b in mine if (abs(x - a) < 2 and abs(y - b) < 2) and (a, b) != (x, y)])

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
    return max({sosedov(x,y, mine):(x, y) for x, y  in vsa_polja(s, v)}.items())[1]

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
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

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
    #d = {i: set() for i in range(0, 9)}
    #for x, y in vsa_polja(s, v):
    #   d[sosedov(x, y, mine)].add((x,y))
    #return d
    #return {sosedov(x, y, mine): set().update((x,y)) for x, y in vsa_polja(s, v) }

    return {i: {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == i} for i in range(0, 9)}

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
    return int(sum([sqrt((t2[0]-t1[0])**2+(t2[1]-t1[1])**2) for t1, t2 in zip(pot, pot[1:])]))

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

    for x, y in mine:
        if x in range(min(x0, x1), max(x0, x1)+1) and y in range(min(y0, y1), max(y0, y1)+1):

            return False

    return True
    """
    return False if False in [False if x in range(min(x0, x1), max(x0, x1)+1) and
                                       y in range(min(y0, y1), max(y0, y1)+1) else True for x, y in mine] \
                                       else True

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """


    #!!! POJASNILO!!!

    # Če je dolžina seznama pot enaka ena je edina možnost da že začnemo na polju na katerem se nahaja mina
    # Ker pa se v eni vrstici neda preverjati ali zip(pot, pot[1:]) sploh obstaja oz ali seznam ni prazen,
    # sem se odločil da to preverjam kar v if stavku. V primeru t = [(1,1)] je zip(t, t[1:]) = [], očitno pa se točka
    # (1, 1) nahaja v množici mine1 --> iz tega sledi, da lahko preverjam če mina obstaja na začetnem polju kar v if
    # stavku - (len(pot) == 1 and pot[0] not in mine) - len(pot) pa preverjam zaradi spodaj napisanega.
    # Če je pot = [], se ne postavimo na nobeno polje, torej ne moremo sprožiti nobene mine (or len(pot) == 0)

    # (len(pot) == 1 and pot[0] not in mine) == True - če ima seznam eno vrednost in ta vrednost ni v množici min, ne
    # pristanemo na mini, torej vrnemo vrednost true.
    # (or len(pot) == 0) == True - če ne opravljamo nobene poti, ne moremo sprožiti nobene mine in vrnemo true.


    # Zavedam se, da je zapis zapleten in težek za branje, ampak ura je trenutno 3:22 AM, in rešitev deluje.
    # Zavedam se tudi, da po vsej verjetnosti obstaja boljša rešitev.

    '''
    Mogoče sem s spodnjo kodo stopil na mino  
     ,-*
    (_)     
    '''
    return True if (False not in [varen_premik(t1[0], t1[1], t2[0], t2[1], mine) for t1, t2 in zip(pot, pot[1:])] and len(pot) > 1) \
                   or ((len(pot) == 1 and pot[0] not in mine) or len(pot) == 0) \
                   else False


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
    return ({(indx, ind ) for ind, y in enumerate(polje.split(" ")) for indx, x in enumerate(y)  if x == "X"},
            len(polje.split(" ")[0]), len(polje.split()))

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
    xzac = 0
    yzac = 0
    polozaj = 4
    ukazi = ukazi.split()
    konc_pot = [(0,0)]
    for ukaz in ukazi:
        if ukaz == "DESNO":
            if polozaj == 4:
                polozaj = 1
            else:
                polozaj += 1
        elif ukaz == "LEVO":
            if polozaj == 1:
                polozaj = 4
            else:
                polozaj -= 1
        elif ukaz.isdigit():
            if polozaj == 1:
                xzac += int(ukaz)
            elif polozaj == 3:
                xzac -= int(ukaz)
            elif polozaj == 2:
                yzac += int(ukaz)
            elif polozaj == 4:
                yzac -= int(ukaz)
            konc_pot.append((xzac, yzac))

    return konc_pot

def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    c = []
    polozaj = 4
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        ''' 
        print("x-x:", x0-x1)
        print("y-y:", y0 - y1)
        print("---")
        '''
        if y1>y0 and x0 == x1:
            while polozaj != 2:
                c.append("LEVO")
                if polozaj == 1:
                    polozaj = 4
                else:
                    polozaj -= 1
            c.append(str(y1-y0))
        elif y0>y1 and x0 == x1:
            while polozaj != 4:
                c.append("LEVO")
                if polozaj == 1:
                    polozaj = 4
                    break
                else:
                    polozaj -= 1
            c.append(str(y0-y1))
        elif x1>x0 and y0 == y1:
            while polozaj != 1:
                c.append("DESNO")
                if polozaj == 4:
                    polozaj = 1
                    break
                else:
                    polozaj += 1
            c.append(str(x1-x0))
        elif x0>x1 and y0 == y1:
            while polozaj != 3:
                c.append("DESNO")
                if polozaj == 4:
                    polozaj = 1
                else:
                    polozaj += 1
            c.append(str(x0-x1))
    return "\n".join(c)


