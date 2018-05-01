
import math

# Za oceno 6
def sosedov(x, y, mine):
    return len([mina_x for mina_x, mina_y in mine if 0 < math.sqrt((mina_x - x)**2 + (mina_y - y)**2) < 1.42])

def najvec_sosedov(mine, s, v):
    return [(x,y) for i in range(8,-1,-1) for x in range(s) for y in range(v) if sosedov(x,y,mine) == i][0]

def brez_sosedov(mine, s, v):
    return set((x, y) for x in range(s) for y in range(v) if sosedov(x, y, mine) == 0)

def po_sosedih(mine, s, v):
    return {i: set((x, y) for x in range(s) for y in range(v) if sosedov(x, y, mine) == i) for i in range(9)}

# Za oceno 7
def dolzina_poti(pot):
	return sum([abs(x0-x1)+abs(y0-y1) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])

def varen_premik(x0, y0, x1, y1, mine):
	return len([(x,y) for x in range(min([x0,x1]),max([x0,x1])+1) for y in range(min([y0,y1]),max([y0,y1])+1) if (x,y) in mine])==0

def varna_pot(pot, mine):
	return pot == [] or all([pot[0] not in mine] + [varen_premik(x0,y0,x1,y1,mine) for (x0, y0), (x1, y1) in zip(pot, pot[1:])])

# Za oceno 8
def polje_v_mine(polje):
	mine = set()
	x = y = s = v = 0
	for indeks, znak in enumerate(polje):
		if znak != ' ':
			if znak == 'X':
				mine.add( (x,y) )
			x += 1
		if indeks+1 == len(polje) or znak == ' ':
			s = x
			x = 0
			y += 1
	v = y
	return (mine,s,v)

# Za oceno 10
def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def kot_dodaj(kot,sprememba):
    kot += sprememba
    if kot < 0:
        return (360 + kot)
    return (kot % 360)

def kot_normaliziraj(kot):
    return(int(math.cos(math.radians(kot))),-int(math.sin(math.radians(kot))))

def kordinate_normaliziraj(kordinate):
    x,y = kordinate
    return(sign(x),sign(y))

def kordinate_odstej(kot1,kot2):
    x1,y1 = kot1
    x2,y2 = kot2
    return (x2-x1,y2-y1)

def kordinate_v_kot(kordinate):
    x,y = kordinate
    return kot_dodaj(math.degrees(math.atan2(y,x)),0)

def preberi_pot(ukazi):
    kot = 90
    x = y = 0
    pot = [(0,0)]
    
    if ukazi == None:
        return 

    ukazi = ukazi.split()
    for ukaz in ukazi:
        if ukaz == "DESNO":
            kot = kot_dodaj(kot,-90)
        elif ukaz == "LEVO":
            kot = kot_dodaj(kot,90)
        else:
            kx,ky = kot_normaliziraj(kot)
            ukaz = int(ukaz)
            x += kx * ukaz
            y += ky * ukaz
            pot.append((x,y))
    return pot

def zapisi_pot(pot):
    kot = 90
    ukazi = ""
    for kordinate1, kordinate2 in zip(pot, pot[1:]):
        dx, dy = kordinate_odstej(kordinate1,kordinate2)
        kordinate_razlika = (dx,-dy)
        kordinate_razlika_normalizirana = kordinate_normaliziraj(kordinate_razlika)
        kot_iskani = kordinate_v_kot(kordinate_razlika_normalizirana)
        kot_razlika = kot_iskani-kot
        stevilo_ukazov = kot_razlika / 90

        kot = kot_iskani
        for i in range(int(abs(stevilo_ukazov))):
            if(stevilo_ukazov < 0):
                ukazi += "DESNO\n"
            else:
                ukazi += "LEVO\n"
        dx, dy = kordinate_razlika
        if dx != 0:
            ukazi += str(abs(dx)) + "\n"
        if dy != 0:
            ukazi += str(abs(dy)) + "\n"
    return ukazi

