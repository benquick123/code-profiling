from collections import *
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


def varna_pot(pot, mine):
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

def sosedov(x, y, mine):
    return len([(x1,y1) for x1,y1 in mine if abs(x-x1)<2 and abs(y-y1)<2 and (x1,y1)!=(x,y)])

def najvec_sosedov(mine, s, v):
    return max((v,k) for k,v in {(x,y):sosedov(x,y,mine) for x in range(s) for y in range(v)}.items())[1]

def brez_sosedov(mine, s, v):
    return set([(x,y) for y in range(0,v) for x in range(0,s) if sosedov(x,y,mine)==0])

def po_sosedih(mine, s, v):
    return {i:{(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine)==i} for i in range(0,9)}

def dolzina_poti(pot):
    return sum([abs(x[1]-x[0]) for x in zip([x[0] for x in pot], [x[0] for x in pot][1:])]) + sum([abs(x[1]-x[0]) for x in zip([x[1] for x in pot], [x[1] for x in pot][1:])])

def varen_premik(x0, y0, x1, y1, mine):
    return all([(x,y) not in mine for x in range(x0,x1+1) for y in range(y0,y1+1)]+[(x,y) not in mine for x in range(x0,x1-1,-1) for y in range(y0,y1-1,-1)])

def varna_pot(pot,mine):
    return all([varen_premik(pot[i:i+2][0][0],pot[i:i+2][0][1],pot[i:i+2][1][0],pot[i:i+2][1][1],mine)for i in range(len(pot)-1)]+ [(x,y) not in mine for x,y in pot])

def polje_v_mine(polje):
    t=[]
    i=0
    z=0
    for a in polje.split():
        z=0
        for e in a:
            if e=="X":
                t.append((z,i))
            z+=1
        i+=1
    return (set(t),z,i)

def preberi_pot(ukazi):
    pot=[]
    x=0
    y=0
    pot.append((x, y))
    smer=0
    for e in ukazi.split():
        if e=="DESNO":
            smer+=1
            continue
        if e=="LEVO":
            smer-=1
            continue
        if smer>3:
            smer-=4
        if smer<-3:
            smer+=4
        if smer==0:
            y-=int(e)
        if smer==1 or smer==-3:
            x+=int(e)
        if smer==2 or smer==-2:
            y+=int(e)
        if smer==3 or smer==-1:
            x-=int(e)
        pot.append((x,y))
    return pot

def zapisi_pot(ukazi):
    j = 0
    ukaz = ""
    prejsnjix = 0
    prejsnjiy = 0
    smer=0
    for x, y in ukazi:
        if y < prejsnjiy:
            smer=0
            obrni = smer - trenutna_smer
            if obrni < 0:
                obrni += 4
            ukaz += "DESNO " * obrni
            ukaz += str(abs(y - prejsnjiy)) + " "
        if x > prejsnjix:
            smer=1
            obrni=smer-trenutna_smer
            if obrni<0:
                obrni+=4
            ukaz += "DESNO "*obrni
            ukaz +=str(x-prejsnjix)+" "
        if y > prejsnjiy:
            smer=2
            obrni = smer - trenutna_smer
            ukaz += "DESNO " * obrni
            ukaz += str(y - prejsnjiy)+" "
        if x < prejsnjix:
            smer=3
            obrni = smer - trenutna_smer
            if obrni < 0:
                obrni += 4
            ukaz += "DESNO " * obrni
            ukaz += str(abs(x - prejsnjix)) + " "
        trenutna_smer = smer
        prejsnjix = x
        prejsnjiy = y
    return ukaz























