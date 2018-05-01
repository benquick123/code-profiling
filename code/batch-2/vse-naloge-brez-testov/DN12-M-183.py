def preberi(ime_datoteke):
    slovar = {}
    idx = 1
    file = open(ime_datoteke)
    for line in file:
        seznam_izvoz = []
        for izvoz in line.split():
            seznam_izvoz.append(int(izvoz))
        seznam_izvoz_sorted = []

        firstIdx = 1
        for izvoz in seznam_izvoz:
            if izvoz == min(seznam_izvoz):
                seznam_izvoz_sorted.append(izvoz)
                break
            firstIdx+=1

        for currIdx in range(firstIdx, len(seznam_izvoz)):
            seznam_izvoz_sorted.append(seznam_izvoz.__getitem__(currIdx))

        for currIdx in range(0, firstIdx-1):
            seznam_izvoz_sorted.append(seznam_izvoz.__getitem__(currIdx))

        slovar[idx] = seznam_izvoz_sorted
        idx += 1

    file.close()

    return slovar

def mozna_pot(pot, zemljevid):
    idx = 0
    prevK = -1
    for currK in pot:

        if idx == 0 and zemljevid[currK].__len__() > 1:
            return False

        if idx == pot.__len__()-1 and zemljevid[currK].__len__() > 1:
            return False

        if prevK == currK:
            return False

        if prevK > -1 and not zemljevid[prevK].__contains__(currK):
            return False

        if zemljevid[currK].__len__() == 1 and idx > 0 and idx < pot.__len__()-1:
            return False

        prevK = currK
        idx += 1

    return True

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid) == False:
        return False

    duplicates = []
    for currK in pot:
        if duplicates.__contains__(currK):
            return False
        duplicates.append(currK)


    for currK in zemljevid.keys():
        if not duplicates.__contains__(currK) and zemljevid[currK].__len__() > 1:
            return False

    return True

def navodila(pot, zemljevid):
    navodila_sez = []

    prevK = -1
    nextK = -1
    for idx in range(0, len(pot)):

        currK = pot[idx]

        if idx+1 < len(pot):
            nextK = pot[idx+1]

        if zemljevid[currK].__len__() == 1:
            prevK = currK
            continue

        diff = zemljevid[currK].index(nextK) - zemljevid[currK].index(prevK)
        navodila_sez.append(diff % zemljevid[currK].__len__())
        prevK = currK


    return navodila_sez


def prevozi(zacetek, navodila, zemljevid):
    seznam_kroz = [zacetek, zemljevid[zacetek][0]]

    currK = zemljevid[zacetek][0]
    prevIn = zemljevid[currK].index(zacetek)

    for izv in navodila:

        prevK = currK

        nextIdx = prevIn+izv
        if nextIdx >= zemljevid[prevK].__len__():
            nextIdx -= zemljevid[prevK].__len__()

        currK = zemljevid[prevK][nextIdx]
        prevIn = zemljevid[currK].index(prevK)

        seznam_kroz.append(currK)

    return seznam_kroz



def sosedi(doslej, zemljevid):
    sosedi_mnoz = set()

    for currK in doslej:
        for currSos in zemljevid[currK]:
            if not sosedi_mnoz.__contains__(currSos):
                sosedi_mnoz.add(currSos)

    for currK in doslej:
        if sosedi_mnoz.__contains__(currK):
            sosedi_mnoz.remove(currK)


    return sosedi_mnoz

def razdalja(x, y, zemljevid):
    currLen = 0
    if sosedi([x], zemljevid).__contains__(y):
        return currLen+1

    for x2 in sosedi([x], zemljevid):
        currLen+=razdalja(x2, y, zemljevid)

    return currLen


