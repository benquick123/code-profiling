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
    datoteka=open(ime_datoteke)
    X=0 #koordinati
    Y=0
    zacetna_smer="N"
    seznam=[(X,Y,zacetna_smer)] # na zacetku je na 0,0,N
    for vrstica in datoteka: # za vsako vrstico v datoteki
        if "DESNO" in vrstica: # če se obrne v desno potem R
            premikanje="R"
        if "LEVO" in vrstica: # če se obrne v levo potem L
            premikanje="L"
        if "NAPREJ" in vrstica: # dobimo koliko se premakne
            premikanje=int(vrstica.split()[1])
        seznam.append(premik(premikanje, X, Y, zacetna_smer)) #v seznam dodamo elemente
        X = premik(premikanje, X, Y, zacetna_smer)[0] #spremenimo koordinati
        Y = premik(premikanje, X, Y, zacetna_smer)[1]
        zacetna_smer = premik(premikanje, X, Y, zacetna_smer)[2]
    return seznam

def opisi_stanje(x,y,smer):

    if smer=="N": #preverjanje smeri
        izpissmer="^"
    if smer=="S":
        izpissmer="v"
    if smer=="E":
        izpissmer=">"
    if smer=="W":
        izpissmer="<"
    return("{:>3}:{:<3} {}".format(x,y,izpissmer)) #.format

def prevedi(ime_vhoda, ime_izhoda):
    seznam=izvedi(ime_vhoda)
    datoteka=open(ime_izhoda, "w")# odpre datoteko, če jo ni ustvari novo z vsebino w
    for vrstica in seznam: # za vsako vrstico v seznamu
        datoteka.write(opisi_stanje(vrstica[0],vrstica[1],vrstica[2])+"\n")
    # v datoteko vpisemo posamezen element terke, in potem \n da preskoci v novo vrsto


