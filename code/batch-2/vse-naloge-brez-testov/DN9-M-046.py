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
    datoteka = open(ime_datoteke)
    robot = (0, 0, 'N')
    rx, ry, rd = robot

    status = []

    for vrstica in datoteka:
        rx, ry, rd = robot
        status.append(robot)
        vrstica = vrstica.strip()
        if vrstica == 'LEVO':
            robot = premik('L', rx, ry, rd)
        elif vrstica == 'DESNO':
            robot = premik('R', rx, ry, rd)
        else:
            naprej = int(vrstica.split(' ')[1])
            robot = premik(naprej, rx, ry, rd)
    status.append(robot)
    datoteka.close()
    return status

def opisi_stanje(x, y, smer):
	smeri = { 'N':'^', 'E':'>', 'W':'<', 'S':'v' }
	return "{0:>3}:{1:<4}{2}".format(x,y,smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
    prevodi = [opisi_stanje(x,y,smer) for x,y,smer in izvedi(ime_vhoda)]
    datoteka = open(ime_izhoda,"w")
    for prevod in prevodi:
        datoteka.write(prevod+"\n")
    datoteka.close()

def opisi_stanje_2(x, y, smer):
	smeri = { 'N':'^', 'E':'>', 'W':'<', 'S':'v' }
	return "{2}{0:>5}:{1}".format("("+str(x),str(y)+")",smeri[smer])

