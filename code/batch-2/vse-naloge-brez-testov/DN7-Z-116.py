def vsa_polja(s, v):
    return ((x, y) for x in range(s) for y in range(v))


# ZA 6
def sosedov(x, y, mine):
    return len({(x1, y1) for x1 in range(x - 1, x + 2) for y1 in \
                range(y - 1, y + 2) if (x1, y1) in mine and (x, y) != (x1, y1)})


def najvec_sosedov(mine, s, v):
    return tuple((x, y) for x, y in vsa_polja(s, v) if max([sosedov(x, y, mine) \
                                                            for x, y in vsa_polja(s, v)]) == sosedov(x, y, mine))[0]


def brez_sosedov(mine, s, v):
    return {(x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == 0}


def po_sosedih(mine, s, v):
    return {i: set((x, y) for x, y in vsa_polja(s, v) if sosedov(x, y, mine) == i) for i in range(9)}


# Za 7
def dolzina_poti(pot):
    return sum([abs(dolzina(pot)[n] - dolzina(pot)[n - 1]) for n in range(len(dolzina(pot)))][1:])


def varen_premik(x0, y0, x1, y1, mine):
    return not True in [(x, y) in mine for x in range(min(x0, x1), max(x0, x1) + 1) \
                        for y in range(min(y0, y1), max(y0, y1) + 1)]


def varna_pot(pot, mine):
    return (not True in [(x, y) in mine for x, y in pot]) \
           and (not False in [varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])


def dolzina(pot):
    return [koordinate[0] + koordinate[1] for koordinate in pot]


# Za 8
def polje_v_mine(polje):
    x, y, visina, sirina = 0, 0, 1, 0
    mine = set()
    for znak in polje:
        if znak == ".":
            x += 1;
            sirina += 1
        if znak == " ":
            x = 0;
            y += 1;
            visina += 1
        if znak == "X":
            sirina += 1;
            mine.add((x, y));
            x += 1
    return mine, int(sirina / visina), visina


# Za 10
def preberi_pot(ukazi):
    polja = [(0, 0)]
    smeri = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    smer = 0
    for ukaz in ukazi:
        if ukaz == "DESNO":
            smer = (smer + 1) % 4
        elif ukaz == "LEVO":
            smer = (smer + 3) % 4
        else:
            premik = int(ukaz)
            x, y = polja[-1]
            dx, dy = smeri[smer]
            polja.append((x + dx * premik, y + dy * premik))
    return polja


def zapisi_pot(polja):
    ukazi = []
    x, y = 0, 0
    smer = 0
    for px, py in polja[1:]:
        dx, dy = px - x, py - y
        star_smer = smer
        if dx > 0:  # desno
            smer = 1
        elif dx < 0:  # levo
            smer = 3
        elif dy > 0:  # dol
            smer = 2
        elif dy < 0:  # gor
            smer = 0
        sprememba_smeri = (smer - star_smer + 4) % 4
        for i in range(sprememba_smeri):
            ukazi.append("DESNO")
        ukazi.append(max(abs(dx), abs(dy)))
        x, y = px, py
    return ukazi
