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
    premiki = []
    x = 0
    y = 0
    smer = 'N'
    ukaz = 0
    st_polj = ''
    datoteka = open(ime_datoteke)

    premiki.append(premik(ukaz, x, y, smer))

    for line in datoteka:
        print(line)
        st = 0
        prebran_ukaz = line
        if prebran_ukaz == 'DESNO\n':
            ukaz = 'R'
            terka = premik(ukaz, x, y, smer)
            x = terka[0]
            y = terka[1]
            smer = terka[2]
            premiki.append(terka)
        elif prebran_ukaz == 'LEVO\n':
            ukaz = 'L'
            terka = premik(ukaz, x, y, smer)
            x = terka[0]
            y = terka[1]
            smer = terka[2]
            premiki.append(terka)
        else:
            for char in prebran_ukaz:
                if (st > 0) and (char != '\n'):
                    st_polj = st_polj + char
                if char == ' ':
                    st += 1
            ukaz = int(st_polj)
            terka = premik(ukaz, x, y, smer)
            x = terka[0]
            y = terka[1]
            smer = terka[2]
            premiki.append(terka)
        st_polj = ''

    datoteka.close()
    return premiki

def opisi_stanje(x, y, smer):
    znak = ''

    if smer == 'N':
        znak += '^'
    elif smer == 'E':
        znak += '>'
    elif smer == 'S':
        znak += 'v'
    elif smer == 'W':
        znak += '<'

    stanje = ("{:>3}:{:<3} {}".format(x, y, znak))
    return stanje

def prevedi(ime_vhoda, ime_izhoda):
    nova_datoteka = open(ime_izhoda, 'w')
    premiki = izvedi(ime_vhoda)
    for i in premiki:
        stanje = opisi_stanje(i[0], i[1], i[2])
        nova_datoteka.write(stanje)
        nova_datoteka.write('\n')

    nova_datoteka.close()
    nova_datoteka = open(ime_izhoda, 'r')
    print(nova_datoteka.read())
    nova_datoteka.close()

def opisi_stanje_2(x, y, smer):
    znak = ''

    if smer == 'N':
        znak += '^'
    elif smer == 'E':
        znak += '>'
    elif smer == 'S':
        znak += 'v'
    elif smer == 'W':
        znak += '<'

    x = ('(' + str(x))
    y = (str(y) + ')')
    stanje = ("{} {X:>4}:{Y:<}".format(znak, X = x, Y = y))
    return stanje


