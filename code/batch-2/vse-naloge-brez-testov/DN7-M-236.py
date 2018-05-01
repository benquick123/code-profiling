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
    stmin = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if((i,j) in mine and (i,j) != (x,y)):
                stmin+=1
    return stmin


def najvec_sosedov(mine, s, v):
    max = 0
    kordinate = 0
    for i in range(s):
        for j in range(v):
          if(sosedov(i,j,mine)>=max):
              max = sosedov(i,j,mine)
              kordinate = (i,j)

    return kordinate




def brez_sosedov(mine, s, v):
    mnozica=set()
    for i in range(s):
        for j in range(v):
            if(sosedov(i,j,mine)==0):
                mnozica.add((i,j))
    return mnozica


def po_sosedih(mine, s, v):
    slovar = {}
    for i in range(9):
        slovar[i] =set()
    for i in range(s):
        for j in range(v):
            slovar[sosedov(i,j,mine)].add((i,j))
    return slovar

########################
# Za oceno 7

def dolzina_poti(pot):
    pot2=pot[1:]
    dolzina = 0
    for i in range(len(pot)-1):
        dolzina += abs(pot[i][0]-pot2[i][0]) + abs(pot[i][1]-pot2[i][1])
    return dolzina



def varen_premik(x0, y0, x1, y1, mine):
    if(x0==x1 and y0<=y1):
        for i in range(y0,y1+1):
            if((x0,i) in mine):
                return False
    if(x0==x1 and y0>=y1):
        for i in range(y1,y0+1):
            if((x0,i) in mine):
                return False
    if(y0==y1 and x0<=x1):
        for i in range(x0, x1+1):
            if ((i, y0) in mine):
                return False
    if(y0==y1 and x0>=x1):
        for i in range(x1, x0+1):
            if ((i, y0) in mine):
                return False

    return True




def varna_pot(pot, mine):
    if(len(pot)==1):
        if(not (varen_premik(pot[0][0], pot[0][1], pot[0][0], pot[0][1], mine))):
            return False

    for i in range(len(pot)-1):
        if(not(varen_premik(pot[i][0],pot[i][1],pot[i+1][0],pot[i+1][1],mine))):
            return False
    return True


########################
# Za oceno 8

def polje_v_mine(polje):
    koordinate=set()
    st_pik = 0
    st_presledkov = 0
    max_pik=0

    for i in polje:
        if(i =="."):
            st_pik+=1
        if (i =="X"):
            koordinate.add((st_pik,st_presledkov))
            st_pik+=1

        if (i ==" "):
            st_pik=0
            st_presledkov+=1
        if(st_pik>max_pik):
            max_pik=st_pik
    return(koordinate,max_pik,st_presledkov+1)




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


