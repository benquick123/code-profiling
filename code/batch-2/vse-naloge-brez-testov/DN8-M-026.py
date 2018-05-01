'''
    Opis: naloge z datotekami,string formatting
    Avtor: Blaz Kumer
    Datum: 12. 12. 2017

'''

def izvedi(ime_datoteke):
    x=y=0
    smer="N"
    dat=open(ime_datoteke)
    pozicije=[(x,y,smer)]
    for vrs in dat:
        if vrs.startswith("DESNO"):
            pre= premik("R", x, y, smer)
        elif vrs.startswith("LEVO"):
            pre = premik("L", x, y, smer)
        else:
            pre = premik(int(vrs.split()[1]), x, y, smer)
        pozicije.append(pre)
        smer=pre[2]
        x=pre[0]
        y=pre[1]
    dat.close()
    return pozicije

def opisi_stanje(x,y,smer ):
    if smer=="N":
        return("{:>3}:{:<3} ^".format(x,y))
    elif smer=="S":
        return("{:>3}:{:<3} v".format(x,y))
    elif smer=="E":
        return("{:>3}:{:<3} >".format(x,y))
    else:
        return("{:>3}:{:<3} <".format(x,y))

def prevedi(ime_vhoda, ime_izhoda):
    seznam=izvedi(ime_vhoda)
    datoteka = open(ime_izhoda ,"w")
    for ter in seznam:
        datoteka.write(opisi_stanje(ter[0],ter[1],ter[2]))
        datoteka.write("\n")
    datoteka.close()

def opisi_stanje_2(x,y,smer):
    sx = "(" + str(x)
    if smer == "N":
        return "^{: >5}:{})".format(sx, y)
    elif smer == "S":
        return "v{: >5}:{})".format(sx, y)
    elif smer == "E":
        return ">{: >5}:{})".format(sx, y)
    else:
        return "<{: >5}:{})".format(sx, y)

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


