def preberi(ime_datoteke):
    tekst = open(ime_datoteke)
    st_v = 1
    slovar = {}
    for vrstica in tekst:
        mnozica = vrstica.split(' ')
        mnozica = [int(i) for i in mnozica]
        while mnozica[0] != min(mnozica):
            rez = mnozica[0]
            for i in range(1, len(mnozica)):
                mnozica[i - 1] = mnozica[i]
            mnozica[len(mnozica) - 1] = rez

        slovar[st_v] = mnozica
        st_v += 1
    tekst.close()
    return slovar


def mozna_pot(pot, zemljevid):
    ## prva in zadnja imata samo 1 krožišče ##
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[len(pot) - 1]]) != 1:
        return False

    ## vmesne nimajo samo 1 krožišča ##
    for i in range(1, len(pot) - 1):
        if len(zemljevid[pot[i]]) == 1:
            return False

    for i in range(1, len(pot)):
        ## točke se ne ponavljajo ##
        if pot[i] == pot[i] - 1:
            return False
        ## križišča so povezana ##
        if pot[i] not in zemljevid[pot[i - 1]]:
            return False

    return True


def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):
        for i in range(len(pot)):
            if pot[i] in pot[i + 1:]:
                return False
        if len(pot) != len([x for x in zemljevid if len(zemljevid[x]) != 1]) + 2:
            return False
        return True
    return False


import os

