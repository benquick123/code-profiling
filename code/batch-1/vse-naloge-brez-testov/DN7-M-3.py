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
    return sum([1 for x1, y1 in vsa_polja(3, 3) if((x-(x1-1),y-(y1-1)) in mine and (x-(x1-1),y-(y1-1)) != (x,y))])



def najvec_sosedov(mine, s, v):
    return [(x1,y1) for x1,y1 in vsa_polja(s,v) if(max([sosedov(x,y,mine) for x,y in vsa_polja(s,v)]) == sosedov(x1,y1,mine))][0]



def brez_sosedov(mine, s, v):
    return {(x,y) for x, y in vsa_polja(s, v) if sosedov(x,y,mine) == 0}


def po_sosedih(mine, s, v):
    return ({ key:set({(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine) == key}) for key in range(0,9)})



########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([abs((pot[i][0] - pot[i - 1][0]) + (pot[i][1] - pot[i - 1][1])) for i in range(1, len(pot))])



def varen_premik(x0, y0, x1, y1, mine):
    return (all([False for (x,y) in[(x,y) for x in range(min(x1,x0),max(x1,x0)+1) for y in range(min(y1,y0),max(y1,y0)+1)] if (x,y) in mine]))


def varna_pot(pot, mine):
    return all([False for i in range(1,len(pot)) if (not varen_premik(pot[i-1][0],pot[i-1][1],pot[i][0],pot[i][1],mine))]+[False for x,y in pot if (not varen_premik(x,y,x,y,mine))])



########################
# Za oceno 8

def polje_v_mine(polje):
    k = set()
    polje = polje.strip()
    polje = polje.split(" ")
    v = len(polje)
    s = len(polje[0])
    for x in range(v):
        for y in range(s):
            if polje[x][y] == "X":
                k.add((y,x))
    return (k,s,v)



########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    obr = 0
    x = 0
    y = 0
    r = [(x,y)]
    ukazi = ukazi.split('\n')
    for i in ukazi:
        if i == "LEVO":
            if obr == 0:
                obr = 270
            else:
                obr -= 90
        elif i == "DESNO":
            if obr == 270:
                obr = 0
            else:
                obr += 90
        elif i.isnumeric():
            i = int(i)
            if obr == 0:
                y += i
                r.append((abs(x), abs(y)))
            if obr == 90:
                x += i
                r.append((abs(x), abs(y)))
            if obr == 180:
                y -= i
                r.append((abs(x), abs(y)))
            if obr == 270:
                x -= i
                r.append((abs(x),abs(y)))
    return r

def zapisi_pot(pot):
    uk = ""
    pre = 0
    for i in range(1, len(pot)):
        x = pot[i - 1][0]
        y = pot[i - 1][1]
        x1 = pot[i][0]
        y1 = pot[i][1]
        if (y < y1):
            uk += str(y1-y)
            uk += "\n"
        if (y > y1):
            uk += "LEVO\nLEVO\n"
            uk += str(y - y1)
            uk += "\n"
            uk += "LEVO\nLEVO\n"
        if (x < x1):
            uk += "DESNO\n"
            uk += str(x1 - x)
            uk += "\n"
            uk += "DESNO\nDESNO\nDESNO\n"
        if (x > x1):
            uk += "LEVO\n"
            uk += str(x - x1)
            uk += "\n"
            uk += "LEVO\nLEVO\nLEVO\n"
    return uk




