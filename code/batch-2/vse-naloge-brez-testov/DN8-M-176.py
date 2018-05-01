def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "DESNO":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "LEVO":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * int(ukaz)
        y += dy * int(ukaz)
    return (x, y, smer)

def izvedi(ime_datoteke):
    ukazi = open(ime_datoteke)
    ukazi = ukazi.read()
    ukazi = ukazi.split()
    premiki = [(0,0,'N')]
    prevPremik = (0,0,'N')
    for ukaz in ukazi:
        if ukaz == 'NAPREJ':
            continue
        currPremik = premik(ukaz, prevPremik[0], prevPremik[1], prevPremik[2])
        premiki.append(currPremik)
        prevPremik = currPremik
    return premiki

def opisi_stanje(x, y, smer):
    if smer == 'N':
        smert = '^'
    elif smer == 'S':
        smert = 'v'
    elif smer == 'E':
        smert = '>'
    else:
        smert = '<'
    ret = "{0:>3}:{1:<3} {2}".format(x,y,smert)
    return ret

def prevedi(ime_vhoda, ime_izhoda):
    inp = izvedi(ime_vhoda)
    out = open(ime_izhoda, 'w')
    for x, y, smer in inp:
        out.write(opisi_stanje(x,y,smer) + "\n")
    out.close()

def opisi_stanje_2(x,y, smer):
    if smer == 'N':
        smert = '^'
    elif smer == 'S':
        smert = 'v'
    elif smer == 'E':
        smert = '>'
    else:
        smert = '<'
    odmik = 5 - len(str(x))
    ret = "{0:<}{1:>" + str(odmik) + "}{2}:{3})"
    return ret.format(smert,str('('),x,y)

