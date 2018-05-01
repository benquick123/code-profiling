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


#Uporabniske funkcije:

def izvedi(ime_datoteke):
    s = [(0, 0, 'N')]
    try:
        with open(ime_datoteke) as the_file:
            line = the_file.readline()
            if line:
                if line.strip() == "DESNO":
                    prejsnji = premik("R", 0, 0, "N")
                elif line.strip() == "LEVO":
                    prejsnji = premik("L", 0, 0, "N")
                else:
                    st = int(line.strip().split(" ")[1])
                    prejsnji = premik(st, 0, 0, "N")
                s.append(prejsnji)
                line = the_file.readline()
                while line:
                    if line.strip() == "DESNO":
                        prejsnji = premik("R", prejsnji[0], prejsnji[1], prejsnji[2])
                    elif line.strip() == "LEVO":
                        prejsnji = premik("L", prejsnji[0], prejsnji[1], prejsnji[2])
                    else:
                        st = int(line.strip().split(" ")[1])
                        prejsnji = premik(st, prejsnji[0], prejsnji[1], prejsnji[2])
                    s.append(prejsnji)
                    line = the_file.readline()
            else:
                print("Prazna datoteka!")
    finally:
        the_file.close()
    return s


def opisi_stanje(x, y, smer):
    if smer == "N":
        znak = '^'
    elif smer == "E":
        znak = '>'
    elif smer == "S":
        znak = 'v'
    else:
        znak = '<'
    return '{:>3}:{:<3} {}'.format(x, y, znak)


def prevedi(ime_vhoda, ime_izhoda):
    s = izvedi(ime_vhoda)
    with open(ime_izhoda, "w") as the_file:
        for x, y, smer in s:
            the_file.write(opisi_stanje(x, y, smer) + "\n")


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        znak = '^'
    elif smer == "E":
        znak = '>'
    elif smer == "S":
        znak = 'v'
    else:
        znak = '<'
    return '{} {:>4}:{})'.format(znak, "(" + str(x), y)




