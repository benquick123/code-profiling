import collections
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
    return len(set([(x+i, y+z) for i in range(-1, 2) for z in range(-1, 2) if (x+i, y+z) != (x, y)]) & set(mine))



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
    return sorted([(sosedov(x, y, mine), x, y) for x, y in vsa_polja(s, v)], key=lambda e: -e[0])[0][1:]



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
    return set([(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0])


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
    return {n: set([(x, y) for key, x, y in [(sosedov(x, y, mine), x, y) for x, y in vsa_polja(s, v)] if key == n]) for n in range(0, 9)}


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
    return sum([(abs(x1-x2)+abs(y1-y2)) for (x1, y1), (x2, y2) in zip(pot, pot[1:])])

# print(dolzina_poti([(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]))


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

    return len(set([(x0+x, y0) if x0 < x1 else (x0-x, y0) for x in range(0, abs(x1-x0)+1)] + [(x0, y0+y) if y0 < y1 else (x0, y0-y) for y in range(0, abs(y1-y0)+1)]) & mine) ==0
    #return [(x,y0) for x in range(x0, x1, (x1 - x0) // abs(x1 - x0))] + [(x1, y) for y in range(y0, y1, (y1 - y0) // abs(y1 - y0))]
    #return len(set([(x, y0) for x in range_os(x0, x1)]+[([(x, y0) for x in range_os(x0, x1)][-1][0], y) for y in range_os(y0, y1)]) & mine) == 0

# mine1 = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
#
# print(varen_premik(2, 1, 5, 1, mine1))
# print(varen_premik(6,1,2,1, mine1))
# print(varen_premik(1, 1, 0, 0, mine1))
#
# def range_os(x, y):
#     if x>y:
#         return [x for x in range(y, x+1)][::-1]
#     else:
#         return [x for x in range(x, y+1)]



def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])]) if len(pot) > 1 else not bool(set(pot) & mine)

    # if len(pot) > 1:
    #     return all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])
    # elif pot == []:
    #     return True
    # else:
    #     return not bool(set(pot) & mine)

        #return [(x0,y0,x1,y1,mine) for (x0,y0),(x1,y1) in zip(pot,pot[1:])]
#     return True if len(set(pot) & set(mine))==0 else False

# print(varna_pot([(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)], mine1))
# print(varna_pot([(1, 1)], mine1))
# print(len([(1,1)]))
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
    x = []
    vrstice=polje.split(" ")
    for i in vrstice:
        if i == "":
            vrstice.remove("")
    for iv,v in enumerate(vrstice):
        x = x + [(n, iv) for n, c in enumerate(v) if c == "X"]
    return set(x), len(polje.split(" ")[0]),len(vrstice)
    # koordinate_min=[set([(n,iv) for n,c in enumerate(v) if c == "X"]) for iv,v in enumerate(polje.split(" "))]


# print(polje_v_mine("...X.... "
#                                       ".X....X. "
#                                       ".XX..... "
#                                       "......X."))
# print(polje_v_mine("X "". "". ""X "". ""X "". "))
# print(polje_v_mine("...X.... .X....X. .XX..... ......X."))


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
    #smeri = [(1,"+x"),(2,"-y"),(3,"-x"),(4,"+y")]
    c_smeri=4
    tocke=[(0,0)]
    ukazi_seznam = ukazi.splitlines()
    for u in ukazi_seznam:
        if u == "DESNO":
            c_smeri += 1
            if c_smeri > 4: c_smeri = 1
        elif u == "LEVO":
            c_smeri -= 1
            if c_smeri < 1: c_smeri = 4
        else:
            if abs(c_smeri) == 1:
                tocke.append((tocke[-1][0]+int(u), tocke[-1][1]))
            if abs(c_smeri) == 2:
                tocke.append((tocke[-1][0], tocke[-1][1]+int(u)))
            if abs(c_smeri) == 3:
                tocke.append((abs(tocke[-1][0]-int(u)), tocke[-1][1]))
            if abs(c_smeri) == 4:
                tocke.append((tocke[-1][0], abs(tocke[-1][1]-int(u))))
    return tocke

def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    navodila=""
    smer=4
    smerobrata=4
    obrat=1
    obrati=0
    # smeri = [(1,"+x"),(2,"-y"),(3,"-x"),(4,"+y")]
    for (x0,y0),(x1,y1) in zip(pot,pot[1:]):
        if x0<x1 and y0==y1:
            smerobrata=1
            if smerobrata<smer:
                obrati = abs(smerobrata - smer)
                for i in range(obrati):
                    navodila += "LEVO\n"
            else:
                obrati = abs(smerobrata - smer)
                for i in range(obrati):
                    navodila += "DESNO\n"
            navodila += str(abs(x0 - x1)) + "\n"
            smer=smerobrata
        if x0>x1 and y0==y1:
            smerobrata = 3
            if smerobrata<smer:
                obrati = abs(smerobrata - smer)
                for i in range(obrati):
                    navodila += "LEVO\n"
            else:
                obrati = abs(smerobrata - smer)
                for i in range(obrati):
                    navodila += "DESNO\n"
            navodila += str(abs(x0 - x1)) + "\n"
            smer = smerobrata

        if x0 == x1 and y0<y1:
            smerobrata = 2
            if smerobrata<smer:
                obrati = abs(smerobrata - smer)
                for i in range(obrati):
                    navodila += "LEVO\n"
            else:
                obrati = abs(smerobrata - smer)
                for i in range(obrati):
                    navodila += "DESNO\n"
            navodila+= str(abs(y0-y1))+"\n"
            smer = smerobrata

        if x0 == x1 and y0 > y1:
            smerobrata = 4
            if smerobrata<smer:
                obrati = abs(smerobrata - smer)
                for i in range(obrati):
                    navodila += "LEVO\n"
            else:
                obrati = abs(smerobrata - smer)
                for i in range(obrati):
                    navodila += "DESNO\n"
            navodila += str(abs(y0 - y1)) + "\n"
            smer = smerobrata
    return navodila

