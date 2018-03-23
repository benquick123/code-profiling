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
    st_min = 0
    x1 = x -1
    y1 = y -1
    x2 = x +1
    y2 = y + 1

    while x1 <= x2:
        y1= y -1
        while y1 <= y2:
            if (x1, y1) in mine:
                if (x, y) not in mine:
                    st_min+=1



            y1 += 1
        x1 += 1
    return st_min

def sosedov1(x, y, mine):
    st_min = 0
    x1 = x -1
    y1 = y -1
    x2 = x +1
    y2 = y + 1
    while x1 <= x2:
        y1= y -1
        while y1 <= y2:
            if (x1, y1) in mine:
                st_min+=1
            y1 += 1
        x1 += 1
    if (x, y) in mine and st_min ==1:
        return True
    else:
        if st_min == 0:
            return 0

def sestevanje_min_na_polju(x, y, mine):
    st_min = 0
    x1 = x - 1
    y1 = y - 1
    x2 = x + 1
    y2 = y + 1
    while x1 <= x2:
        y1 = y - 1
        while y1 <= y2:
            if (x1, y1) in mine:
                st_min += 1
            y1 += 1
        x1 += 1
    if (x, y) in mine:
        return (st_min - 1)

    else:
        return st_min

def najvec_sosedov(mine, s, v):
    x1 = 0
    y1 = 0
    polje =0
    s1, v1 = (s -1), (v -1)

    while s1 >= 0:
        v1 = (v -1)
        while v1 >= 0:
            if sosedov(s1, v1, mine) > polje:
                polje = sosedov(s1, v1, mine)
                x1 = s1
                y1 = v1
            v1 -= 1
        s1 -= 1
    return (x1, y1)


def brez_sosedov(mine, s, v):
    s1, v1 = (s - 1), (v - 1)
    mn = set()
    while s1 >= 0:
        v1 = (v -1)
        while v1 >= 0:
            if sosedov1(s1, v1, mine) == True or sosedov1(s1, v1, mine)== 0 :
                mn.add((s1, v1))
            v1 -= 1
        s1 -= 1
    return mn

def po_sosedih(mine, s, v):
    slovar = {}
    i = 1
    s1, v1 = (s - 1), (v - 1)
    mn = set()
    slovar[0] = brez_sosedov(mine, s, v)
    while i <= 8:
        mn = set()
        s1 = (s -1)
        while s1 >= 0:
            v1 = (v - 1)
            while v1 >= 0:
                if sestevanje_min_na_polju(s1, v1, mine) == i:
                    mn.add((s1, v1))
                v1 -= 1
            s1 -= 1
        slovar[i]= mn
        i +=1
    return slovar





########################
# Za oceno 7

def dolzina_poti(pot):
    i = 0
    sestevek = 0
    while i < (len(pot)-1):

        x1, y1 = pot[i]
        x2, y2 = pot[i+1]
        sestevek +=abs((x1 + y1)-(x2 + y2))
        i+=1
    return sestevek


def varen_premik(x0, y0, x1, y1, mine):
    i = 0
    while i < x1 or i < y1:
        if x0 == x1:
            if y0 < y1:
                while y0 < y1:
                    if (x0, y0) not in mine:
                        y0 +=1
                    else:
                        return False
            else:
                while y1 < y0:
                    if (x0, y0) not in mine:
                        y0 -=1
                    else:
                        return False

        if y0 == y1:
            if x0 < x1:
                while x0 < x1:
                    if (x0, y0) not in mine:
                        x0 +=1
                    else:
                        return False
            else:
                while x1 < x0:
                    if (x0, y0) not in mine:
                        x0 -=1
                    else:
                        return False

        i += 1
    if (x1, y1) not in mine:
        return True
    else:
        return False


def varna_pot(pot, mine):
    i = 0
    varno = True


    if not pot:
        while i < (len(pot)-1):

            x1, y1 = pot[i]
            x2, y2 = pot[i+1]
            if varen_premik(x1, y1, x2, y2, mine) == True:
                varno = True
            else:
                varno = False
                return varno
            i+=1
        return varno
    else:
        if pot[0] not in mine :
            while i < (len(pot) - 1):

                x1, y1 = pot[i]
                x2, y2 = pot[i + 1]
                if varen_premik(x1, y1, x2, y2, mine) == True:
                    varno = True
                else:
                    varno = False
                    return varno
                i += 1
            return varno
        else:
            return False


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


