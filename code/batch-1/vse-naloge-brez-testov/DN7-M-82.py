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

def sosedov(x, y, mine):
    return len((set(((a, b) for a in range(x-1, x+2) for b in range(y-1, y+2) if (a, b) != (x, y)))) & mine)


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

def najvec_sosedov(mine, s, v):
   return max(tuple((x, y) for x, y in set(vsa_polja(s, v))
                if sosedov(x, y, mine) == max(sosedov(x, y, mine) for x, y in set(vsa_polja(s, v)))))


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

def brez_sosedov(mine, s, v):
    return set((x, y) for x, y in set(vsa_polja(s, v)) if sosedov(x, y, mine) == 0)


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

def po_sosedih(mine, s, v):
  return {i: set((x, y) for x, y in set(vsa_polja(s, v)) if i == sosedov(x, y, mine)) for i in range(0, 9)}

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

def dolzina_poti(pot):
    return sum(abs((x2 - x1) + (y2 - y1)) for (x1, y1), (x2, y2) in zip(pot[:], pot[1:]) if x1 != x2 and y1 == y2 or x1 == x2 and y1 != y2)


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

def varen_premik(x0, y0, x1, y1, mine):
    return set(set((x, y0) for x in range(x1, x0 + 1) if y0 == y1 and x0 > x1) or
               set((x, y0) for x in range(x0, x1 + 1) if y0 == y1 and x0 < x1) or
               set((x0, y) for y in range(y0, y1 + 1) if x0 == x1 and y0 < y1) or
               set((x0, y) for y in range(y1, y0 + 1) if x0 == x1 and y0 > y1) or
               set((x0, y0) for y in range(y0) if x0 == x1 and y0 == y1)) & mine == set()


def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """

def varna_pot(pot, mine):
    return bool(all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot[:], pot[1:])])
            and all([varen_premik(x0, y0, x0, y0, mine) for x0, y0 in pot if len(pot) == 1]))

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

def polje_v_mine(polje):
    m = set()
    nov = polje.split()
    y = 0
    for niz in nov:
        x = 0
        for znak in niz:
            if znak == "X":
                m.add((x, y))
            x += 1
        y += 1
    return m, x, y

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

def preberi_pot(ukazi):
    kazalci = ["GOR", "DESNO", "DOL", "LEVO"]
    i = 0
    kazalec = kazalci[i]
    s = ukazi.split()
    x = y = 0
    p = [(x, y)]
    for ukaz in s:
        if ukaz == "DESNO":
            i += 1
            if i == 4:
                i = 0
            kazalec = kazalci[i]
            continue
        if ukaz == "LEVO":
            i -= 1
            if i == -1:
                i = 3
            kazalec = kazalci[i]
            continue
        else:
            if kazalec == "DOL":
                y += int(ukaz)
                p.append((x, y))
            if kazalec == "GOR":
                y -= int(ukaz)
                p.append((x, y))
            if kazalec == "DESNO":
                x += int(ukaz)
                p.append((x, y))
            if kazalec == "LEVO":
                x -= int(ukaz)
                p.append((x, y))
    return p


def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """

def zapisi_pot(pot):
    ukaz = """"""
    kazalci = ["GOR", "DESNO", "DOL", "LEVO"]
    u = ["DESNO", "LEVO"]
    kazalec = kazalci[0]
    for (x0, y0), (x1, y1) in zip(pot[:], pot[1:]):
        razlika_x = x1 - x0
        razlika_y = y1 - y0
        if razlika_y > 0:
            if kazalec == "DESNO":
                ukaz += ("\n" + u[0])
            if kazalec == "GOR":
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
            if kazalec == "LEVO":
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
            ukaz += ("\n" + str(razlika_y))
            kazalec = kazalci[2]
        if razlika_y < 0:
            if kazalec == "LEVO":
                ukaz += ("\n" + u[0])
            if kazalec == "DOL":
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
            if kazalec == "DESNO":
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
            ukaz += ("\n" + str(-razlika_y))
            kazalec = kazalci[0]
        if razlika_x > 0:
            if kazalec == "GOR":
                ukaz += ("\n" + u[0])
            if kazalec == "LEVO":
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
            if kazalec == "DOL":
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
            ukaz += ("\n" + str(razlika_x))
            kazalec = kazalci[1]
        if razlika_x < 0:
            if kazalec == "DOL":
                ukaz += ("\n" + u[0])
            if kazalec == "DESNO":
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
            if kazalec == "GOR":
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
                ukaz += ("\n" + u[0])
            ukaz += ("\n" + str(-razlika_x))
            kazalec = kazalci[3]
    return ukaz

