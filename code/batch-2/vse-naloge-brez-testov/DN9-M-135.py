import re
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
    sez = [(0,0,'N')]
    x= 0
    y=0
    znak = "N"
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        a = vrstica
        print(a)
        if a == "DESNO\n":
            r=premik("R",x,y,znak)
            sez.append(r)
            x = r[0]
            y = r[1]
            znak = r[2]
            print(x,y,znak)

        elif a == "LEVO\n":
            e= premik("L", x, y, znak)
            sez.append(e)
            x = e[0]
            y=e[1]
            znak =e[2]
            print(x, y, znak)
        else:
            o= re.findall('\d+', vrstica)
            e = premik(int(o[0]), x, y, znak)
            sez.append(e)
            x = e[0]
            y = e[1]
            znak = e[2]

    datoteka.close()
    return sez
def opisi_stanje(x,y,smer):
    if smer == "N":
        a = '  {:>1}:{:>1}  {:>1}'.format(x, y,'^')
    if smer == "S":
        a = ' {:>1}:{:>1} {:>1}'.format(x, y,'v')
    if smer == "W":
        a = '  {:>1}:{:>1}   {:>1}'.format(x, y,'<')
    if smer == "E":
        a = '{:>1}:{:>1}   {:>1}'.format(x, y,'>')
    return a
def prevedi(ime_vhoda,ime_izhoda):
    a = izvedi(ime_vhoda)
    f = open(ime_izhoda, "w")
    for x in a:
        if x[2] == "N":
            if len(str(x[0]))==1:
                a = ' {:>2}:{:>1}   {:>1}'.format(x[0], x[1], '^')
            if len(str(x[0]))==2:
                a = ' {:>2}:{:>1}   {:>1}'.format(x[0], x[1], '^')
            if len(str(x[1])) == 3:
                a = '  {:>1}:{:>1} {:>1}'.format(x[0], x[1], '^')
        if x[2] == "S":
            if len(str(x[0])) == 1:
                a = '  {:>1}:{:>1}   {:>1}'.format(x[0], x[1], 'v')
            if len(str(x[0])) == 2:
                a = ' {:>1}:{:>1}   {:>1}'.format(x[0], x[1], 'v')
            if len(str(x[1])) == 3:
                a = '  {:>1}:{:>1} {:>1}'.format(x[0], x[1], 'v')
        if x[2] == "W":
            if len(str(x[0])) == 1:
                a = '  {:>1}:{:>1}   {:>1}'.format(x[0], x[1], '<')
            if len(str(x[0])) == 2:
                a = ' {:>1}:{:>1}   {:>1}'.format(x[0], x[1], '<')
            if len(str(x[1])) == 3:
                a = '  {:>1}:{:>1} {:>1}'.format(x[0], x[1], '<')
            if len(str(x[1])) == 3 and len(str(x[0])) == 3:
                a = '{:>1}:{:>1} {:>1}'.format(x[0], x[1], '<')
        if x[2] == "E":
            if len(str(x[0])) == 1:
                a = '  {:>1}:{:>1}   {:>1}'.format(x[0], x[1], '>')
            if len(str(x[0])) == 2:
                a = ' {:>1}:{:>1}   {:>1}'.format(x[0], x[1], '>')
        f.write(a+'\n')
    f.close()


