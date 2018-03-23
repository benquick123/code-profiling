from collections import defaultdict
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
    #print(x,y,mine)
    '''vsota=0
    for i in mine:
        #print(i)
        for x1 in i:
            #print("x1: ",x1)
            for y1 in i:
                if y1!=x1:
                    break
            #print(x1,y1)
            if (x1==x-1 and y1==y) or (x1==x+1 and y1==y) or (x1==x-1 and y1==y-1) or (x1==x and y1==y-1) or (x1==x+1 and y1==y-1) or (x1==x-1 and y1==y+1) or (x1==x and y1==y+1) or (x1==x+1 and y1==y+1):
                vsota+=1
            break
        #print("    ")
    #print(vsota)

    return vsota'''

def sosedov(x, y, mine):
    return (len(list([(x1,y1) for y1 in range(y-1,y+2) for x1 in range(x-1,x+2) if (x1,y1) in mine if (x1,y1)!=(x,y)])))

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
    return (tuple((x,y) for x,y in vsa_polja(s,v) if (max(sosedov(x, y, mine) for x,y in vsa_polja(s,v))) == sosedov(x, y, mine))[0])



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
    return ({(x, y) for x, y in vsa_polja(s, v) if (min(sosedov(x, y, mine) for x, y in vsa_polja(s, v))) == sosedov(x, y, mine)})


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
    '''slovar = {}
    for stev in range(9):
        if stev == 0:
            slovar[stev] = brez_sosedov(mine,s,v)
        else:
            slovar[stev] = {(x,y) for x,y in vsa_polja(s,v) if stev == sosedov(x, y, mine)}
    return (slovar)'''

def po_sosedih(mine, s, v):
    return ({stev:{(x,y) for x,y in vsa_polja(s,v) if stev==sosedov(x,y,mine)} for stev in range(9)})



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
    '''vsota=0
    for i,j in pot:
        #print(i,"    ",j)
        for k,l in pot:
            #print(i,k,j,l)
            vsota += abs(i-k)
            vsota += abs(j-l)
            i=k
            j=l
        break
    #print(vsota)
    return vsota'''

def dolzina_poti(pot):
    return (sum(abs(i-k)+abs(j-l) for (i,j),(k,l) in zip(pot, pot[1:])))

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
    if x0 < x1 or y0 < y1:
        while y0 <= y1:
            if (x0, y0) in mine:
                return False
            if x0 == x1:
                y0 += 1
            else:
                x0 += 1
        return True
    else:
        while y0 >= y1:
            if (x0, y0) in mine:
                return False
            if x0 == x1:
                y0 -= 1
            else:
                x0 -= 1
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
    if len(pot)==1:
        for index in pot:
            #print("   ",index)
            if index in mine:
                return False
            else:
                return True
    else:
        seznam = []
        for (x1, y1),(x2, y2) in zip(pot, pot[1:]):
            #print((x1, y1),(x2, y2))
            seznam.append(varen_premik(x1, y1, x2, y2, mine))
        #print(all(seznam))
        return all(seznam)


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
    nov={}
    nov1=[]
    for i,a in enumerate(polje.split()):
        for j,b in enumerate(a):
            if b=="X":
                nov1.append((j,i))
    nov = set((nov1))
    nov1 = (nov, len(a), len(polje.split()))
    return nov1

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


