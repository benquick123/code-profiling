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

print (vsa_polja(7,3))
########################
# Za oceno 6

def sosedov(x, y, mine):
    return len((set((d, v) for d in range(x - 1, x + 2) for v in range(y - 1, y + 2)) - {(x, y)}) & mine)


def najvec_sosedov(mine, s, v):
    return max(list(((sosedov(x, y, mine)), x, y) for x,y in vsa_polja(s,v)))[1:]


def brez_sosedov(mine, s, v):
    return set(filter(None, ((x,y) if (sosedov(x, y, mine) == 0) else None for x, y in vsa_polja(s, v))))


def po_sosedih(mine, s, v):
    return {a:(set(filter(None, ((x, y) if (sosedov(x, y, mine) == a) else None for x, y in vsa_polja(s, v))))) for a in range(9)}


########################
# Za oceno 7

def dolzina_poti(pot):
    return sum(abs(x0-x1) + abs(y1-y0) for (x0, y0), (x1, y1) in zip(pot, pot[1:]))


def varen_premik(x0, y0, x1, y1, mine):
    return not bool(set((x,y)
                        for x in (range(x0,x1+1) if x0<=x1 else range(x0,x1-1,-1))
                        for y in (range(y0,y1+1) if y0<=y1 else range(y0,y1-1,-1)))& mine)


def varna_pot(pot, mine):
    return not any(not varen_premik(x0, y0, x1, y1, mine)
                   for (x0, y0), (x1, y1) in (zip(pot, pot[1:]) if len(pot)>1 else zip(pot, pot)))


########################
# Za oceno 8

def polje_v_mine(polje):
    x = 0
    y = 0
    kord = set()
    for znak in polje:
        if znak == 'X':
            kord.add((x, y))
            x += 1
        elif znak == ' ':
            y += 1
            x = 0
        else:
            x += 1

    return kord,x,y+1


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


