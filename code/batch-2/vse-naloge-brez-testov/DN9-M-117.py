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

def parse_str(s):
   try:
      return eval(str(s))
   except:
      return

def izvedi(ime_datoteke):
    pot = []
    x = 0
    y = 0
    smer = 'N'
    terka = x, y, smer
    ukazi = open(ime_datoteke, "r")
    pot.append(terka)
    for line in ukazi:

        if line[0] == "D":
            ukaz = "R"
            pot.append(premik(ukaz, x, y, smer))
            terka = premik(ukaz, x, y, smer)
            x = terka[0]
            y = terka[1]
            smer = terka[2]

        if line[0] == "L":
            ukaz = "L"
            pot.append(premik(ukaz, x, y, smer))
            terka = premik(ukaz, x, y, smer)
            x = terka[0]
            y = terka[1]
            smer = terka[2]

        elif line[0] == "N":
            word_list = line.split()
            ukaz = parse_str(word_list[-1])
            pot.append(premik(ukaz, x, y, smer))
            terka = premik(ukaz, x, y, smer)
            x = terka[0]
            y = terka[1]
            smer = terka[2]

    return pot

def opisi_stanje(x, y, smer):
    if smer == "N":
        return '{:>3}:{:<4}^'.format(x, y)

    if smer == "E":
        return '{:>3}:{:<4}>'.format(x, y)

    if smer == "S":
        return '{:>3}:{:<4}v'.format(x, y)

    if smer == "W":
        return '{:>3}:{:<4}<'.format(x, y)

def prevedi(ime_vhoda, ime_izhoda):
    terka = izvedi(ime_vhoda)
    file = open(ime_izhoda, "w")
    for i in range(len(terka)):
        zapis = opisi_stanje(terka[i][0],terka[i][1],terka[i][2])
        file.write(zapis)
        file.write("\n")
    file.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        return '^{:>4}:{:<2}'.format(x, y)

    if smer == "E":
        return '>{:>4}:{:<2}'.format(x, y)

    if smer == "S":
        return 'v{:>4}:{:<2}'.format(x, y)

    if smer == "W":
        return '<{:>4}:{:<2}'.format(x, y)


