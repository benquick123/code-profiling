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

    datoteka = open(ime_datoteke) #odpre datoteko
    t = [(0, 0, 'N')]   #seznam pozicij
    t_mesto = [0, 0, 'N']   #trenutno mesto izračuna

    for vrstica in datoteka:    #sprehod skozi vrstice datoteke, ki je dana

        if vrstica.strip() == "DESNO":
            t.append(premik("R", t_mesto[0], t_mesto[1], t_mesto[2]))   #doda novo trenutno mesto
            t_mesto = premik("R", t_mesto[0], t_mesto[1], t_mesto[2])   #spremeni trenutno mesto

        elif vrstica.strip() == "LEVO":
            t.append(premik("L",t_mesto[0], t_mesto[1], t_mesto[2]))    #doda novo trenutno mesto
            t_mesto = premik("L", t_mesto[0], t_mesto[1], t_mesto[2])   #spremeni trenutno mesto

        else:
            a = int(re.search(r'\d+', vrstica).group())                 #poišče število v str(), POZOR! uporabno samo če je eno število
            t.append(premik(a,t_mesto[0], t_mesto[1], t_mesto[2]))   #doda novo trenutno mesto
            t_mesto = premik(a, t_mesto[0], t_mesto[1], t_mesto[2])     #spremeni trenutno mesto
    return t

def opisi_stanje(x, y, smer):
    if smer == "N":
        a = '^'
    elif smer =="E":
        a = '>'
    elif smer =="W":
        a = '<'
    else:
        a = 'v'
    return ("{x:>3}:{y:<3} {smer}".format(x=x, y=y, smer = a))

def prevedi(ime_vhoda, ime_izhoda):
    datoteka = open(ime_vhoda, "r")
    izhodna_datoteka = open(ime_izhoda, "w")
    izhodna_datoteka.write(opisi_stanje(0, 0, "N")+'\n')
    t_mesto = [0, 0, 'N']
    for vrstica in datoteka:   #sprehod skozi vrstice datoteke, ki je dana

        if vrstica.strip() == "DESNO":
            d = premik("R", t_mesto[0], t_mesto[1], t_mesto[2])         #za MALO boljšo preglednost
            izhodna_datoteka.write(opisi_stanje(d[0],d[1],d[2])+'\n')   #zapiše novo trenutno mesto v izhodno datoteko
            t_mesto = premik("R", t_mesto[0], t_mesto[1], t_mesto[2])   #spremeni trenutno mesto

        elif vrstica.strip() == "LEVO":
            l = premik("L", t_mesto[0], t_mesto[1], t_mesto[2])         #za MALO boljšo preglednost
            izhodna_datoteka.write(opisi_stanje(l[0], l[1], l[2])+'\n') #zapiše novo trenutno mesto v izhodno datoteko
            t_mesto = premik("L", t_mesto[0], t_mesto[1], t_mesto[2])   #spremeni trenutno mesto

        else:
            a = int(re.search(r'\d+', vrstica).group())                 #poišče število v str(), POZOR! uporabno samo če je eno število
            n = premik(a, t_mesto[0], t_mesto[1], t_mesto[2])           #za MALO boljšo preglednost
            izhodna_datoteka.write(opisi_stanje(n[0],n[1],n[2])+'\n')   #zapiše novo trenutno mesto v izhodno datoteko
            t_mesto = premik(a, t_mesto[0], t_mesto[1], t_mesto[2])     #spremeni trenutno mesto
    izhodna_datoteka.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        a = '^'
    elif smer =="E":
        a = '>'
    elif smer =="W":
        a = '<'
    else:
        a = 'v'
    return ("{smer} {x:>4}{d:>}{y:>{y_w}})".format(smer=a, x='('+str(x), y=y, d=":",x_w=len(str(x)),y_w=len(str(y))))

