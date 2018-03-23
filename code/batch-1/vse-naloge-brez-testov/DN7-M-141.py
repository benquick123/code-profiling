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
    stevilo_sosed = 0
    for a, b in mine:
        if a in (x - 1, x, x + 1) and b in (y - 1, y, y + 1) and (a, b) != (x, y):
            stevilo_sosed += 1
    return stevilo_sosed


def slovar_sosedov(s,v,mine):
    slovar = {}
    for i in range(s):
        for j in range(v):
            slovar[(i, j)] = sosedov(i, j, mine)
    return slovar



def najvec_sosedov(mine, s, v):
    slovar = slovar_sosedov(s,v,mine)
    top_sosed= (0,0)
    stevilo = 0
    for x,y in slovar:
        if slovar[(x,y)] > stevilo:
            stevilo = slovar[(x,y)]
            top_sosed = (x,y)
    return top_sosed


def brez_sosedov(mine, s, v):
    slovar = slovar_sosedov(s, v, mine)
    keys = {i for i in slovar.keys() if slovar[i] == 0}
    return keys

def n_sosed(mine,s,v,n):
    slovar = slovar_sosedov(s, v, mine)
    keys = {i for i in slovar.keys() if slovar[i] == n}
    return keys

def po_sosedih(mine, s, v):
    slovar = slovar_sosedov(s,v,mine)
    vrni = {}
    for i in range(9):
       vrni[i] = n_sosed(mine,s,v,i)
    return vrni


########################
# Za oceno 7

def dolzina_poti(pot):
    r= 0
    for i in range(len(pot)-1):
        r = r + abs((pot[i+1][0] - pot[i][0]) + (pot[i+1][1]-pot[i][1]))
    return r


def varen_premik(x0, y0, x1, y1, mine):
    pot = [(x0,y0),(x1,y1)]
    koraki = []
    if x0 > x1:
        a = x0
        x0 = x1
        x1 = a
    if y0 > y1:
        a = y0
        y0 = y1
        y1 = a

    for i in range(dolzina_poti(pot)+1):
        if x0==x1:
            koraki.append((x0,y0+i))
        else:
            koraki.append((x0+i, y0))

    for koordinate in koraki:
        if koordinate in mine:
            return False
    return True



def varna_pot(pot, mine):
    if len(pot)== 1:
        if pot[0] in mine:
            return False
        else:
            return True
    for i in range(len(pot)-1):
        varno = varen_premik(pot[i][0],pot[i][1],pot[i+1][0],pot[i+1][1],mine)
        if varno == False:
            return False
    return True


########################
# Za oceno 8

def polje_v_mine(polje):
    j = 0
    dolzina_vrstice=0
    vrni = set()
    if polje[len(polje)-1] == " ":
        polje = polje[:-1]
    if " " in polje:
        while polje[dolzina_vrstice] != " ":
            dolzina_vrstice += 1
    else:
        dolzina_vrstice = len(polje)
    for i in range(len(polje)):
        if polje[i] == "X":
            vrni.add(((i- j)-(dolzina_vrstice*j),j))
        if polje[i] == " ":
            j+=1
    return vrni,dolzina_vrstice,j+1


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


