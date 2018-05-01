
def preberi(ime_datoteke):
    seznam = []
    seznam_krozisc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for vrsta in open(ime_datoteke):
        a = vrsta.split()
        b = [int(x) for x in a]
        seznam.append(b)
    for i in seznam:
        if i[0] == min(i):
            pass
        else:
            while i[0] is not min(i):
                i.append(i[0])
                del i[0]
                if i[0] is min(i):
                    break
    knjiznica = dict(zip(seznam_krozisc, seznam))

    return knjiznica


def mozna_pot(pot, zemljevid):

    ce_je = 0
    ne_vsebuje_podvojitve = 0
    for i in pot[:-1]:
        b = pot.index(i)
        print(b)
        if pot[b] in zemljevid[pot[b+1]]:
            ce_je = True
        else:
            ce_je = False
            break
    if 1 == len(zemljevid[pot[0]]) and 1 == len(zemljevid[pot[-1]]):
        zacne_konca = True
    else:
        zacne_konca = False
    vmes_izhod = True
    stevec = 1
    while stevec < (len(pot) -2):
        if len(zemljevid[pot[stevec]]) == 1:
            vmes_izhod = False
        stevec += 1
    for x,y in enumerate(pot[:-1]):
        if y == pot[x+1]:
            ne_vsebuje_podvojitve = False
        else:
            ne_vsebuje_podvojitve = True
    if zacne_konca and vmes_izhod and ne_vsebuje_podvojitve and ce_je == True:
        return True
    else:
        return False



def hamiltonova(pot, zemljevid):
    ali_bo_slo = 0
    ali_ne_bo_slo = 0
    stevec1 = 1
    seznam = []
    while stevec1 < (len(zemljevid)+1):
        if len((zemljevid[stevec1])) != 1:
            seznam.append(stevec1)
        stevec1 += 1
    if mozna_pot(pot, zemljevid) == True:
        if len(seznam) == (len(pot) - 2):
            ali_bo_slo = True
        else:
            ali_ne_bo_slo = False
    if ali_bo_slo == True:
        return True
    else:
        return False

