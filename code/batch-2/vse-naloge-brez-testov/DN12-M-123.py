def preberi(ime_datoteke):
    slovar_krozisc = {}
    datoteka = open(ime_datoteke, mode='r',encoding='UTF-8')
    for i, vrstica in enumerate(datoteka,1):
        vrstica = vrstica.strip()
        vrstica = list(map(int, vrstica.split()))
        prvi = vrstica[0]
        if min(vrstica) == vrstica[0]:
            slovar_krozisc[i] = vrstica
        else:
            vrstica.append(prvi)
            vrstica.remove(prvi)
            slovar_krozisc[i] = vrstica
            prvi_po_popravku = vrstica[0]
            #print("popravljena vrstica:",vrstica)
        if min(vrstica) != vrstica[0]:
            vrstica.append(prvi_po_popravku)
            vrstica.remove(prvi_po_popravku)
            slovar_krozisc[i] = vrstica
        #print(i,":",vrstica)
    #print("slovar:",slovar_krozisc)
    datoteka.close()
    return slovar_krozisc


def mozna_pot(pot, zemljevid):
    izhodi = []
    krozisca = zemljevid
    for odcepi in krozisca.items():
        odcep, stevilke = odcepi
        #print("odcep:",odcep,"stevilke:",stevilke)
        if len(stevilke) == 1:
            izhodi.append(odcep)
    #print("IZHODI:",izhodi)
    #print("ostevilceni izhodi:",izhodi.count(stevilo for stevilo in izhodi))
    poiskano = True
    zaporedna = 0
    for pkljuc in pot:
        iskano = pot[zaporedna]
        zaporedna = zaporedna + 1
        #print("Rezultat:", pkljuc, '--', pot, '--', zemljevid[pkljuc], '--', iskano)
        if zaporedna < len(pot):
            # print(pot[zaporedna])
            if pot[zaporedna] in zemljevid[pkljuc]:
                #print("Najdeno:", pot[zaporedna], '-', zemljevid[pkljuc], poiskano)
                poiskano = True
            else:
                #print("Ni najdeno:", pot[zaporedna], '-', zemljevid[pkljuc], poiskano)
                poiskano = False
                #print("ni najdeno", poiskano)
                break
    for cesta in pot:
        ponovitev = []
        ponovno = False
        for v, w in zip(pot[:-1], pot[1:]):
            ponovitev.append((v,w))
            if v == w:
                ponovno = True
        #print("ponovitev:",ponovitev, ponovno)
        prvo_stevilo, zadnje_stevilo = pot[0], pot[-1]
        pot_brez_vhodov = pot
        pot_brez_vhodov.pop(0)
        pot_brez_vhodov.pop(-1)
        #print("potbrez",pot_brez_vhodov)
        #print(prvo_stevilo,zadnje_stevilo)
        for stevilo in pot_brez_vhodov:
            par = set(izhodi) & set(pot_brez_vhodov)
            #print("par:", par)
            #print("stevilo:",stevilo)
            if (prvo_stevilo in izhodi) and (zadnje_stevilo in izhodi) and par == set([]) and ponovno is False and poiskano is True:
                return True

def hamiltonova(pot,zemljevid):
    vsa_krozisca = []
    pot_je_mozna = mozna_pot(pot,zemljevid)
    #print("Pot:", pot, "---", pot_je_mozna)
    for kljuc, seznam in zemljevid.items():
        if len(seznam) > 1:
            vsa_krozisca.append(kljuc)
    #print("krozisca:",vsa_krozisca)
    if pot_je_mozna is True and len(pot) == len(vsa_krozisca):
        return True

def navodila(pot,zemljevid):
    navodilo = []
    zaporedna = 0
    for pkljuc in pot:
        zaporedna = zaporedna + 1
        if zaporedna < len(pot):
            if pot[zaporedna] in zemljevid[pkljuc]:
                navodilo.append(zemljevid[pkljuc].index(pot[zaporedna]))
                if navodilo[-1] == 0:
                    navodilo[-1] = pot[-1]
    navodilo.pop(0)
    #print("Pot:",pot)
    #print("Navodilo:",navodilo)
    return navodilo



