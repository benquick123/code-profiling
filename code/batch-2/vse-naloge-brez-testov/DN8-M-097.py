#coding=utf-8
#from __future__ import unicode_literals

def izvedi(ime_datoteke):

    x,y,s = 0, 0, 'N'
#    robot = (0,0,'N')
    premiki = [(0, 0, 'N')]

    for vrstica in open(ime_datoteke) :
        vrstica = vrstica.strip()

        if vrstica == 'DESNO' :
            vrstica = 'R'
        elif vrstica == 'LEVO' :
            vrstica = 'L'
        else :
            vrstica = int(vrstica.split(' ')[1])

    #    print("VR 222 ", vrstica)
    #    print("Premik ", premik(vrstica, x,y,s))

        x,y,s = premik(vrstica, x,y,s)

    #    print("Robot: ",x,y,s)

        premiki.append((x,y,s))

    return premiki
#    print("PREMIKI:   ", premiki)



def opisi_stanje(x, y, smer):

    # if smer == 'N' :
    # smer = '^'.....

    #    print("x: ", x)
    #    print("y: ", y)
    #    print("smer: ", smer)


    neba = 'NESW'
    pusc = '^>v<'
    smer = pusc[neba.index(smer)]

    #    print("{:>3}:{:<3} {}".format(x,y,smer))

    return "{:>3}:{:<3} {}".format(x,y,smer)



def prevedi(ime_vhoda, ime_izhoda):

    premiki = izvedi(ime_vhoda)

    dat = open(ime_izhoda, 'w')

    for premik in premiki :
    #    print("333")
    #    stanje = opisi_stanje(premik)
    #    print("444")
        dat.write(opisi_stanje(premik[0], premik[1], premik[2]) + "\n")

    dat.close()

def opisi_stanje_2(x, y, smer):

    neba = 'NESW'
    pusc = '^>v<'
    smer = pusc[neba.index(smer)]

    x = str(x)
    y = str(y)

    # print("{} {:>4}:{}".format(smer,"("+x,y+")"))

    return "{} {:>4}:{}".format(smer,"("+x,y+")")


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


