'''
        opis prog.: kvazi minolovec
        avtor: Blaž Kumer
        Datum: 5. 12. 2017

'''






# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
from collections import Counter

def vsa_polja(s, v):

    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    return len(
        [(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if (i, j) in mine and (i, j) != (x, y)])

def najvec_sosedov(mine, s, v):
    return max([
                [(i[0],i[1]),sosedov(i[0],i[1],mine)] for i in vsa_polja(s,v)],
                key=lambda koordinate_sosedi:koordinate_sosedi[1])[0]

def brez_sosedov(mine,s,v):
    return set([(e[0],e[1]) for e in vsa_polja(s,v) if sosedov(e[0],e[1],mine)==0])

def po_sosedih(mine,s,v):
    return {i:set([(e[0],e[1]) for e in vsa_polja(s,v) if sosedov(e[0],e[1],mine)==i]) for i in range(9)}


########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([abs(pot[i][0]-pot[i+1][0])+abs(pot[i][1]-pot[i+1][1]) for i in range(len(pot)-1)])



def varen_premik(x0, y0, x1, y1, mine):
    return all([(i, j) not in mine for i in range(min(x0, x1), max(x0, x1) + 1) for j in range(min(y0, y1), max(y0, y1) + 1)])


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
    return all([(varen_premik(el[0][0],el[0][1],el[1][0],el[1][1],mine) if len(el)>1 else varen_premik(el[0][0],el[0][1],el[0][0],el[0][1],mine))
for el in (zip(pot, pot[1:]) if len(pot) > 1 else [(pot[0],pot[0])] if len(pot)==1 else [] )])

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
    min=set()
    s=polje.split(" ")
    for x in range(len(s) ):
        if s[x]=="":
            del s[x]
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j]=="X":
                min.add((j,i))
    return(min,j+1,i+1)


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
    pot=[]
    pot.append((0,0))
    x=y=0
    kot=0
    uk=ukazi.split()
    for u in uk:
        if u.isalpha():
            if u=="DESNO":
                kot+=1
                if kot==4:
                    kot=0
            else:
                kot-=1
                if kot==-1:
                    kot=3
        else:
            if kot==0:
                y-=int(u)
                pot.append((x,y))
            elif kot==1:
                x+=int(u)
                pot.append((x,y))
            elif kot==2:
                y+=int(u)
                pot.append((x,y))
            else:
                x-=int(u)
                pot.append((x,y))
    return pot




    """
    Za podani seznam ukazov (glej navodila naloge) vrni pot.

    Args:
        ukazi (str): ukazi, napisani po vrsticah

    Returns:
        list of tuple of int: pot
    """


def zapisi_pot(pot):
    s= zip(pot,pot[1:])
    kot=0
    ukazi=[]
    for sez in s:
        t1,t2 = sez
        if t1[0]==t2[0]:
            if t1[1]<t2[1]:
                while kot!=2:
                    kot+=1
                    ukazi.append("DESNO")
                    if kot==4:
                        kot=0
                ukazi.append(t2[1]-t1[1])
            if t1[1]>t2[1]:
                while kot!=0:
                    kot+=1
                    ukazi.append("DESNO")
                    if kot==4:
                        kot=0
                ukazi.append(t1[1]-t2[1])
        else:
            if t1[0] < t2[0]:
                while kot != 1:
                    kot += 1
                    ukazi.append("DESNO")
                    if kot == 4:
                        kot = 0
                ukazi.append(t2[0] - t1[0])
            if t1[0] > t2[0]:
                while kot != 3:
                    kot += 1
                    ukazi.append("DESNO")
                    if kot == 4:
                        kot = 0
                ukazi.append(t1[0] - t2[0])
    return '\n'.join(map(str, ukazi))
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """


