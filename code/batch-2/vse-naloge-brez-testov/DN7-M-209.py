



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


def sosedov(x,y,mine):
    return len([(xi, yi) for xi, yi in mine if abs(xi - x) <= 1 and abs(yi - y) <= 1 and not (xi == x and yi == y)])
"""
def sosedov(x, y, mine):
    sosedi = 0
    for x2,y2 in mine:
        if y2 == y and ((x2 == x - 1) or (x2 == x + 1)):
            sosedi += 1
        if y2 == y - 1 and ((x2 == x - 1) or (x2 == x) or (x2 == x + 1)):
            sosedi += 1
        if y2 == y + 1 and ((x2 == x - 1) or (x2 == x) or (x2 == x + 1)):
            sosedi += 1
    return sosedi
"""

#def sosedov(x, y, mine):
 #   return   [ el + 1 for el in mine sosedi = 0 for x2,y2 in mine: sosedi += 1 if (y2 == y and ((x2 == x - 1) or (x2 == x + 1))) or (y2 == y - 1 and ((x2 == x - 1) or (x2 == x) or (x2 == x + 1))) or (y2 == y + 1 and ((x2 == x - 1) or (x2 == x) or (x2 == x + 1))):]



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

#mine = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
def najvec_sosedov(mine, s, v):
    polja = set(vsa_polja(s,v))
    if len(mine) == len(polja):
        return 0,0
    if mine:
        polja = set(vsa_polja(s,v))
        stevilo = 0
        kdo = None

        for x,y in polja:
            if sosedov(x,y,mine) > stevilo:
                kdo = x,y
                stevilo = sosedov(x,y,mine)
        return kdo
    return 1,1
#print(najvec_sosedov({(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)},8,4))

"""
    Vrni koordinati polja z največ sosednjih min

    Args:
        mine (set of (int, int)): koordinate min
        s (int): širina polja
        v (int): višina polja

    Returns:
        tuple of int: koordinati polja

"""


def brez_sosedov(mine, s, v):
    polja = vsa_polja(s,v)
    brez_min = set()
    for x,y in polja:
        if sosedov(x,y,mine) == 0:
            brez_min.add((x,y))
    return brez_min
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

mine =  {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
def po_sosedih(mine, s, v):
    polja = vsa_polja(s,v)
    slovar_sosedov = {}
    for polje in polja:
        slovar_sosedov[polje] = sosedov(polje[0],polje[1],mine)
    slovar = {}
    for i in range(9):
        slovar[i] = set()
        for key,values in slovar_sosedov.items():
            if i == values:
                slovar[i].add(key)
    return slovar
#print(po_sosedih(mine,8,4))
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


########################
# Za oceno 7

def dolzina_poti(pot):
    dolzina = 0
    i = 0
    while i < len(pot) - 1:
        #print("fsafsf")
        #print(i)
        #print("fsafsf")
        if pot[i][0] == pot[i + 1][0] and pot[i][1] < pot[i + 1][1]:
            dolzina += pot[i + 1][1] - pot[i][1]
            #print(dolzina)
        elif pot[i][1] == pot[i + 1][1] and pot[i][0] < pot[i + 1][0]:
            dolzina += pot[i + 1][0] - pot[i][0]
            #print(dolzina)
        elif pot[i][0] == pot[i + 1][0] and pot[i][1] > pot[i + 1][1]:
            dolzina += pot[i][1] - pot[i + 1][1]
            #print(dolzina)
        elif pot[i][1] == pot[i + 1][1] and pot[i + 1][0] < pot[i][0]:
            dolzina += pot[i][0] - pot[i + 1][0]
            #print(dolzina)
        i += 1
    return dolzina
#print(dolzina_poti([(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]))
#print(dolzina_poti([(7,5),(4,5)]))
"""
    Vrni dolžino podane poti, vključno z vmesnimi polji.

    Args:
        pot (list of tuple): seznam koordinat polj

    Returns:
        int: dolžina poti
    """

mine1 = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
def varen_premik(x0, y0, x1, y1, mine):
    polja_vmes = []
    if x0 == x1:
        vecji = max(y0,y1)
        manjsi = min(y0,y1)
        while manjsi <= vecji:
            polja_vmes.append((x0,manjsi))
            manjsi += 1
    elif y0 == y1:
        vecji = max(x0,x1)
        manjsi = min(x0,x1)
        while manjsi <= vecji:
            polja_vmes.append((manjsi,y0))
            manjsi += 1
    for polje in polja_vmes:
        if polje in mine:
            return False
    return True

#print(varen_premik(0, 1, 3, 1, mine1))

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


mine1 = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
def varna_pot(pot, mine):
    if len(pot) == 1 and pot[0] in mine:
        return False
    i = 0
    while i < len(pot) - 1:
        if not varen_premik(pot[i][0],pot[i][1],pot[i + 1][0],pot[i + 1][1],mine):
            return False
        i += 1
    return True
#print(varna_pot([(0, 0), (0, 1), (3, 1)], mine1))
#print(varna_pot([(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)], mine1))
"""
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """


########################
# Za oceno 8

def polje_v_mine(polje):
    mine = set()
    vrstice = polje.split()
    i = 0
    for vrstica in vrstice:
        j = 0
        for crka in vrstica:
            if crka == "X":
                mine.add((j,i))
            j += 1
        i += 1
    return mine,len(vrstice[0]),len(vrstice)
print(polje_v_mine("...X.... .X....X. .XX..... ......X."))
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


