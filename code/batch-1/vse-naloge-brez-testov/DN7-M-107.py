# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))


########################
# Za oceno 6

def sosedov(x, y, mine):
    return sum([True for x_m, y_m in mine if (
    (y - 1 == y_m and (x - 1 == x_m or x == x_m or x + 1 == x_m)) or (y == y_m and (x - 1 == x_m or x + 1 == x_m)) or (y + 1 == y_m and (x - 1 == x_m or x == x_m or x + 1 == x_m)))])


def najvec_sosedov(mine, s, v):
    return ({sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)}.get(max({sosedov(x, y, mine): (x, y) for x, y in vsa_polja(s, v)})))


def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if (sosedov(x, y, mine) == 0)}


def po_sosedih(mine, s, v):
    return (({i: {(x, y) for (x, y) in [(x, y) for (x, y) in vsa_polja(s, v)] if (sosedov(x, y, mine) == i)} for i in range(0, 9)}))


########################
# Za oceno 7

def dolzina_poti(pot):
    return (sum([abs(x) for x in [x0 - x1 for (x0, y0), (x1, y1) in zip(pot, pot[1:])]]) + sum([abs(y) for y in [y0 - y1 for (x0, y0), (x1, y1) in zip(pot, pot[1:])]]))


def varen_premik(x0, y0, x1, y1, mine):
    return (all([(x, y) not in [(x, y) for (x, y) in [(x2, y2) for x2 in range(min(x0, x1), max(x0, x1) + 1) for y2 in range(min(y0, y1), max(y0, y1) + 1)]] for (x, y) in mine if (x, y)]))


def varna_pot(pot, mine):
    return (all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:]) if(x0, y0) not in [(x, y) for (x, y) in mine]] + [False for (x, y) in pot if(x, y) in [(x, y) for (x, y) in mine]]))


"...X.... .X....X. .XX..... ......X."


########################
# Za oceno 8

def polje_v_mine(polje):
    novo_polje = []
    i = 0
    polje = polje.split(" ")
    v = sum([1 for p in polje if (p != '')])
    for vrstica in polje:
        j = 0
        c = len(vrstica)
        for crka in vrstica:
            if crka == 'X':
                novo_polje.append((j, i))
            j = j + 1
        i = i + 1
    if (c == 0):
        c = c + 1
    return ({(x, y) for (x, y) in novo_polje}, c, v)


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    x = 0
    y = 0
    pos = 0
    pot = []
    pot.append((0, 0))
    ukazi = ukazi.split("\n")
    for ukaz in ukazi:
        if (str(ukaz) == 'DESNO' or str(ukaz) == 'LEVO'):
            if (str(ukaz) == 'DESNO'):
                pos = pos + 1
                if (pos >= 4):
                    pos = pos - 4
            else:
                pos = pos + 3
                if (pos >= 4):
                    pos = pos - 4
        else:
            if pos == 0:
                y = y - int(ukaz)
                pot.append((x, y))
            if pos == 1:
                x = x + int(ukaz)
                pot.append((x, y))
            if pos == 2:
                y = y + int(ukaz)
                pot.append((x, y))
            if pos == 3:
                x = x - int(ukaz)
                pot.append((x, y))
    return pot


def zapisi_pot(pot):
    pos = 0
    pos2 = 0
    nova_pot = []
    for (x0, y0), (x1, y1) in zip(pot, pot[1:]):
        if (x0 > x1):
            pos2 = 3
            premik = max(x0, x1) - min(x0, x1)
        if (x1 > x0):
            pos2 = 1
            premik = max(x0, x1) - min(x0, x1)
        if (y0 > y1):
            pos2 = 0
            premik = max(y0, y1) - min(y0, y1)
        if (y1 > y0):
            pos2 = 2
            premik = max(y0, y1) - min(y0, y1)
        if(pos<pos2):
            while(pos<pos2):
                nova_pot.append("DESNO")
                pos=pos+1
                if(pos==pos2):
                    break
        if (pos > pos2):
            temp=pos
            pos=pos2
            pos2=temp
            while (pos<=pos2):
                nova_pot.append("LEVO")
                pos2 = pos2 - 1
                if (pos == pos2):
                    break

        if(pos==pos2):
            nova_pot.append(str(premik))
    return("\n".join(nova_pot))




