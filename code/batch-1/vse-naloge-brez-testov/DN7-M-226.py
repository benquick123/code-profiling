import math

#mine = {(3, 0), (1, 1), (6, 1), (1, 2), (2, 2), (6, 3)}


def sosedov(x, y, mine):
    cifra_min = 0
    sez = []
    for x1, y1 in mine:

        if (x == x1) & ((y - 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))


        elif ((x + 1) == x1) & ((y - 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x - 1) == x1) & ((y - 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x + 1) == x1) & (y == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x + 1) == x1) & ((y + 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x) == x1) & ((y + 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x - 1) == x1) & ((y + 1) == y1):
            cifra_min += 1
            sez.append((x1, y1))

        elif ((x - 1) == x1) & (y == y1):
            cifra_min += 1
            sez.append((x1, y1))

    return cifra_min


# print(sosedov(2, 1, mine))

def setup_board(s, v):
    coordinates = []
    for x in range(0, s):
        for y in range(0, v):
            coordinates.append((x, y))
    return coordinates


def najvec_sosedov(mine, s, v):
    ogX, ogY = 0, 0
    max_sosedov = 0
    for x, y in setup_board(s, v):
        if sosedov(x, y, mine) > max_sosedov:
            max_sosedov = sosedov(x, y, mine)
            ogX, ogY = x, y

    return (ogX, ogY)


# print(najvec_sosedov(mine, 7, 4))

def brez_sosedov(mine, s, v):
    brez = []
    for x, y in setup_board(s, v):
        if sosedov(x, y, mine) == 0:
            brez.append((x, y))
    return set(brez)


# print(brez_sosedov(mine, 7, 4))

def po_sosedih(mine, s, v):
    # setup slovarja s praznimi seti do kljuca stevila 8
    slovar = {}
    for i in range(0, 9):
        slovar[i] = set()

    for x, y in setup_board(s, v):
        slovar[sosedov(x, y, mine)].add((x, y))
    return slovar


# print(po_sosedih(mine, 8, 4))

pot = [(0, 0), (0, 3), (4, 3), (4, 2), (7, 2), (7, 3)]


def dolzina_poti(pot):
    dolzina, i = 0, 0
    while i < len(pot) - 1:
        x, y = pot[i]
        x1, y1 = pot[i + 1]
        this_dolzina = math.sqrt((x1 - x) ** 2) + math.sqrt((y1 - y) ** 2)
        dolzina += this_dolzina
        i += 1
    return int(dolzina)


# print(dolzina_poti(pot))

def is_mine(x, y, mine):
    if (x, y) in mine:
        return True
    else:
        return False


def get_premiki(x0, y0, x1, y1):
    premiki = []
    if (x0 < x1) & (y0 < y1):  # 0,0 -> 1,5
        while x0 < x1:
            x0 += 1
            premiki.append((x0, y0))
            # if is_mine(x0, y0, mine): return False
        while y0 < y1:
            y0 += 1
            premiki.append((x0, y0))
        return premiki

    if (x0 < x1) & (y0 > y1):  # 0,6 -> 3,4
        while x0 < x1:
            x0 += 1
            premiki.append((x0, y0))
        while y0 > y1:
            y0 -= 1
            premiki.append((x0, y0))
        return premiki

    if (x0 > x1) & (y0 < y1):  # 5,0 -> 3,4
        while x0 > x1:
            x0 -= 1
            premiki.append((x0, y0))
        while y0 < y1:
            y0 += 1
            premiki.append((x0, y0))
        return premiki

    if (x0 > x1) & (y0 > y1):  # 6,6 -> 1,1
        while x0 > x1:
            x0 -= 1
            premiki.append((x0, y0))
        while y0 > y1:
            y0 -= 1
            premiki.append((x0, y0))
        return premiki

    if (x0 > x1) & (y0 == y1):
        while x0 > x1:
            x0 -= 1
            premiki.append((x0, y0))
        return premiki

    if (x0 < x1) & (y0 == y1):
        while x0 < x1:
            x0 += 1
            premiki.append((x0, y0))
        return premiki
    if (x0 == x1) & (y0 > y1):
        while y0 > y1:
            y0 -= 1
            premiki.append((x0, y0))
        return premiki
    if (x0 == x1) & (y0 < y1):
        while y0 < y1:
            y0 += 1
            premiki.append((x0, y0))
        return premiki


# print(get_premiki(3,6,1,6))

def varen_premik(x0, y0, x1, y1, mine):
    if len(mine) == 0:
        return True
    if is_mine(x0, y0, mine):
        return False
    for (x, y) in get_premiki(x0, y0, x1, y1):
        if is_mine(x, y, mine):
            return False
    return True


# print(varen_premik(0,3,3,3,mine))

def varna_pot(pot, mine):
  i = 0
  if len(pot) == 1:
    (x,y) = pot[0]
    if is_mine(x,y,mine):
      return False
  while i < len(pot)-1 & len(pot)>1:
    x0,y0 = pot[i]
    if (i == 0) & (is_mine(x0,y0,mine)):
        return False
    x1, y1 = pot[i+1]
    i+=1
    if varen_premik(x0, y0, x1, y1, mine):
      pass
    else:
      return False
  return True


# print(varna_pot(pot, mine))

#polje = "...X.... .X....X. .XX..... ......X."


def polje_v_mine(polje):
    vrste = []
    found_mines = []
    x, y = 0, 0

    for vrstica in polje.split():
        vrste.append(vrstica)

        for znak in vrstica:
            s = len(vrstica)
            if znak == "X":
                found_mines.append((x, y))
            x = x + 1
        y = y + 1
        x = 0
    v = len(vrste)
    return set(found_mines), s, v

# print(polje_v_mino(polje))



