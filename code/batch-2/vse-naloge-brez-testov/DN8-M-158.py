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
    f = open(ime_datoteke, "r")
    arr = [(0,0,"N")]
    switch = {"D": lambda ukaz, x, y, smer: premik("R", x, y, smer),
              "L": lambda ukaz, x, y, smer: premik("L", x, y, smer),
              "N": lambda ukaz, x, y, smer: premik(int(ukaz.split()[1]), x, y, smer)}
    for string in f.readlines():
        arr.append(switch[string[0]](string, arr[-1][0], arr[-1][1], arr[-1][2]))
    f.close()
    return arr

def opisi_stanje(x, y, smer):
	smeri = {"N": "^", "E": ">", "S":"v", "W":"<"}
	return  str(x).rjust(3, " ") + ":" + str(y).ljust(4, " ") + smeri[smer]

def prevedi(ime_vhoda, ime_izhoda):
	output_file = open(ime_izhoda, 'w')
	for i in izvedi(ime_vhoda):
		output_file.write(opisi_stanje(i[0], i[1], i[2]) + "\n")
	output_file.close()

def opisi_stanje_2(x, y, smer):
    smeri = {"N": "^", "E": ">", "S":"v", "W":"<"}
    return   smeri[smer] + ("(" + str(x)).rjust(5, " ") + ":" + str(y) + ")"


