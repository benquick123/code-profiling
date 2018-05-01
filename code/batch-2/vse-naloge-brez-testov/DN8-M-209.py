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
#print(premik("R",0,0,"N"))

def izvedi(ime_datoteke):
     ime = open(ime_datoteke)
     rezultat = (0,0,"N")
     seznam_zaporednih_stanj = [rezultat]
     for line in ime:
         #print(line)
         if "DESNO" == line.strip():
            rezultat = premik("R",rezultat[0],rezultat[1],rezultat[2])
         elif "LEVO" == line.strip():
            rezultat = premik("L",rezultat[0],rezultat[1],rezultat[2])
         elif "N" == line[0]:
            line = line.split(" ")
            rezultat = premik(int(line[1]),rezultat[0],rezultat[1],rezultat[2])
         seznam_zaporednih_stanj.append(rezultat)
     return seznam_zaporednih_stanj

#print(izvedi("primer.txt"))

def opisi_stanje(x,y,smer):
    if smer == "N":
        smer = "^"
        return "{:3}:{:<3}{:>2}".format(x,y,smer)
    if smer == "S":
        smer = "v"
        return "{:3}:{:<3}{:>2}".format(x,y,smer)
    if smer == "E":
        smer = ">"
        return "{:3}:{:<3}{:>2}".format(x,y,smer)
    if smer == "W":
        smer = "<"
        return "{:3}:{:<3}{:>2}".format(x,y,smer)

#print(opisi_stanje(0, 12, "N"))

def prevedi(ime_vhoda,ime_izhoda):
    stanja_datoteke = izvedi(ime_vhoda)
    ime = open(ime_izhoda, "w")
    for stanje in stanja_datoteke:
        lepse_stanje = opisi_stanje(stanje[0],stanje[1],stanje[2])
        ime.write(lepse_stanje + "\n")

#print(prevedi("primer.txt", "stanja.txt"))

def opisi_stanje_2(x,y,smer):
    if smer == "N":
        smer = "^"
        return "{:2}{:>4}:{:>2}".format(smer,"(" + str(x),str(y) + ")")
    if smer == "S":
        smer = "v"
        return "{:2}{:>4}:{:>2}".format(smer,"(" + str(x),str(y) + ")")
    if smer == "E":
        smer = ">"
        return "{:2}{:>4}:{:>2}".format(smer,"(" + str(x),str(y) + ")")
    if smer == "W":
        smer = "<"
        return "{:2}{:>4}:{:>2}".format(smer,"(" + str(x),str(y) + ")")

print(opisi_stanje_2(0,12,"N"))

