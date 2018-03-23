# To funkcijo prijazno podarjam vsem, ki bodo programirali v eni vrstici. :)
# Kako jo uporabiti, je v navodilih. Kdor je ne potrebuje, naj jo ignorira.
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

# TESTS_OK

########################
# Za oceno 6

def sosedov(x, y, mine):
	n = 0
	for xx in range(x-1, x+2):
		for yy in range(y-1, y+2):
			if (xx, yy) in mine and (xx, yy) != (x, y):
				n += 1
	return n


def najvec_sosedov(mine, s, v):
	m = 0
	nn = (0, 0)
	for (x, y) in vsa_polja(s, v):
		n = sosedov(x, y, mine)
		if n > m:
			m = n
			nn = (x, y)
	return nn


def brez_sosedov(mine, s, v):
	m = set()
	for (x, y) in vsa_polja(s, v):
		if sosedov(x, y, mine) == 0:
			m.add((x, y))
	return m


def po_sosedih(mine, s, v):
	m = {}
	for i in range(9):
		m[i] = set()
	for (x, y) in vsa_polja(s, v):
		n = sosedov(x, y, mine)
		m[n].add((x, y))
	return m


########################
# Za oceno 7

def dolzina_poti(pot):
	n = 0
	for i in range(len(pot)-1):
		if pot[i][0] != pot[i+1][0]:
			n += abs(pot[i][0] - pot[i+1][0])
		elif pot[i][1] != pot[i+1][1]:
			n += abs(pot[i][1] - pot[i+1][1])
	return n


def varen_premik(x0, y0, x1, y1, mine):
	if x0 == x1:
		if y0 > y1:
			a = y0
			y0 = y1
			y1 = a
		for y in range(y0, y1+1):
			if (x0, y) in mine:
				return False
	if y0 == y1:
		if x0 > x1:
			a = x0
			x0 = x1
			x1 = a
		for x in range(x0, x1+1):
			if (x, y0) in mine:
				return False
	return True


def varna_pot(pot, mine):
	if len(pot) == 1 and pot[0] in mine:
		return False
	for i in range(len(pot)-1):
		if not varen_premik(pot[i][0], pot[i][1], pot[i+1][0], pot[i+1][1], mine):
			return False
	return True


########################
# Za oceno 8

def polje_v_mine(polje):
	m = set()
	s = 0
	v = 1
	for i in range(len(polje)):
		if polje[i] != " ":
			if v == 1:
				s += 1
			if polje[i] == "X":
				if v == 1:
					m.add((i, v-1))
				else:
					m.add((i-((v-1)*s+(v-1)), v-1))
		else:
			v += 1
	return (m, s, v)


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


