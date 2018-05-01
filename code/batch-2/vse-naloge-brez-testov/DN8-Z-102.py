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
    i = 0
    move = [(0, 0, "N")]
    dat = open(ime_datoteke)
    for x in dat:
        if x.split()[0] == "DESNO":
            move.append(premik("R", move[i][0], move[i][1], move[i][2]))
        elif x.split()[0] == "LEVO":
            move.append(premik("L", move[i][0], move[i][1], move[i][2]))
        else:
            koraki= x.split()[1]
            move.append(premik(int(koraki), move[i][0], move[i][1], move[i][2]))
        i += 1
    return move

def opisi_stanje(x,y,smer):
    for z in smer:
        if z == "N":
            return "{:3}:{:<4}{}".format(x,y,'^')
        elif z == 'E':
            return "{:3}:{:<4}{}".format(x, y, '>')
        elif z == 'S':
            return "{:3}:{:<4}{}".format(x, y, 'v')
        elif z == 'W':
            return "{:3}:{:<4}{}".format(x, y, '<')

def prevedi(ime_vhoda, ime_izhoda):
    z = izvedi(ime_vhoda)
    a = []
    pisanje = open(ime_izhoda, "w")
    for x,y,smer in z:
        a.append(opisi_stanje(x,y,smer)+"\n")
    for j in a:
        pisanje.write(j)
    pisanje.close()
