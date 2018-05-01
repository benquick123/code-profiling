from math import *

def preberi(ime_datoteke):
    slovar = {}
    datoteka = open(ime_datoteke)
    line = 1
    for el in datoteka:
        temp = []
        seznam = el.strip().split(" ")
        seznam = [int(y) for y in seznam]
        min = seznam[0]
        min_index = 0
        index = 1
        for x in seznam[1:]:
            if x < min:
                min = x
                min_index = index
            index += 1
        temp += seznam[min_index:]
        temp += seznam[:min_index]
        slovar[line] = temp
        line += 1
    datoteka.close()
    return slovar


def mozna_pot(pot, zemljevid):
    temp = []
    for krozisce, povezave in zemljevid.items():
        if len(povezave) == 1:
            temp.append(krozisce)
    if not pot[0] in temp or not pot[len(pot)-1] in temp:
        return False
    for el in zip(pot, pot[1:]):
        if not el[1] in zemljevid[el[0]] or len(zemljevid[el[0]]) == 1 and pot.index(el[0]) not in [0, len(pot)-1]:
            return False
    return True


def hamiltonova(pot, zemljevid):
    temp = []
    for krozisce, povezave in zemljevid.items():
        if len(povezave) == 1:
            temp.append(krozisce)
    if not pot[0] in temp or not pot[len(pot) - 1] in temp:
        return False
    for el in zip(pot, pot[1:]):
        if not el[1] in zemljevid[el[0]] or len(zemljevid[el[0]]) == 1 and pot.index(el[0]) not in [0, len(pot) - 1]:
            return False
    for el in pot:
        if el in pot[:pot.index(el)] or el in pot[pot.index(el)+1:]:
            return False
    temp = []
    for krozisce, povezave in zemljevid.items():
        if len(povezave) == 1:
            temp.append(krozisce)
    if mozna_pot(pot, zemljevid) and len(pot) == len(zemljevid.keys())-len(temp)+2:
        return True
    return False


def navodila(pot, zemljevid):
    seznam = []
    for prejsnji, trenutni, naslednji in zip(pot, pot[1:], pot[2:]):
        if pot[1:]:
            if zemljevid[trenutni].index(prejsnji) < zemljevid[trenutni].index(naslednji):
                seznam.append(zemljevid[trenutni].index(naslednji) - zemljevid[trenutni].index(prejsnji))
            else:
                seznam.append((zemljevid[trenutni].index(naslednji) - (zemljevid[trenutni].index(prejsnji))) % (len(zemljevid[trenutni])))
    return seznam


def prevozi(zacetek, navodila, zemljevid):
    seznam = [zacetek]
    prejsnji = zacetek
    for z, x in zemljevid.items():
        if len(x) == 1 and zacetek == z:
            trenutni = x[0]
            break
    seznam.append(trenutni)
    for el in navodila:
        temp = trenutni
        if zemljevid[trenutni].index(prejsnji) + el < len(zemljevid[prejsnji])-2:
            trenutni = zemljevid[trenutni][zemljevid[trenutni].index(prejsnji) + el]
            seznam.append(trenutni)
        else:
            tmp = zemljevid[trenutni][zemljevid[trenutni].index(prejsnji):]+zemljevid[trenutni][:zemljevid[trenutni].index(prejsnji)]
            trenutni = tmp[tmp.index(prejsnji) + el]
            seznam.append(trenutni)
        prejsnji = temp
    return seznam


def sosedi(doslej, zemljevid):
    x = set()
    for el in doslej:
        for y in zemljevid[el]:
            if y not in doslej:
                x.add(y)
    return x


def razdalja(x, y, zemljevid):
    count = 0
    z = {x}
    doslej = {x}
    while True:
        z = z | sosedi(doslej, zemljevid)
        count += 1
        doslej = doslej | sosedi(doslej, zemljevid)
        if y in doslej:
            break
    return count





