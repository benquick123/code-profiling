def sosedov(x, y, mine):
    a = x
    b = y
    x = x - 1
    y = y - 1
    i = 0
    ii = 0
    stevilo_min = 0
    while i < 3:
        while ii < 3:
            if not (x,y) == (a,b):
                if (x, y) in mine:
                    stevilo_min = stevilo_min + 1
            x = x + 1
            ii = ii + 1
        ii = 0
        x = a - 1
        i = i + 1
        y = y + 1
    return stevilo_min

def najvec_sosedov(mine, s, v):
    x = 0
    y = 0
    najstevilo = 0
    najvecpolje = (0,0)
    while x < s:
        while y < v:
            a = sosedov(x, y, mine)
            if a > najstevilo:
                najstevilo = a
                najvecpolje = (x, y)
            y = y + 1
        y = 0
        x = x + 1
    return najvecpolje

def brez_sosedov(mine, s, v):
    poljabrez = set()
    x = 0
    y = 0
    while x < s:
        while y < v:
            a = sosedov(x, y, mine)
            if a == 0:
                poljabrez.add((x, y))
            y = y + 1
        y = 0
        x = x + 1
    return poljabrez

def po_sosedih(mine, s, v):
    dic = {0:set(), 1:set(), 2:set(), 3:set(), 4:set(), 5:set(), 6:set(), 7:set(),8:set()}
    x = 0
    y = 0
    while x < s:
        while y < v:
            a = sosedov(x, y, mine)
            dic[a].add((x,y))
            y = y + 1
        y = 0
        x = x + 1
    return dic

def dolzina_poti(pot):
    dolzina = 0
    postaja = 1
    while postaja < len(pot):
        if pot[postaja][0] == pot[postaja - 1][0]:
            if pot[postaja][1] > pot[postaja - 1][1]:
                razlika = pot[postaja][1] - pot[postaja - 1][1]
            else:
                razlika = pot[postaja - 1][1] - pot[postaja][1]
            dolzina = dolzina + razlika
        else:
            if pot[postaja][0] > pot[postaja - 1][0]:
                razlika = pot[postaja][0] - pot[postaja - 1][0]
            else:
                razlika = pot[postaja - 1][0] - pot[postaja][0]
            dolzina = dolzina + razlika
        postaja = postaja + 1
    return dolzina

def varen_premik(x0, y0, x1, y1, mine):
    if x0 == x1:
        if y0 < y1:
            while y0 <= y1:
                if (x0, y0) in mine:
                    return False
                y0 = y0 + 1
        else:
            while y1 <= y0:
                if (x0, y1) in mine:
                    return False
                y1 = y1 + 1
    else:
        if x0 < x1:
            while x0 <= x1:
                if (x0,y0) in mine:
                    return False
                x0 = x0 + 1
        else:
            while x1 <= x0:
                if (x1,y0) in mine:
                    return False
                x1 = x1 + 1
    return True

def varna_pot(pot, mine):
    a = 1
    if len(pot) == 0:
        return True
    if len(pot) == 1:
        if pot[0] in mine:
            return False
        else:
            return True
    while a < len(pot):
        varnost = varen_premik(pot[a-1][0], pot[a-1][1], pot[a][0], pot[a][1], mine)
        a = a + 1
        if varnost == False:
            return False
    return True

def polje_v_mine(polje):
    a = set()
    x = 0
    y = 0
    polje = polje.split(" ")
    s = len(polje[0])
    v = len(polje)
    for vrstica in polje:
        for crka in vrstica:
            if crka == "X":
                a.add((x,y))
            x = x + 1
        x = 0
        y = y + 1
    return (a, s, v)
