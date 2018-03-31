
mine = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}

# def sosedov(x,y,mine):
#   stevilo_sosedov=0
#   for premik in [-1, 0, 1]:
#       for premik2 in [-1, 0, 1]:
#           if premik==0 and premik2==0:
#               continue
#           sosed=(x+premik, y+premik2)
#           if sosed in mine:
#               stevilo_sosedov+=1
#   return stevilo_sosedov

def sosedov(x,y,mine):
    return sum((x+premik1, y+premik2) in mine for premik1 in [-1, 0, 1] for premik2 in [-1, 0, 1] if not (premik1==0 and premik2==0))

#print(sosedov(3,0,mine))


# def najvec_sosedov(mine, s, v):
#   polje_najvec=0
#   naj_koordinate=()
#   for x in range(0, s):
#       for y in range(0, v):
#           stevilo_min=sosedov(x,y,mine)
#           if stevilo_min>polje_najvec:
#               polje_najvec=stevilo_min
#               naj_koordinate=(x,y)
#           else:
#               continue
#   return naj_koordinate

def najvec_sosedov(mine,s,v):
    return max(((x,y) for x in range(s) for y in range(v)), key=lambda terka: sosedov(terka[0],terka[1],mine))

# def najvec_sosedov(mine,s,v):
#   return((x,y) for x in range(0,s) for y in range(0,v) if max(sosedov(x,y,mine)))

#print(najvec_sosedov(mine,8,4))


def brez_sosedov(mine,s,v):
    return {(x,y) for x in range(s) for y in range(v) if sosedov(x,y,mine)==0}

#print(brez_sosedov(mine,8,4))

def po_sosedih(mine,s,v):
    # slovar={}
    # for n in range(0,9):
    #   slovar[n]=set((x,y) for x in range(0,s) for y in range(0,v) if sosedov(x,y,mine)==n)
    return {n:set((x,y) for x in range(s) for y in range(v) if sosedov(x,y,mine)==n) for n in range(9)}



# print(po_sosedih(mine,8,4)=={0: {(3, 0), (4, 2), (6, 1), (6, 3), (4, 3)},
#  1: {(7, 3), (3, 2), (0, 0), (7, 0), (3, 3), (7, 1),
#     (4, 0), (6, 0), (5, 0), (5, 3), (5, 1), (1, 0),
#     (4, 1), (0, 3)},
#  2: {(0, 1), (1, 2), (1, 3), (0, 2), (3, 1), (2, 0),
#     (6, 2), (2, 3), (2, 2), (5, 2), (1, 1), (7, 2)},
#  3: set(),
#  4: {(2, 1)},
#  5: set(),
#  6: set(),
#  7: set(),
#  8: set()})

pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]

# def dolzina_poti(pot):
#   stevilo_premikov=0
#   print(list(zip(pot, pot[1:])))
#   for (x1,y1),(x2,y2) in zip(pot, pot[1:]):
#       stevilo_premikov+=abs(y1-y2)+abs(x1-x2)
#   return stevilo_premikov

def dolzina_poti(pot):
    return sum(abs(y1-y2)+abs(x1-x2) for (x1,y1),(x2,y2) in zip(pot, pot[1:]))

#print(dolzina_poti(pot))


def varen_premik(x0,y0,x1,y1,mine):
    # obiskane_koordinate=[]
    # if x0 == x1:
    #   for i in range(y0, y1+1):
    #       obiskane_koordinate.append((x0, i) in mine)

    # else:
    #   for i in range(x0, x1+1):
    #       obiskane_koordinate.append((i, y0) in mine)
    # return any(obiskane_koordinate)

    return all([(x0, i) not in mine for i in range(min(y0, y1), max(y0, y1)+1)] if x0==x1 else [(i, y0) not in mine for i in range(min(x0, x1), max(x0, x1)+1)])

#print(varen_premik(6,1,6,3,mine))

def varna_pot(pot,mine):
    # seznam=[]
    # for (x0,y0),(x1,y1) in zip(pot, pot[1:]):
    #   seznam.append(varen_premik(x0,y0,x1,y1,mine))
    # return any(seznam)

    return pot[0] not in mine if len(pot)==1 else all([varen_premik(x0,y0,x1,y1,mine) for (x0,y0),(x1,y1) in zip(pot, pot[1:])])

#print(varna_pot(pot,mine))

def polje_v_mine(polje):
    zapis=list(enumerate(polje.strip().split(" ")))
    return ({(j,i) for i,e in zapis for j,f in enumerate(e) if f=='X'}, len(zapis[0][1]),len(zapis))

#print(polje_v_mine("...X.... .X....X. .XX..... ......X.")==({(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}, 8, 4))


def rotacija(terka,smer):
    return (-terka[1], terka[0]) if smer=='DESNO' else (terka[1], -terka[0])

import re
def preberi_pot(ukazi):
    zacetna_smer=(0,-1)
    lokacije=[(0,0)]
    for e in re.split('\s',ukazi):
        if e=='DESNO'or e=='LEVO':
            zacetna_smer=rotacija(zacetna_smer, e)
        elif e.isdigit():
            lokacije.append((lokacije[-1][0]+zacetna_smer[0]*int(e), lokacije[-1][1]+zacetna_smer[1]*int(e)))
    return lokacije

# print(preberi_pot('DESNO DESNO 3 LEVO 4 LEVO 1 DESNO 3 DESNO 1'))

def get_ukaz(terka0,terka1):
    count=0
    while terka0!=terka1:
        terka0=rotacija(terka0,'DESNO')
        count+=1
    return " ".join(["DESNO"]*count)


def zapisi_pot(pot):
    koraki=''
    smer=(0,-1)
    for (x0,y0),(x1,y1) in zip(pot, pot[1:]):
        premik=(x1-x0, y1-y0)
        smer_nova=(premik[0]/max(1,abs(premik[0])), premik[1]/max(1,abs(premik[1])))
        koraki+=get_ukaz(smer, smer_nova)
        smer=smer_nova
        koraki+=" "+str(abs(premik[1] if premik[0]==0 else premik[0]))+" "
    return koraki.strip()

# print(preberi_pot(zapisi_pot(pot)))