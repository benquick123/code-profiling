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


########################
# Za oceno 6

def sosedov(x, y, mine):
	st=0
	
	if (x+1,y) in mine:
		st+=1
		
	if (x-1,y) in mine:
		st+=1
	
	if (x,y+1) in mine:
		st+=1
	
	if (x,y-1) in mine:
		st+=1
		
	if (x+1,y+1) in mine:
		st+=1
		
	if (x-1,y-1) in mine:
		st+=1
	
	if (x-1,y+1) in mine:
		st+=1
	
	if (x+1,y-1) in mine:
		st+=1
		
	return st


def najvec_sosedov(mine, s, v):	
	naj = 0
	k = (0,0)
	for koord in vsa_polja(s,v,):
		if sosedov(koord[0],koord[1],mine) > naj:
			naj = sosedov(koord[0],koord[1], mine)
			k = koord
	return k

def brez_sosedov(mine, s, v):
	m = set()
	for koord in vsa_polja(s,v,):
		if sosedov(koord[0],koord[1],mine) is 0:
			m.add(koord)
	return m

def po_sosedih(mine, s, v): 
	sl = {0:set(), 1:set(), 2:set(), 3:set(), 4:set(), 5:set(), 6:set(), 7:set(), 8:set()}
	for koord in vsa_polja(s,v,):
		sl[sosedov(koord[0],koord[1],mine)].add(koord)
	return sl

########################
# Za oceno 7

def dolzina_poti(pot):
	d = 0
	if not pot == []:
		x1 = pot[0][0]
		y1 = pot[0][1]
		for koord in pot:
			d += abs(koord[0]-x1) + abs(koord[1]-y1)
			x1 = koord[0]
			y1 = koord[1]
	return d

def varen_premik(x0, y0, x1, y1, mine):
	if (x0,y0) in mine:
		return False
	if (x1,y1) in mine:
		return False
	if x0 == x1:
		if y0 < y1:
			while not y0 == y1:
				y0 += 1
				if (x0,y0) in mine:
					return False
		if y1 < y0:
			while not y0 == y1:
				y0 -= 1
				if (x0,y0) in mine:
					return False
	if y1 == y0:
		if x0 < x1:
			while not x0 == x1:
				x0 += 1
				if (x0,y0) in mine:
					return False
		if x1 < x0:
			while not x0 == x1:
				x0 -= 1
				if (x0,y0) in mine:
					return False
	return True

def varna_pot(pot, mine):
	prvic = True
	if len(pot) == 1:
		if pot[0] in mine:
			return False
	else:
		for x, y in pot:
			if prvic:
				x0 = x
				y0 = y
				prvic = False
				continue
				
			if varen_premik(x0, y0, x, y, mine) == False:
				return False
				
			x0 = x
			y0 = y
			
			
	return True



########################
# Za oceno 8

def polje_v_mine(polje):

	v = 0
	s = 0
	st_s = 1
	st_v = 1
	mine = set()
	
	while polje[len(polje)-1:] == " ":
		polje = polje[:len(polje)-1]
	
	for crka in polje:
		
		if crka == "X":
			mine.add((s,v))
			
		if crka == " ":
			v += 1
			st_s = s
			s = 0
			continue
			
		s += 1
	
	if not s == 0:
		st_s = s
	st_v = v+1
	
	return (mine, st_s, st_v)

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