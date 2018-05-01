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
    return sum(1 for a, b in mine if
               (a + 1, b + 1) == (x, y) or (a + 1, b - 1) == (x, y) or (a - 1, b + 1) == (x, y) or (a - 1, b - 1) == (
               x, y) or (a, b + 1) == (x, y) or (a, b - 1) == (x, y) or (a + 1, b) == (x, y) or (a - 1, b) == (x, y))

def najvec_sosedov(mine, s, v):
    return max(f for f in [(sosedov(x, y, mine), (x, y)) for x, y in vsa_polja(s, v)])[1]


def brez_sosedov(mine, s, v):
    return set((x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine)==0)

def po_sosedih(mine, s, v):
    return {i: {(x, y) for x, y in vsa_polja(s, v) if i == sosedov(x, y, mine)} for i in range(0, 9)}


########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([abs((pot[a][0] - abs(pot[a + 1][0]) + pot[a][1] - abs(pot[a + 1][1]))) for a in
                [i for i in range(len(pot) - 1)]])


def varen_premik(x0, y0, x1, y1, mine):
    return sum([a in mine for a in [(x, y) for x in range(min(x0, x1), max(x0, x1) + 1) for y in range(min(y0, y1), max(y0, y1) + 1)]]) == 0


def varna_pot(pot, mine):
    return sum([k in mine for k in pot]) + sum([not varen_premik(pot[i][0],pot[i][1],pot[i+1][0],pot[i+1][1],mine) for i in range(len(pot)-1)]) == 0

########################
# Za oceno 8

def polje_v_mine(polje):
    niz=polje.split(" ")
    niz=[str for str in niz if str]
    rez=set()
    for i in range(len(niz)):
        temp=niz[i]
        for j in range(len(temp)):
            if temp[j]=="X":
                rez.add((j,i))
    return rez,len(niz[0]),len(niz)



########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    vsiuk=ukazi.split("\n")
    smer=0
    x,y=0,0
    rez=[(0,0)]
    for uk in vsiuk:
        if uk=="DESNO":
            smer+=1
            if smer==4:
                smer=0
        elif uk=="LEVO":
            smer-=1
            if smer==-1:
                smer=3
        else:
            uk=int(uk)
            if smer==0:
                y=y-uk
            elif smer==1:
                x=x+uk
            elif smer==2:
                y=y+uk
            else:
                x=x-uk
            rez.append((x,y))
    return rez


def zapisi_pot(pot):
    rez = ''
    smer = 0
    smer1 = 0
    for i in range(len(pot) - 1):
        coor = pot[i]
        coor2 = pot[i + 1]

        if coor[0] < coor2[0]:
            smer1 = 1
            st1 = coor2[0] - coor[0]
        elif coor[0] > coor2[0]:
            smer1 = 3
            st1 = coor[0] - coor2[0]
        elif coor[1] < coor2[1]:
            smer1 = 2
            st1 = coor2[1] - coor[1]
        elif coor[1] > coor2[1]:
            smer1 = 0
            st1 = coor[1] - coor2[1]

        if smer < smer1:
            st = smer1 - smer
            rez = rez + st * "DESNO\n"
        elif smer > smer1:
            st = smer - smer1
            rez = rez + st * 3 * "DESNO\n"

        rez = rez + str(st1) + "\n"
        smer = smer1
    return rez[:-1]


