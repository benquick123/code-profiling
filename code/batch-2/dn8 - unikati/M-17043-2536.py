def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "R":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "L":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer

def izvedi(ime_datoteke):
	x = 0
	y = 0
	smer = "N"
	stanja = [(x,y,smer)]
	
	with open(ime_datoteke) as datoteka:
		for vrstica in datoteka:	
			
			if vrstica == 'DESNO\n':
				stanja.append(premik("R",x,y,smer))
			elif vrstica == 'LEVO\n':
				stanja.append(premik("L",x,y,smer))
			else:
				stanja.append(premik( int(vrstica.split(" ")[1]) ,x,y,smer))
				
			x = stanja[len(stanja)-1][0]
			y = stanja[len(stanja)-1][1]
			smer = stanja[len(stanja)-1][2]
			
	return stanja		
		
def opisi_stanje(x, y, smer):	
	s = "{:>3d}:{:<3d} {}"
	if smer == 'N':
		return s.format(x,y,"^");
	elif smer == 'S':
		return s.format(x,y,"v");
	elif smer == 'W':
		return s.format(x,y,"<");
	else: #je east
		return s.format(x,y,">");
		
def prevedi(ime_vhoda, ime_izhoda):
	stanja = izvedi(ime_vhoda)
	for i in range(len(stanja)):
		stanja[i] = opisi_stanje(stanja[i][0],stanja[i][1],stanja[i][2])

	with open(ime_izhoda, 'w') as datoteka:
		for stanje in stanja:
			datoteka.write(stanje+"\n")
			
	datoteka.close()		