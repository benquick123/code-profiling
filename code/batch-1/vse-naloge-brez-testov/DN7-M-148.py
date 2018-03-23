import collections
import operator
from math import sqrt

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
#    """
#       Vrni število sosedov polja s koordinatami `(x, y)` na katerih je mina.
#       Polje samo ne šteje.
#
#       Args:
#           x (int): koordinata x
#           y (int): koordinata y
#           mine (set of tuple of int): koordinate min
#
#       Returns:
#           int: število sosedov
#       """
#    stevc = 0
#    for poz_X_mine, poz_Y_mine in mine:
#        if (poz_X_mine, poz_Y_mine) != (x, y) and (x - 1) <= poz_X_mine <= (x + 1) and (y - 1) <= poz_Y_mine <= (y + 1):
#            stevc += 1
#    return stevc
    return len([x for poz_X_mine, poz_Y_mine in mine if (poz_X_mine, poz_Y_mine) != (x, y) and (x - 1) <= poz_X_mine <= (x + 1) and (y - 1) <= poz_Y_mine <= (y + 1)])


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
    #presteto = collections.Counter()
    #for x, y in vsa_polja(s, v):
    #    presteto[(x, y)] = sosedov(x, y, mine)
    #return(max(presteto(mine, s, v).items(), key=operator.itemgetter(1))[0])
    return (max({(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}.items(), key=operator.itemgetter(1))[0])


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
    #presteto = collections.Counter()
    #for x, y in vsa_polja(s, v):
    #    presteto[(x, y)] = sosedov(x, y, mine)
    return {koordinata for koordinata, sosedi in {(x, y): sosedov(x, y, mine) for x, y in vsa_polja(s, v)}.items() if sosedi == 0}



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
    #urejeno = {x: set() for x in range(9)}
    #for koordinata, sosedi in presteto(mine, s, v).items():
    #    if sosedi not in urejeno:
    #        urejeno[sosedi] = {koordinata}
    #    else:
    #        urejeno[sosedi].update({koordinata})
    #return urejeno
    return {x: {(x_poz, y_poz) for x_poz, y_poz in vsa_polja(s, v) if sosedov(x_poz, y_poz, mine) == x} for x in range(9)}



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
    return sum(sqrt((drugi[0] - prvi[0])**2 + ((drugi[1] - prvi[1])**2)) for prvi, drugi in zip(pot[0::1], pot[1::1]))

def razdalja(x0, y0, x1, y1):
    return sqrt((x1 - x0)**2 + (y1 - y0)**2)

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
    #for x_koordinata, y_koordinata in mine:
    #    if x_koordinata in range(min(x0, x1), max(x0, x1) + 1) and y_koordinata in range(min(y0, y1), max(y0, y1) + 1):
    #        return False
    #else:
    #    return True
    return (False if False in [False for x, y in mine if min(x0, x1) <= x <= max(x0, x1) and min(y0, y1) <= y <= max(y0, y1)] else True)



def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    #if len(pot) == 1 and pot[0] in mine:
    #    return False
    #for prve_koordinate, druge_koordinate in zip(pot[0::1], pot[1::1]):
    #    if not varen_premik(prve_koordinate[0], prve_koordinate[1], druge_koordinate[0], druge_koordinate[1], mine):
    #        return False
    #return True
    return (False if False in [False for prve_koordinate, druge_koordinate in zip(pot[0::1], pot[1::1])
                               if not varen_premik(prve_koordinate[0], prve_koordinate[1], druge_koordinate[0], druge_koordinate[1], mine)]
            else False if len(pot) == 1 and pot[0] in mine else True)


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
    sirina, visina = len(polje.split()[0]), len(polje.split())
    koordinati = set()
    for index, vrsta in enumerate(polje.split()):
        for index_mine, mina in enumerate(vrsta):
            if mina == "X":
                koordinati.add((index_mine, index))
    return (koordinati, sirina, visina)



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
    smer = 0
    poz_X, poz_Y = (0, 0)
    premiki = [(0, 0), ]
    for i in ukazi.split():
        if i == "DESNO":
            smer += 90
        elif i == "LEVO":
            smer -= 90
        elif i.isnumeric():
            if smer % 360 == 90:
                poz_X, poz_Y = (poz_X + int(i), poz_Y)
                premiki.append((poz_X, poz_Y))
            elif smer % 360 == 180:
                poz_X, poz_Y = (poz_X, poz_Y + int(i))
                premiki.append((poz_X, poz_Y))
            elif smer % 360 == 270:
                poz_X, poz_Y = (poz_X - int(i), poz_Y)
                premiki.append((poz_X, poz_Y))
            elif smer % 360 == 0:
                poz_X, poz_Y = (poz_X, poz_Y - int(i))
                premiki.append((poz_X, poz_Y))
    return premiki


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    od_do_pozicije = {('Levo', 'Levo'): 270, ('Dol', 'Dol'): 180, ('Gor', 'Desno'): 90, ('Gor', 'Dol'): 180, ('Gor', 'Levo'): 270, ('Desno', 'Gor'): 270, ('Desno', 'Dol'): 90, ('Desno', 'Levo'): 180, ('Dol', 'Gor'): 180, ('Dol', 'Desno'): 270, ('Dol', 'Levo'): 90, ('Levo', 'Gor'): 90, ('Levo', 'Desno'): 180, ('Levo', 'Dol'): 270}
    kje_sem_zdej = "Gor"
    poz_x, poz_y = (0, 0)
    zapisana_pot = []
    for ta_x, ta_y in pot:
        print(ta_x, ta_y)

        #if (ta_x, ta_y) == (0, 0):
        #    continue

        if ta_y > poz_y:
            if kje_sem_zdej == "Dol":
                zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Dol")] // 90))
                zapisana_pot[-1] = str(abs((ta_y)))
                poz_x, poz_y = (ta_x, ta_y)
            else:
                zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Dol")] // 90))
                zapisana_pot.append(str(abs((ta_y))))
                poz_x, poz_y = (ta_x, ta_y)
                kje_sem_zdej = "Dol"


        elif ta_y < poz_y:
            if kje_sem_zdej == "Levo":
                zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Levo")] // 90))
                zapisana_pot[-1] = str(abs((ta_y)))
                poz_x, poz_y = (ta_x, ta_y)
            else:
                zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Levo")] // 90))
                zapisana_pot.append(str(ta_y))
                poz_x, poz_y = (ta_x, ta_y)
                kje_sem_zdej = "Levo"

        elif ta_x > poz_x:
            zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Desno")] // 90))
            zapisana_pot.append(str(ta_x))
            poz_x, poz_y = (ta_x, ta_y)
            kje_sem_zdej = "Desno"

        elif ta_x > poz_x:
            zapisana_pot.extend(["DESNO"] * (od_do_pozicije[(kje_sem_zdej, "Gor")] // 90))
            zapisana_pot.append(str(ta_x))
            poz_x, poz_y = (ta_x, ta_y)
            kje_sem_zdej = "Gor"


    print(zapisana_pot)
    return " ".join(zapisana_pot)


