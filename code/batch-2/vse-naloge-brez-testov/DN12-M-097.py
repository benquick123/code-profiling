#coding=utf-8
#from __future__ import unicode_literals




def preberi(ime_datoteke):
    i = 1
    slv = {}
    for vrstica in open(ime_datoteke) :
        vrstica = vrstica.strip()

        tab = vrstica.split(" ")
        tab = [int(i) for i in tab]

        najm = min(tab)
        while (najm != tab[0]) :
            tab.append(tab.pop(0))

        slv[i] = tab
        i += 1
    return slv


def mozna_pot(pot, zemljevid):
    koncna = []
    for k, tocka in zemljevid.items() :
        if len(tocka) == 1 :
            koncna.append(k)

    i = 0
    if pot[0] not in koncna or pot[len(pot)-1] not in koncna :
        return False

    for korak in pot :
        i += 1
        if korak in koncna :
            if i != 1 and i != len(pot) :
                return False
        if korak == pot[i-2] and i != 1:
            return False
        if i != 1 and korak not in zemljevid[pot[i-2]] :
            return False

    return True


def hamiltonova(pot, zemljevid):

    koncna = []
    for k, tocka in zemljevid.items() :
        if len(tocka) == 1 :
            koncna.append(k)

    if not mozna_pot(pot, zemljevid) :
        return False
    else :

        tab = []
        for k, tocka in zemljevid.items() :
            if k not in koncna :
                tab.append(k)

        for korak in pot :

            if korak in tab :
                tab.pop(tab.index(korak))
            else :
                if korak not in koncna :
                    return False


        if len(tab) == 0 :
            return True
        else :
            return False














