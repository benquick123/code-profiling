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
    return sum(1 for x1, y1 in mine if x1 in [x - 1, x, x + 1] and y1 in [y - 1, y, y + 1] and not (y == y1 and x == x1))

def najvec_sosedov(mine, s, v):
    return max([(sosedov(x,y,mine),x,y) for x,y in vsa_polja(s,v)])[1:]

def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}

def po_sosedih(mine, s, v):
    return {a:{(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine) == a} for a in range(9)}

########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([(abs(x0-x1) + abs(y0-y1)) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])

def varen_premik(x0, y0, x1, y1, mine):
    return not bool([(x,y) for x in range(min(x0,x1),max(x0,x1)+1) for y in range(min(y0,y1), max(y0,y1)+1) if (x,y) in mine])

def varna_pot(pot, mine):
    return not bool([1 for a in pot if a in mine] + [1 for (x0, y0), (x1, y1) in zip(pot, pot[1:]) if not (varen_premik(x0, y0, x1, y1, mine))])


########################
# Za oceno 8

def polje_v_mine(polje):
    sirina = 1
    visina = 1
    x = -1
    y = 0
    mine = set()
    for znak in polje:
        if znak == "." or "X":
            x += 1
        if znak == "X":
            mine.add((x,y))
        if znak == " ":
            sirina = x
            y += 1
            x = -1
            visina += 1
    if visina == 1:
        sirina = x+1
    return (mine,sirina,visina)


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    pot = [(0,0)]
    x = y = l = d = 0
    smer = 0
    for ukaz in ukazi.split('\n'):
        if ukaz == "DESNO":
            d += 1
        elif ukaz == "LEVO":
            l += 1
        else:
            premik = int(ukaz)
            smer = ((max(d,l)-min(d,l))) % 4
            if d > l and (smer == 1 or smer == 3):
                x += (-(smer-2))*premik
            elif d < l and (smer == 1 or smer == 3):
                x += ((smer-2))*premik
            else:
                if smer == 0:
                    y += -premik
                if smer == 2:
                    y += premik
            pot += [(x,y)]
    return pot


def zapisi_pot(ukazi):
    pot = []
    gledam = smer = premik = 0
    for (x,y),(x1, y1) in zip(ukazi, ukazi[1:]):
        gledam = smer
        if x < x1:
            premik = x1-x
            smer = 1
            if gledam == 2:
                pot += 3*["DESNO"]
            else:
                pot += abs(gledam-smer)*["DESNO"]
            pot += [str(premik)]
        if x > x1:
            premik = abs(x1-x)
            smer = 3
            pot += abs(gledam - smer) * ["DESNO"]
            pot += [str(premik)]
        if y < y1:
            premik = y1-y
            smer = 2
            if gledam == 3:
                pot += 3 * ["DESNO"]
            else:
                pot += abs(gledam - smer) * ["DESNO"]
            pot += [str(premik)]
        if y > y1:
            premik = abs(y1-y)
            smer = 0
            if gledam == 0 or gledam == 2:
                pot += abs(gledam - smer) * ["DESNO"]
            elif gledam == 3:
                pot += ["DESNO"]
            else:
                pot += 3 * ["DESNO"]
            pot += [str(premik)]
    return '\n'.join(pot)


