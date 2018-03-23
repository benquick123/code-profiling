
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

def sosedov(x, y, mine):
    return len([1 for x1, y1 in mine if abs(x - x1) <= 1 and abs(y - y1) <= 1 and (abs(x - x1) + abs(y - y1)) != 0])

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
    return (max([(sosedov(x, y, mine), x, y) for x in range(s) for y in range(v)])[1:])

def brez_sosedov(mine, s, v):
   return { (x, y) for x in range(s) for y in range(v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine,s,v):
    return {i: {(x, y) for x in range(s) for y in range(v) if sosedov(x, y, mine) == i} for i in range(9)}
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
    return (sum([abs(x0 - x1) + abs(y0 - y1) for (x0, y0), (x1, y1) in zip(pot, pot[1:])]))

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
    return [] == (([1 for x in range(min(x0, x1), max(x0 + 1, x1 + 1)) for y in range(min(y0, y1), max(y0 + 1, y1 + 1)) if (x, y) in mine]))

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    return not len(pot) or (all([varen_premik(x0,y0,x1,y1,mine) for (x0, y0),(x1, y1) in zip(pot, pot[1:]) ])  and  pot[0] not in mine)
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
    return ({(x,y) for y in range(len(polje.split())) for x in range(len(polje.split()[0])) if polje.replace(" ", "")[y*len(polje.split()[0])+x] == 'X'},len(polje.split()[0]),len(polje.split()))

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
    lokacija = 0 + 0j
    smer = -1j
    pot = [(0, 0)]
    for n in ukazi.split("\n"):
        if n == "DESNO":
            smer *= 1j
        elif n == "LEVO":
            smer *= -1j
        else:
            n = int(n)
            lokacija += n * smer
            pot.append(tuple((lokacija.real, lokacija.imag)))
    return pot

from cmath import *

from math import *

#def zapisi_pot(pot):
"""
Za podano pot vrni seznam ukazov (glej navodila naloge).

Args:
    pot (list of tuple of int): pot

Returns:
    str: ukazi, napisani po vrsticah
"""

def zapisi_pot(pot):
	lokacija = 0+0j
	smer = -1j
	cela_pot = ""
	for x,y in pot[1:]:
		delta = (complex(x,y)-lokacija)
		for i in range(int((((atan2(smer.imag,smer.real)-atan2(delta.imag,delta.real))* 2 / pi)+4)%4)):
			cela_pot += "LEVO" + "\n"
		cela_pot += str(int((abs(delta/smer)))) + "\n"
		smer = rect(1,atan2(delta.imag,delta.real))
		lokacija = complex(x,y)
	cela_pot = cela_pot.rstrip("\n")
	return cela_pot
print(zapisi_pot([(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]))

