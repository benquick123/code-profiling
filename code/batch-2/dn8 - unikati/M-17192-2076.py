def izvedi(ime_datoteke):
    datoteka = open(ime_datoteke)
    x = 0
    y = 0
    smeri = ["N", 'E', "S", "W"]
    indeks_smeri = 0
    pot = [(x, y, smeri[indeks_smeri])]
    for vrstica in datoteka:
        niz = vrstica.strip()

        if niz == "DESNO":
            if indeks_smeri >= 3:
                indeks_smeri = 0
            else:
                indeks_smeri += 1

        elif niz == "LEVO":
            if indeks_smeri <= 0:
                indeks_smeri = 3
            else:
                indeks_smeri -= 1

        else:
            st_korakov = niz.split(" ", 1)[1]
            if indeks_smeri == 0:
                y -= int(st_korakov)
            elif indeks_smeri == 2:
                y += int(st_korakov)
            elif indeks_smeri == 1:
                x += int(st_korakov)
            else:
                x -= int(st_korakov)
        pot.append((x, y, smeri[indeks_smeri]))

    return pot

def opisi_stanje(x, y, smer):
    if smer == "N":
        return ("{:>3}:{:<3} {}".format(x, y, "^"))
    if smer == "E":
        return ("{:>3}:{:<3} {}".format(x, y, ">"))
    if smer == "S":
        return ("{:>3}:{:<3} {}".format(x, y, "v"))
    if smer == "W":
        return ("{:>3}:{:<3} {}".format(x, y, "<"))

def prevedi(ime_vhoda,ime_izhoda):
    pot=izvedi(ime_vhoda)
    dat=open(ime_izhoda,"w")
    for x,y,smer in pot:
        dat.write(opisi_stanje(x,y,smer)+"\n")
    dat.close()


def opisi_stanje_2(x,y,smer):
    if smer == "N":
        return ("{} {:>4}:{})".format("^", "(" + str(x), y))
    if smer == "E":
        return ("{} {:>4}:{})".format(">", "(" + str(x), y))
    if smer == "S":
        return ("{} {:>4}:{})".format("v", "(" + str(x), y))
    if smer == "W":
        return ("{} {:>4}:{})".format("<", "(" + str(x), y))





