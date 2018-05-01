

#Napiši funkcijo najvec_sosedov(mine, s, v), ki vrne koordinati polja, ki je obkroženo z največ minami. Pri tem sta s in v širini in višina polja. Za gornji primer bi klic najvec_sosedov(mine, 8, 4) vrnil polje (2, 1).

#Napiši funkcijo brez_sosedov(mine, s, v), ki vrne množico vseh polj, ki nimajo na sosednjih poljih nobene mine. (Dovoljeno pa je, da mina stoji prav na tem polju). V gornjem primeru klic brez_sosedov(mine, 8, 4) vrne {(3, 0), (4, 2), (6, 1), (6, 3), (4, 3)}

#Napiši funkcijo po_sosedih(mine, s, v), ki vrne slovar, katerega ključi so števila od 0 do 8, pripadajoče vrednosti pa so množice koordinat polj, ki vsebujejo toliko min. V gornjem primeru bi klic po_sosedih(mine, 8, 4) vrnil slovar

# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):

    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6
# Napiši funkcijo sosedov(x, y, mine), ki pove, na koliko sosedov polja s koordinatami (x, y) je postavljena mina.
#  Klic sosedov(2, 1, mine) v gornjem primeru vrne 4, saj je polje obkroženo s štirimi minami.
#  Klic sosedov(3, 0) vrne 0,
# saj nobeno od sosednjih polj nima mine; mina je seveda prav na polju (3, 0),
#  vendar ta ne šteje.

def preveri_mino(x, y, mine):

    for x_koordinata,y_koordinata in mine:
        if x_koordinata==x  and y_koordinata==y:
            return True #true
    return False

def max_velikost(mine):
    max_x=0
    max_y=0
    for x, y in mine:
        if x > max_x:
            max_x=x


        if y > max_y:
            max_y=y

    return (max_x,max_y)


def sosedov(x, y, mine):


    mina_1=preveri_mino(x-1,y-1,mine)
    mina_2=preveri_mino(x+0,y-1,mine)
    mina_3=preveri_mino(x+1,y-1,mine)
    mina_4=preveri_mino(x+1,y+0,mine)
    mina_5=preveri_mino(x+1,y+1,mine)
    mina_6=preveri_mino(x+0,y+1,mine)
    mina_7=preveri_mino(x-1,y+1,mine)
    mina_8=preveri_mino(x-1,y+0,mine)

    seznam_min=[mina_1,mina_2,mina_3, mina_4, mina_5, mina_6, mina_7, mina_8]
    return  sum(seznam_min)



def najvec_sosedov(mine, s, v):
    št_sosednih_min=[]
    for x, y in vsa_polja(s,v):
        sosednje_mine= sosedov(x,y,mine)
        št_sosednih_min.append((x,y, sosednje_mine))
    največja_terka_max=max(št_sosednih_min, key=lambda mina:mina[2])

    return (največja_terka_max[0],največja_terka_max[1])


def brez_sosedov(mine, s, v):
    ni_sosedov=[]
    for x, y in vsa_polja(s, v):
       # sosednje_mine=sosedov (x,y,mine)
        if sosedov(x,y,mine)==0:
            mesta_kjer_ni_sosedov=(x,y)
            ni_sosedov.append(mesta_kjer_ni_sosedov)
    return set(ni_sosedov)

 #Napiši funkcijo po_sosedih(mine, s, v),
# ki vrne slovar, katerega ključi so števila od 0 do 8, pripadajoče vrednosti pa so množice
def po_sosedih (mine, s,v ):
    slovar= {}
    for i in range(0,9):
        seznam_koordinat=[]
        for x,y in vsa_polja(s,v):
            if sosedov(x,y,mine)==i:
                seznam_koordinat.append((x,y))
        slovar[i]=set(seznam_koordinat)
    return slovar


#NALOGA za 7

def dolzina_poti(pot):

    # dolžina=0
    # vsota=0
    # for i in range(0,len(pot)-1):
    #
    #     x1=pot[i][0]
    #     y1=pot[i][1]
    #     x2=pot[i+1][0]
    #     y2=pot[i+1][1]
    #
    #     dolžina=abs(y2-y1)+abs(x2-x1)
    #
    #     vsota+=dolžina
    #
    # return vsota

    return sum([abs(pot[i][0] - pot[i + 1][0]) + abs(pot[i][1] - pot[i + 1][1]) for i in range(len(pot) - 1)])

def varen_premik(x0,y0,x1,y1, mine):
    for x in range(min(x0,x1), max(x0, x1)+1): #za vodoravno
        if preveri_mino(x,y0,mine):
            return False


    for y in range(min(y0,y1),max(y0,y1)+1): #za navpično
        if preveri_mino(x0,y, mine):
            return False

    return True

def varna_pot(pot, mine):
    if len(pot)==1 and preveri_mino(pot[0][0],pot[0][1],mine):
        return False




    for i in range(0, len(pot) - 1):#ker zanji nima več para/ ne obstaja več  je -1!!!!"!!!!

        x1 = pot[i][0]
        y1 = pot[i][1]
        x2 = pot[i + 1][0]
        y2 = pot[i + 1][1]

        if varen_premik(x1,y1,x2,y2, mine)==False: #pot ni varna

            return False
    return True



#naloga 8
def polje_v_mine(polje):

    razdeljeni_znaki_po_vrsticah=polje.strip().split(" ")
    visina=len(razdeljeni_znaki_po_vrsticah)
    dolžina=len(razdeljeni_znaki_po_vrsticah[0])

    novi_seznam=[]
    for y in range(0, visina):
        for x in range(0, dolžina):
            if razdeljeni_znaki_po_vrsticah[y][x] =="X":
                novi_seznam.append((x,y))
    return (set(novi_seznam),dolžina, visina)





