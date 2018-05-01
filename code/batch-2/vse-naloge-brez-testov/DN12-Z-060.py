def obrniNiz(niz):
    najmanjsi = niz[0]
    najmanjsi_index = 0
    for i in range(1, len(niz)):
        if najmanjsi > niz[i]:
            najmanjsi = niz[i]
            najmanjsi_index = i
    return niz[najmanjsi_index:]+niz[:najmanjsi_index]

def preberi(ime_datoteke):
    stevec = 1
    naredi_slovar = {}
    for vrstice in open(ime_datoteke):
        vrstice = vrstice.strip()
        nizek = []
        for stevilo_x in vrstice.split():
            nizek.append(int(stevilo_x))
        naredi_slovar[stevec] = obrniNiz(nizek)
        stevec += 1
    return naredi_slovar

def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1: #ne začne se z končno povezavo
        return False
    if len(zemljevid[pot[-1]]) != 1: #ne konča se z končno povezavo
        return False
    # vmes ni končnih povezav
    vmesna_pot = pot[1:-1] # gledamo samo vmesno pot...
    for item in range(0, len(vmesna_pot)):
        if len(zemljevid[vmesna_pot[item]]) == 1: #vmes imamo končno točko
            return False
    # nobeno krožišče se ne ponovi - odstrani zaporedne podvojene
    for item in range(1, len(pot)):
        if(pot[item] == pot[item-1]):
            return False
    # krožišča so na poti dejansko povezana
    for item in range(1, len(pot)):
        if pot[item] not in zemljevid[pot[item-1]]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    #duplicate dict dict2 = dict(dict1)
    moj_zemljevid = dict(zemljevid)
    if not mozna_pot(pot, zemljevid):
        return False
    for item in range(0, len(pot)):
        if not pot[item] in moj_zemljevid: #smo že šli čez krožišče - ponavljanje, pazimo zaradi delete
            return False
        else:
            del moj_zemljevid[pot[item]]
    for seznam in moj_zemljevid:
        if len(moj_zemljevid[seznam]) != 1:
            return False
    return True


# Za oceno 7:
def navodila(pot, zemljevid):
    seznam = []
    for item in range(2, len(pot)): #potujemo po poti, gledamo trojke (namig), zato začnemo z 2
        seznam.append((zemljevid[pot[item-1]].index(pot[item]) - zemljevid[pot[item-1]].index(pot[item-2])) % len(zemljevid[pot[item-1]]))
    return seznam

