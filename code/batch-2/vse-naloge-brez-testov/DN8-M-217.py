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

def izvedi(ime_datotke):
	polje = []
	polje.append((0,0,'N'))
	f = open(ime_datotke)
	i=0
	for vrstica in f:
		vrstica =vrstica.replace("\n","")
		if vrstica == "DESNO":
			vrstica = "R"
		elif vrstica == "LEVO":
			vrstica = "L"
		else:
			vrstica = int(vrstica.replace("NAPREJ ",""))
		polje.append(premik(vrstica,polje[i][0],polje[i][1],polje[i][2]))	
		i+=1
	return polje
	
def opisi_stanje(x,y,smer):
	if smer == "N":
		znak = "^"
	elif smer=="E":
		znak = ">"
	elif smer=="S":
		znak = "v"
	elif smer=="W":
		znak = "<"
	return  "{x:>3}:{y:<3} {znak}".format(x=x,y=y,znak=znak)
	
def prevedi(ime_vhoda,ime_izhoda):
	polje=izvedi(ime_vhoda)
	pisi = open(ime_izhoda,"w")
	for x,y,smer in polje:
		vpis = opisi_stanje(x,y,smer)
		vpis = vpis + "\n"
		pisi.write(vpis)
	pisi.close()
	


