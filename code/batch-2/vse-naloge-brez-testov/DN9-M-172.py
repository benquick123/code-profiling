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
    koraki = list()
    pod = (0, 0, 'N')
    koraki.append(pod)
    st = 0
   # ukaz = ""
    for vrstica in open(ime_datoteke, "r"):
        podatek = vrstica.strip("\n").split()
        x = koraki[st][0]
        y = koraki[st][1]
        smer = koraki[st][2]
        if (podatek[0] == "DESNO"):
            ukaz="R"
        elif (podatek[0] == "LEVO"):
            ukaz="L"
        else:
            ukaz = int(podatek[1])
        pod = (premik(ukaz,x,y,smer))
        koraki.append(pod)
        st+=1
#    print(koraki)
    return koraki

def opisi_stanje(x, y, smer):
    znak = ""
    if smer == "N":
        znak = "^"
    elif smer == "S":
        znak = "v"
    elif smer == "E":
        znak = ">"
    elif smer == "W":
        znak = "<"

    niz = "{:3}:{:<3} {}"
  #  print(niz.format(x, y, znak))
    return niz.format(x, y, znak)

def prevedi(ime_vhoda, ime_izhoda):
    koraki = izvedi(ime_vhoda)
    dat = open(ime_izhoda, "w")
    for ele in koraki:
        x = ele[0]
        y = ele[1]
        znak = ele[2]
        niz = (opisi_stanje(x, y, znak))
        dat.write(niz + '\n')

    dat.close()

# def opisi_stanje_2(x, y, smer):
#     znak = ""
#     if smer == "N":
#         znak = "^"
#     elif smer == "S":
#         znak = "v"
#     elif smer == "E":
#         znak = ">"
#     elif smer == "W":
#         znak = "<"
#
#     niz = "{} ({:}:{:})"
#     print(niz.format(znak, x, y))
#     return niz.format(znak, x, y)

