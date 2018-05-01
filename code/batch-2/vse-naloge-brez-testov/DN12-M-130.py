def preberi(ime_datoteke):
    datoteka = open(ime_datoteke)
    seznam = {}

    i = 1
    for vrstica in datoteka:

        s_vrstica = vrstica.strip()
        izvozi = (s_vrstica.split(" "))
        izvozi = [int(a) for a in izvozi]



        if len(izvozi) != 1:
            while 1 < 2:
                if izvozi[0] > izvozi[1]:
                    izvozi.append(izvozi.pop(0))
                else:
                    break

        seznam[i]= izvozi
        i +=1

    return seznam

def mozna_pot(pot, zemljevid):
    krizisca = zemljevid
    i= 0
    while i < (len(pot)-1):
        to_krizisce = pot[i]
        naslednje_krizisce = pot[i+1]
        if (to_krizisce in krizisca[naslednje_krizisce]) == False:
            return False
        elif to_krizisce == naslednje_krizisce:
            return False
        i +=1

    j= 1
    while j < (len(pot)-2):

        if len(krizisca[pot[j]]) == 1:

            return False
        j +=1

    if (len(krizisca[pot[0]]) == 1) and (len(krizisca[pot[len(pot)-1]]) == 1):
        return True
    else:
        return False


    return True

def hamiltonova(pot, zemljevid):
    i = 1
    seznam = []
    while i < (len(zemljevid)+1):
        if len((zemljevid[i]))  != 1:
            seznam.append(i)
        i +=1


    j = 0
    if mozna_pot(pot, zemljevid) == True:
        if len(seznam) == (len(pot)-2):
            return True
        else:
            return False














