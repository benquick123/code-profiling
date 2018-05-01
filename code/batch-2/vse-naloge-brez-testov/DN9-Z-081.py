#
#1.Napiši funkcijo izvedi(ime_datoteke), ki kot argument dobi ime datoteke z ukazi, ki naj jih robot izvede. Datoteka je oblike:

def izvedi(ime_datoteke):
    datoteka=open(ime_datoteke)
    novi_seznam_premikov=[]
    x=0
    y=0
    novo_stanje=(0,0,"N")
    novi_seznam_premikov.append(novo_stanje)
    trenutna_smer= "N"

    for vrstica in datoteka:
        ukazi=vrstica.split(" ")
        print(ukazi)
        if len(ukazi) ==1:
            smer_ukaz="" #prazni niz
            smer=ukazi[0].strip()
            if smer == "DESNO":
                smer_ukaz="R"
            elif smer == "LEVO":
                smer_ukaz= "L"

            novo_stanje=premik(smer_ukaz,x,y,trenutna_smer)

        elif len(ukazi)==2:
            premik_kvadratek=int(ukazi[1].strip())
            novo_stanje=premik(premik_kvadratek,x,y,trenutna_smer)
        novi_seznam_premikov.append(novo_stanje)
        x = novo_stanje[0]
        y = novo_stanje[1]
        trenutna_smer = novo_stanje[2]
    print(novi_seznam_premikov)
    return novi_seznam_premikov

def opisi_stanje(x,y,smer): # ^, >, v in <
    if smer == "N":
        smer_znak="^"
    elif smer== "W":
        smer_znak="<"
    elif smer =="S":
        smer_znak="v"
    elif smer=="E":
        smer_znak=">"

    niz= "{x:3}:{y:3}".format(x=x, y=str(y)) + " " + smer_znak

    return niz

#Napiši funkcijo prevedi(ime_vhoda, ime_izhoda). Funkcija mora prebrati vhodno datoteko (najbrž tako, da pokliče funkcijo izvedi?) in v izhodno datoteko izpisati zaporedje stanj v obliki, kot jo vrača funkcija opisi_stanje.

#Če pokličemo prevedi("primer.txt", "stanja.txt"), mora ustvariti datoteko stanja.txt z naslednjo vsebino:

def prevedi(ime_vhoda, ime_izhoda):
    seznam_premikov=izvedi(ime_vhoda)
    datoteka_za_pisanje=open(ime_izhoda,"w")
    for x,y,smer in seznam_premikov:

        stanje=opisi_stanje(x,y,smer)
        datoteka_za_pisanje.write(stanje + "\n")
    datoteka_za_pisanje.close()

#DODATNA

def popravi(str):
    for i in range (len(str)):
        znak=str[i]
        if znak!=" ":
            str=str[:i]+"("+str[i:]

            break
    return str

def opisi_stanje_2(x,y,smer):
    if smer == "N":
        smer_znak = "^"
    elif smer == "W":
        smer_znak = "<"
    elif smer == "S":
        smer_znak = "v"
    elif smer == "E":
        smer_znak = ">"

    niz = smer_znak+ popravi("{x:4}:{y})".format(x=x, y=str(y)) )

    return niz































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


