# Obvezna naloga

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
    x,y = 0,0
    s = "N"
    sez = [(x,y,s)]
    for vrstica in open(ime_datoteke):
        v = vrstica.strip()
        if " " not in v:
            if v == "DESNO":
                pre = premik("R",x,y,s)
                s = pre[2]
                sez.append(pre)
            elif v == "LEVO":
                pre = premik("L",x,y,s)
                s = pre[2]
                sez.append(pre)
        else:
            pre = premik(int(v.split(" ")[1]), x, y, s)
            s = pre[2]
            x = pre[0]
            y = pre[1]
            sez.append(pre)
    return sez

def opisi_stanje(x, y, smer):
    smeri = {"N":"^","E":">","S":"v","W":"<"}
    return "{:>3}:{:<3} {}".format(x,y,smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
    s = izvedi(ime_vhoda)
    k = open(ime_izhoda,"w")
    for i in range(len(s)):
        k.write(opisi_stanje(s[i][0],s[i][1],s[i][2])+"\n")
    k.close()

# Dodatna naloga

def opisi_stanje_2(x, y, smer):
    smeri = {"N": "^", "E": ">", "S": "v", "W": "<"}
    s = "(" + str(x)
    return "{}{:>5}:{})".format(smeri[smer],s,y)

