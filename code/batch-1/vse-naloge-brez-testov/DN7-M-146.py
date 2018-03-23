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
    return sum(+1 for a in\
        [(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y-1),(x + 1, y + 1),(x - 1, y - 1),(x - 1, y + 1)]\
        if a in mine)



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
    return(tuple((x,y) for (x,y) in vsa_polja(s,v)\
        if (max(sosedov(x,y,mine) for x,y in vsa_polja(s,v))) == sosedov(x,y,mine))[0])

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

    #print({tuple((x, y) for (x, y) in vsa_polja(s, v) if (min(sosedov(x, y, mine) for x, y in vsa_polja(s, v))) == sosedov(x, y, mine))})
    return {(x, y) for (x, y) in vsa_polja(s, v) if (min(sosedov(x, y, mine) for x, y in vsa_polja(s, v))) == sosedov(x, y, mine)}



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
    return({a: {(x, y) for (x, y) in vsa_polja(s, v) if a == sosedov(x, y, mine)} for a in range(9)})


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

    vsota=0
    for i, o in pot:
        break


    for a, c in pot:
        vsota += abs(a-i) + abs(c-o)
        i=a
        o=c
   # print(vsota)
    return vsota

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

    for k in enumerate(mine):
        n = (x0,y0)
        if n not in mine:
            if x0 < x1:
                x0+=1
            elif x0>x1:
                x0-=1
            if y0 < y1:
                y0+=1
            elif y0 > y1:
                y0-=1
        else:
            return False
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
    n=[]
    if len(pot)<2:
        for a in pot:
            if a in mine:
                n.append(False)
    else:
        for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
            n.append(varen_premik(x0, y0, x1, y1, mine))
   #print(all(n))
    return all(n)






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
    x,y,j,k,b= 0,0,0,1,0
    neki = set()
    for a in polje:
        if a == ".":
            x+=1
        if a == "X":
            neki.add((x,y))
            x+=1
        if y!=b:
            k+=1
            b=y
        if a == " ":
            x=0
            y+=1
    for a in polje:
        if a == "." or a == "X":
            j+=1
        elif a == " ":
            break
    seznam=(neki,j,k)
    return seznam





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


