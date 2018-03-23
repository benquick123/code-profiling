def besedilo(tvit):
    tvit = tvit.split(" ", 1)

    return tvit[1]

def besedilo2(tvit):
    tvit = tvit.split(" ", 1)

    return tvit

from string import punctuation
def izloci_besedo(beseda):

    beseda = beseda.lstrip(punctuation)
    beseda = beseda.rstrip(punctuation)

    return beseda

def zadnji_tvit(tviti):
    slovar = {}

    for x in tviti:
        x = besedilo2(x)

        if izloci_besedo(x[0]) not in slovar:
            slovar[izloci_besedo(x[0])] = []

        slovar[izloci_besedo(x[0])] = (x[1])

    return slovar

def prvi_tvit(tviti):
    slovar = {}

    for x in tviti:
        x = besedilo2(x)

        if izloci_besedo(x[0]) not in slovar:
            slovar[izloci_besedo(x[0])] = []
            slovar[izloci_besedo(x[0])] = (x[1])


    return slovar

from collections import Counter
def prestej_tvite(tviti):

    slovar = {}

    for x in tviti:
        stevec = 0
        x = x.split(" ", 1)

        if x[0] not in slovar:
            slovar[izloci_besedo(x[0])] = []
            for y in tviti:
                if x[0] in y:
                    stevec += 1
            slovar[izloci_besedo(x[0])] = stevec

    return slovar

def omembe(tviti):
    slovar = {}

    for x in tviti:
        y = x.split(" ", 1)

        if izloci_besedo(y[0]) not in slovar:
            slovar[izloci_besedo(y[0])] = []

        x = x.split()

        for i in x:
            if "@" in i:
                slovar[izloci_besedo(x[0])] += [izloci_besedo(i)]

    return slovar

def neomembe(ime, x):

    seznam = []

    seznam = list(x.keys())
    unikati = []

    for i in seznam:
        if i not in x[ime]:
            unikati.append(i)

    unikati.remove(ime)

    return  unikati

### DODATNA ###

def se_poznata(ime1, ime2, tviti):

    if ime2 in tviti.get(ime1, []) or ime1 in tviti.get(ime2, []):
        return True
    else:
        return False

import re
def hashtagi(tviti):
    slovar = {}

    for x in tviti:
        y = x.split("#")

        if len(y) < 3:
            if y[1].replace(" ", "") not in slovar:
                if "?" in y[1].replace(" ", ""):
                    y = y[1].split("?")
                    slovar[izloci_besedo(y[0].replace(" ", ""))] = []
                    x = x.split(":")
                    slovar[izloci_besedo(y[0])] += [(x[0])]

                    continue

                slovar[izloci_besedo(y[1].replace(" ", ""))] = []

            x = x.split(":")
            slovar[izloci_besedo(y[1])] += [(x[0])]
            slovar[izloci_besedo(y[1])] = sorted(slovar[izloci_besedo(y[1])])

        if len(y) >= 3:
            if y[2].replace(" ", "") not in slovar:
                slovar[izloci_besedo(y[2].replace(" ", ""))] = []

            x = x.split(":")
            slovar[izloci_besedo(y[2])] += [(x[0])]

            if y[1].replace(" ", "") not in slovar:
                slovar[izloci_besedo(y[1].replace(" ", ""))] = []

            slovar[izloci_besedo(y[1]).replace(" ", "")] += [(x[0])]
            slovar[izloci_besedo(y[1].replace(" ", ""))] = sorted(slovar[izloci_besedo(y[1].replace(" ", ""))])

    return slovar





######################################
