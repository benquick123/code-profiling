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
from math import *


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
    sosedi=0
    for x1,y1 in mine:
        razdalja=sqrt( (x - x1)**2 + (y - y1)**2 )
        if razdalja<=sqrt(2) and razdalja!=0:
            sosedi=sosedi+1
    return sosedi
#print(sosedov(3,0,{(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}))


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
    d={}
    x=0
    y=0

    while x<s:
        y=0
        while y<v:
            d[x,y]=sosedov(x,y,mine)
            y=y+1
        x=x+1
    return (max(d, key=d.get))


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
    d={}
    x=0
    y=0
    while x<s:
        y=0
        while y<v:
            d[x,y]=sosedov(x,y,mine)
            y=y+1
        x=x+1
    return {k for (k,v) in d.items() if v == 0}

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
    c=0
    filtriraj={}
    d={}
    x=0
    y=0
    while x<s:
        y=0
        while y<v:
            filtriraj[x,y]=sosedov(x,y,mine)
            y=y+1
        x=x+1
    while c<=8:
        d[c]= {k for (k,v) in filtriraj.items() if v == c}
        c=c+1
    return d


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
    d={}
    c=0
    while c<len(pot):
        x1,y1=list(pot[c])
        if c+1>=len(pot):
            break;
        x2,y2=list(pot[c+1])
        if x1<x2:
            while x1<x2:
                x1=x1+1 #mogoce prestaviti dol in na koncu od dolzine odsteti 1
                d[x1,y1]=1
        if y1<y2:
            while y1<y2:
                y1=y1+1
                d[x1,y1]=1
        if x1>x2:
            while x1>x2:
                x1=x1-1 #mogoce prestaviti dol in na koncu od dolzine odsteti 1
                d[x1,y1]=1
        if y1>y2:
            while y1>y2:
                y1=y1-1
                d[x1,y1]=1
        c=c+1
    return sum(d.values())



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

    b=True
    if(x0,y0)in mine or (x1,y1) in mine:
        return False
    if x0<x1:
        while x0<x1:
            if (x0,y0) in mine:
                b= False
            x0=x0+1
    if x0>x1:
        while x0>x1:
            if (x0,y0) in mine:
                b= False
            x0=x0-1
    if y0<y1:
        while y0<y1:
            if (x0,y0) in mine:
                b= False
            y0=y0+1
    if y0>y1:
        while y0>y1:
            if (x0,y0) in mine:
                b= False
            y0=y0-1
    return b




def varna_pot(pot, mine):
    """
    Vrni `True`, če je podana pot varna, `False`, če ni.

    Args:
        pot (list of tuple of int): koordinate točk na poti (brez vmesnih točk)
        mine (set of tuple of int): koordinate min

    Returns:
        bool: `True`, če je pot varna, `False`, če ni.
    """
    b=True
    d={}
    c=0
    while c<len(pot):
        x1,y1=pot[c]
        if c+1>=len(pot):
            if (x1,y1) in mine:
                b=False
            break;
        x2,y2=pot[c+1]
        if x1<x2:
            while x1<x2:
                x1=x1+1 #mogoce prestaviti dol in na koncu od dolzine odsteti 1
                d[x1,y1]=1
        if y1<y2:
            while y1<y2:
                y1=y1+1
                d[x1,y1]=1
        if x1>x2:
            while x1>x2:
                x1=x1-1 #mogoce prestaviti dol in na koncu od dolzine odsteti 1
                d[x1,y1]=1
        if y1>y2:
            while y1>y2:
                y1=y1-1
                d[x1,y1]=1
        c=c+1
        for k in d.keys():
            if k in mine:
                b= False
                break
    return b


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
#za samo eno vrstico:
    x=0
    y=0
    c=0
    s=set()
    if " " not in polje:
        sirina=len(polje)
        visina=1
        #s.add(sirina)
        #s.add(visina)
        while x<sirina:
            if polje[x]=="X":
                s.add((x,y))
            x=x+1
        return s,sirina,visina
    if " " in polje:
        sirina=polje.index(" ")
        visina=polje.count(" ")+1
        if polje[len(polje)-1]==" ":
            visina=visina-1
        #s.add(sirina)
        #s.add(visina)
        while y<visina:
            while x<sirina:
                if c==len(polje):
                    break
                if polje[c]=="X":
                    s.add((x,y))
                x=x+1
                c=c+1
            x=0
            c=c+1
            y=y+1
    return s,sirina,visina



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


