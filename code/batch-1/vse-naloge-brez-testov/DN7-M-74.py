def vsa_polja(s, v): return ((x, y) for x in range(s) for y in range(v))


def sosedov(x, y, mine): return len([1 for xi in range(x-1, x+2) for yi in range(y-1, y+2) if (xi, yi) in mine and (xi, yi) != (x, y)])


def najvec_sosedov(mine, s, v): return sorted([(sosedov(x, y, mine), x, y) for (x, y) in vsa_polja(s, v)], reverse=True)[0][1:]


def brez_sosedov(mine, s, v): return set([(x, y) for (x, y) in vsa_polja(s, v) if not sosedov(x, y, mine)])


def po_sosedih(mine, s, v): return {i: set([(x, y) for (x, y) in vsa_polja(s, v) if sosedov(x, y, mine) == i]) for i in range(9)}
    #diksnari = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}

    #for (x, y) in vsa_polja(s, v):
        #mineru = sosedov(x, y, mine)

        #diksnari[mineru].add((x, y))

    #return diksnari
    #return {str(sosedov(x, y, mine)): set(x, y) for x, y in vsa_polja(s, v)}


def dolzina_poti(pot): return sum([abs(x0-x1) + abs(y0-y1) for (x0, y0), (x1, y1) in zip(pot, pot[1:] or pot)])


def varen_premik(x0, y0, x1, y1, mine): return all(map(lambda x: x[2], [(x, y, (x, y) not in mine) for x in range(min(x0, x1), min(x0, x1)+abs(x1-x0)+1) for y in range(min(y0, y1), min(y0, y1)+abs(y1-y0)+1)]))


def varna_pot(pot, mine): return all([varen_premik(x0, y0, x1, y1, mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:] or pot)])


def polje_v_mine(polje):
    vrstice = polje.split(" ")

    s = len(vrstice[0])
    v = len(vrstice)

    mine = set()

    #[1 for y, vrednost_y in enumerate(vrstice) for x, vrednost_x in enumerate(vrednost_y) if
    for y, vrednost_y in enumerate(vrstice):
        for x, vrednost_x in enumerate(vrednost_y):
            if vrednost_x == "X":
                mine.add((x, y))

    return mine, s, v


########################
# Za oceno 9
#
# Vse funkcije za oceno 6 in 7 morajo biti napisane v eni vrstici.


########################
# Za oceno 10

def preberi_pot(ukazi):
    pot = [(0, 0)]
    orientacija = 0

    for vrstica in ukazi.split('\n'):
        if vrstica.isalpha():
            orientacija = (orientacija + (1 if vrstica == "DESNO" else -1)) % 4
        else:
            koordinate = pot[-1]

            if orientacija % 2:
                pot.append((koordinate[0] + (int(vrstica) * (1 if orientacija == 1 else - 1)), koordinate[1]))
            else:
                pot.append((koordinate[0], koordinate[1] + (int(vrstica) * (1 if orientacija else - 1))))

    return pot


def zapisi_pot(pot):
    ukazi = ""
    orientacija = 0
    nova_orientacija = 0

    for (x0, y0), (x1, y1) in zip(pot, pot[1:] or pot):
        dx = x1 - x0
        dy = y1 - y0

        if dx > 0:
            nova_orientacija = 1
        elif dx < 0:
            nova_orientacija = 3
        elif dy > 0:
            nova_orientacija = 2
        else:
            nova_orientacija = 0

        while orientacija != nova_orientacija:
            orientacija = (orientacija + 1) % 4
            ukazi += "DESNO\n"

        ukazi += (str(abs(dx + dy)) + '\n')

    return ukazi[:-1]


