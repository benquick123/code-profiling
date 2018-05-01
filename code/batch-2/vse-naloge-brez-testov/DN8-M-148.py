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
	with open(ime_datoteke) as f:
		tekst = f.readlines()
	pot = [(0, 0, "N")]
	for i, vrstica in enumerate(tekst):
		x, y ,smer = pot[i]
		if "NAPREJ" in vrstica:
			pot.append(premik(int(vrstica.split()[1]), x, y ,smer))
		elif "DESNO" in vrstica:
			pot.append(premik("R", x, y, smer))
		else:
			pot.append(premik("L", x, y, smer))
	return pot

def opisi_stanje(x, y, smer):
	smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
	return str("{x:>3}:{y:<3} {smer:^}").format(x=x, y=y, smer=smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
	datoteka = open(ime_izhoda, "w")
	for i in range(len(izvedi(ime_vhoda))):
		x, y, smer = izvedi(ime_vhoda)[i]
		datoteka.write(opisi_stanje(x, y, smer) + "\n")
	datoteka.close()

def opisi_stanje_2(x, y, smer):
	smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
	return str("{smer:^} {x:>4}:{y:<}").format(x="("+str(x), y=str(y)+")", smer=smeri[smer])
	
