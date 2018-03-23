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

    return sum([1 for x1 in range(x - 1, x + 2) for y1 in range(y - 1, y + 2) if (x1, y1) in mine and not (x1 == x and y1 == y)])

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
    """
    slovar = {}

    for key in range(9):
        mnozica = set()
        for x, y in vsa_polja(s, v):
                if key == sosedov(x,y,mine):
                    mnozica.add((x,y))
        slovar[key] = mnozica
    return slovar"""

    return ({key: ({(x,y) for x, y in vsa_polja(s, v) if key == sosedov(x,y,mine)}) for key in range(9)})

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
    """
    max = 0
    for x, y in vsa_polja(s, v):
        if sosedov(x, y, mine) >= max:
            max = sosedov(x, y, mine)
            max_terka = (x, y)
    return max_terka"""

    #return po_sosedih(mine, s, v)[(max(x for x in po_sosedih(mine, s, v) if bool((po_sosedih(mine, s, v)[x]).intersection())))].pop()
    #return ({sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)}).get(max({sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)}))
    return max((kljuc, vrednost.pop()) for kljuc, vrednost in po_sosedih(mine, s, v).items() if vrednost)[1]



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
    """
    mnozica = set()
    for x, y in vsa_polja(s, v):
        if not sosedov(x, y, mine):
            mnozica.add((x, y))
    return mnozica
    """
    return ({(x, y) for x, y in vsa_polja(s, v) if not sosedov(x, y, mine)})

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
    """
    vsota = 0
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        vsota = vsota + abs(y1-y0) + abs(x1-x0)
    return vsota"""
    return sum((abs(y1-y0) + abs(x1-x0)) for (x0, y0), (x1, y1) in zip(pot, pot[1:]))

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
    """
    for x,y in mine:
        if ((y0 == y1 == y and ((x0 <= x <= x1) or (x0 >= x >= x1)) or
             x0 == x1 == x and ((y0 <= y <= x1) or (y0 >= y >= y1)))):
            return False
    return True"""

    return not any(((y0 == y1 == y and ((x0 <= x <= x1) or (x0 >= x >= x1)) or
                     x0 == x1 == x and ((y0 <= y <= x1) or (y0 >= y >= y1)))) for x, y in mine)



def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    """    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if not varen_premik(x0, y0, x1, y1, mine):
            return False

    if len(pot) != 0 and pot[0] in mine:
        return False
    else:
        return True
    """
    return not any(not varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])) and not (len(pot) != 0 and pot[0] in mine)


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
    s = polje
    s = s.split()
    sirina = len(s[0])
    visina = len(s)
    mnozica = set()
    for y in range(visina):
        for x in range(sirina):
            if s[y][x] == "X":
                mnozica.add((x,y))
    return (mnozica, sirina, visina)




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
    x, y = (0, 0) # trenutna pozicija
    pot = [(0, 0)]
    current_pointer = 1
    komande = ukazi.splitlines()
    for ukaz in komande:
        if ukaz.isnumeric():
            if   current_pointer == 0:
                x += int(ukaz)
                pot.append((x, y))
            elif current_pointer == 1:
                y -= int(ukaz)
                pot.append((x, y))
            elif current_pointer == 2:
                x -= int(ukaz)
                pot.append((x, y))
            elif current_pointer == 3:
                y += int(ukaz)
                pot.append((x, y))
        elif ukaz == "DESNO":
            if   current_pointer == 0:
                current_pointer = 3
            elif current_pointer == 1:
                current_pointer = 0
            elif current_pointer == 2:
                current_pointer = 1
            elif current_pointer == 3:
                current_pointer = 2
        elif ukaz == "LEVO":
            if   current_pointer == 0:
                current_pointer = 1
            elif current_pointer == 1:
                current_pointer = 2
            elif current_pointer == 2:
                current_pointer = 3
            elif current_pointer == 3:
                current_pointer = 0
    return pot



def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """
    ukazi = """"""
    current_pointer = 1
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        while True:
            if current_pointer == 0:
                if (x0 + abs(x0-x1), y0) == (x1, y1):
                    ukazi += str(abs(x0-x1)) + "\n"
                    break
                else:
                    ukazi += "DESNO\n"
                    current_pointer = 3

            if current_pointer == 1:
                if (x0, y0 - abs(y0-y1)) == (x1, y1):
                    ukazi += str(abs(y0-y1)) + "\n"
                    break
                else:
                    ukazi += "DESNO\n"
                    current_pointer = 0

            if current_pointer == 2:
                if (x0 - abs(x0-x1), y0) == (x1, y1):
                    ukazi += str(abs(x0-x1)) + "\n"
                    break
                else:
                    ukazi += "DESNO\n"
                    current_pointer = 1

            if current_pointer == 3:
                if (x0, y0 + abs(y0-y1)) == (x1, y1):
                    ukazi += str(abs(y0-y1)) + "\n"
                    break
                else:
                    ukazi += "DESNO\n"
                    current_pointer = 2
    return ukazi



