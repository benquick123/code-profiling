# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))



########################
# Za oceno 6

def sosedov(x, y, mine):
    #return sum(tx for tx,ty in mine if all(tx in range(x-1,x+2), ty in range(y-1,y+2), not ty==y, not tx==x))
    c=0
    for tx,ty in mine:
        if tx in range(x-1,x+2) and ty in range(y-1,y+2):
            if ty==y and tx==x:
                pass
            else:
                c+=1
    return c

def najvec_sosedov(mine, s, v):
    maks=(0,(0,0))
    for x,y in vsa_polja(s,v):
        if maks[0]<sosedov(x,y,mine):
            maks=((sosedov(x,y,mine)),(x,y))
    return maks[1]    

def brez_sosedov(mine, s, v):
    brez_min=set()
    for x,y in vsa_polja(s,v):
        if sosedov(x,y,mine)==0:
            brez_min.add((x,y))
    return brez_min


def po_sosedih(mine, s, v):
    dic={}
    for i in range(9):
        dic[i]=set()
    for x,y in vsa_polja(s,v):
        key=sosedov(x,y,mine)
        if key not in dic:
            dic[key]=set()
        dic[key].add((x,y))
    return dic

    


########################
# Za oceno 7
mine = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}

def dolzina_poti(pot):
    prejsni=(0,0)
    c=0
    it=0
    for korak in pot:
        if not it ==0:
            if not korak[0]==prejsni[0]:
                c+=abs(korak[0]-prejsni[0])
            if not korak[1]==prejsni[1]:
                c+=abs(korak[1]-prejsni[1])
        prejsni = korak
        it+=1
    return c
pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]
#print(dolzina_poti(pot))

def vmesni_koraki(x0, y0, x1, y1):#vmesni koraki skupaj z koncem in zacetkom
    t=set()
    if x0==x1:
        while y0 < y1:
            t.add((x0,y0))
            y0+=1
        while y0 >= y1:
            t.add((x0,y0))
            y0-=1
    else:
        while x0 < x1:
            t.add((x0,y0))
            x0+=1
        while x0 >= x1:
            t.add((x0,y0))
            x0-=1
    return t

def varen_premik(x0, y0, x1, y1, mine):
    for p in vmesni_koraki(x0,y0,x1,y1):
        if p in mine:
            return False
    return True

mine = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}
pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]

#print(pot[:-1:])
#print(pot[1::])


def varna_pot(pot, mine):
    #for (x0, y0), (x1, y1) in zip(pot, pot[1:])
    t= pot[:-1:]
    t2= pot[1::]
    if len(pot)==1:
        if pot[0] in mine:
            return False
    for i in range(0,len(t)):
        if not varen_premik(t[i][0],t[i][1],t2[i][0],t2[i][1],mine):
            return False
    return True


########################
# Za oceno 8

def polje_v_mine(polje):
    mine=set()
    v=0
    for vrstica in polje.split():
        s=0
        for t in vrstica:
            if t == "X":
                mine.add((s,v))
            s+=1
        v+=1
    t=(mine,s,v)
    return t


'''
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

'''
