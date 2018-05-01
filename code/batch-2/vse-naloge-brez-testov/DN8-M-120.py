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

    situacija= [(0, 0, 'N')]
    x, y, smer= 0, 0, 'N'

    for poteza in datoteka:
        if poteza =='DESNO\n':
            x, y, smer= premik('R', x, y, smer)
        elif poteza == 'LEVO\n':
            x, y, smer=premik('L', x, y, smer)
        else:
            stevilka=int(poteza.replace('NAPREJ ', ''))
            x, y, smer =premik(stevilka, x, y, smer)
        situacija.append((x, y, smer))

    return situacija






def opisi_stanje(x, y, smer):

    desno = ''
    levo = ''
    niz_desno= 3 - len(str(y))
    niz_levo= 3 - len(str(x))


    for i in range(niz_levo):
        levo =levo + ' '

    for i in range(niz_desno):
        desno= desno + ' '

    if smer=='N':
        nova_smer = '^'
    elif smer=='S':
        nova_smer = 'v'
    elif smer=='W':
        nova_smer='<'
    elif smer=='E':
        nova_smer='>'

    return levo + str(x) + ':' + str(y) + desno + ' ' + nova_smer





def prevedi(ime_vhoda, ime_izhoda):

    datoteka =open(ime_vhoda, 'r')
    situacija=izvedi(ime_vhoda)

    for i in range(len(situacija)):
        situacija[i]=opisi_stanje(situacija[i][0], situacija[i][1], situacija[i][2])

    X=open(ime_izhoda,'w')

    for podatek in situacija:
        X.write(str(podatek)+'\n')







