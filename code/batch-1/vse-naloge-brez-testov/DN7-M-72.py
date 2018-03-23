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
    sosedi = 0

    for x1,y1 in mine:
        if x == x1-1 and y == y1: #levo od vpisa koordinat
            sosedi += 1
        if x == x1+1 and y == y1: #desno od vpisa koordinat
            sosedi += 1
        if x == x1 and y == y1-1: #zgoraj od vpisa koordinat
            sosedi += 1
        if x == x1 and y == y1+1: #spodaj od vpisa koordinat
            sosedi += 1
        if x == x1-1 and y == y1-1: #levo zgoraj od vpisa koordinat
            sosedi += 1
        if x == x1+1 and y == y1-1: #desno zgoraj od vpisa koordinat
            sosedi += 1
        if x == x1-1 and y == y1+1: #levo spodaj od vpisa koordinat
            sosedi += 1
        if x == x1+1 and y == y1+1: #desno spodaj od vpisa koordinat
            sosedi += 1
    return sosedi

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
    najvecje = 0
    polje = (0, 0)

    for i in range(0, v):
        for j in range(0, s):
            sosedi = sosedov(j, i, mine)
            if sosedi > najvecje:
                najvecje = sosedi
                polje = (j, i)
    return polje

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

    d = set()

    for i in range(0, v):
        for j in range(0, s):
            if sosedov(j, i, mine) == 0:
                d.add((j, i))
    return d


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

    d = {}

    for k in range(0, 9):
        sjet = set()
        for i in range(0, v):
            for j in range(0, s):
                sosedi = sosedov(j, i, mine)
                if sosedi == k:
                    sjet.add((j, i))
        d[k] = sjet
    return d


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

    if not pot:
        return 0

    polje = (pot[0][0], pot[0][1])
    dolzina = 0

    for x, y in pot:
        if x != polje[0]:
            dolzina += abs(x - polje[0])
        if y != polje[1]:
            dolzina += abs(y - polje[1])
        polje = (x, y)

    return dolzina


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

    sjet = [(x0, y0), (x1, y1)]
    dolzina = dolzina_poti(sjet)

    for i in range(0, dolzina+1):
        if (x0, y0) in mine:
            return False
        if x0 < x1:
            x0 += 1
        elif x0 > x1:
            x0 -= 1
        if y0 < y1:
            y0 += 1
        elif y0 > y1:
            y0 -= 1
    return True

def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """

    if not pot:
        return True

    prejsnji = (pot[0][0], pot[0][1])

    for x,y in pot:
        if not varen_premik(prejsnji[0], prejsnji[1], x, y, mine):
            return False
        prejsnji = (x, y)
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

    s = 0
    v = 0
    i = 0
    j = 0
    mine = set()

    for vrstica in polje.split(" "):
        if not vrstica:
            continue
        j = 0
        s = len(vrstica)
        for element in vrstica:
            if element == "X":
                mine.add((j, i))
            j += 1
        v += 1
        i += 1
    return (mine, s, v)


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


#IZPISI

mine = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
print(sosedov(2, 1, mine))

s = 8
v = 4
print(najvec_sosedov(mine, s, v))

print(brez_sosedov(mine, s, v))

print(po_sosedih(mine, s, v))

pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]
print(dolzina_poti(pot))

x0 = 2
y0 = 1
x1 = 6
y1 = 1
mine1 = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
print(varen_premik(x0, y0, x1, y1, mine1))


print(polje_v_mine("X "
        ". "
        ". "
        "X "
        ". "
        "X "
        ". "))


