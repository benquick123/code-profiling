# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
import collections

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
    return sum([1 for a,b in mine if a in(x-1,x,x+1) and b in (y-1,y,y+1) and (a,b)!=(x,y)])


def najvec_sosedov(mine, s, v):
    return  [(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine)==max([sosedov(x,y,mine)for x,y in vsa_polja(s,v)])][0]

def brez_sosedov(mine, s, v):
    return {(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine)==0 }


def po_sosedih(mine, s, v):
    return {st:{(x,y) for x,y in vsa_polja(s,v) if sosedov(x,y,mine)==st} for st in range(9)}



########################
# Za oceno 7

def dolzina_poti(pot):
    return sum([abs(a-x)+abs(b-y) for (x,y),(a,b) in zip(pot,pot[1:])])


print(int((5-10)/abs(5-10)))

def varen_premik(x0, y0, x1, y1, mine):
    if abs(x0-x1)!=0:
        if x1>x0:
            for a in range(x0,x1+1):
                if (a,y0)in mine:
                    return False
        else:
            for a in range(x1,x0+1):
                if (a,y0)in mine:
                    return False
    else:
        if y1>y0:
            for a in range(y0,y1+1):
                if (x0,a)in mine:
                    return False
        else:
            for a in range(y1,y0+1):
                if (x0,a)in mine:
                    return False
    return True



def varna_pot(pot, mine):
    d = []
    if len(pot) == 1:
        return not (pot[0] in mine)
    else:
        for (a, b), (x, y) in zip(pot, pot[1:]):
            d.append(varen_premik(a, b, x, y, mine))
        return all(d)


########################
# Za oceno 8

def polje_v_mine(polje):
    a=set()
    sez=polje.split()
    dol=len(sez)
    desno=len(sez[0])
    for x in range(dol):
        for y in range(desno):
            b=sez[x]
            if b[y]=="X":
                a.add((y,x))
    return (a,desno,dol)




########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10
def smer_igralca(x,smer):
    if x == "DESNO":
        if smer != 3:
            smer += 1
        else:
            smer -= 3
    else:
        if x == "LEVO":
            if smer!=0:
                smer -= 1
            else:
                smer +=3
    return smer

def premik(smer,st,poz):
    x,y=poz
    st=int(st)
    if smer==0:
        return (x,y-st)
    if smer==1:
        return (x+st,y)
    if smer==2:
        return (x,y+st)
    if smer==3:
        return (x-st,y)

def preberi_pot(ukazi):
    a=ukazi.split()
    smer=0
    premiki=[(0,0)]
    poz=(0,0)
    for x in a:
        if x=="DESNO" or x=="LEVO":
            smer=smer_igralca(x,smer)
        else:
            poz=premik(smer,x,poz)
            premiki.append(poz)
    return premiki


def premik_gor(smer, a,b,x,y):
    ukazi=""
    if smer!=0:
        premik=abs(y-b)
        ukazi+=premik+"/n"

def zapisi_pot(pot):
    """
    Za podano pot vrni seznam ukazov (glej navodila naloge).

    Args:
        pot (list of tuple of int): pot

    Returns:
        str: ukazi, napisani po vrsticah
    """



