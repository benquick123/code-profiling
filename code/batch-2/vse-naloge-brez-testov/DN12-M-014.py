def preberi(ime_datoteke):
    seznam = ()
    slovar = {}
    i = 1
    for e in open(ime_datoteke):
        seznam = (e.strip().split())
        seznam = [int(x) for x in seznam]
        a = seznam.index(min(seznam))
        seznam = seznam[a:] + seznam[0:a]
        slovar[i] = seznam
        i += 1
    return slovar



def mozna_pot(pot, zemljevid):
    mapa = zemljevid
    da = 0
    i = 0
    for e in pot[1:]:
        prvi = pot[i]
        if e in mapa[prvi] and len(mapa[pot[0]]) == 1 and len(mapa[pot[-1]]) == 1 and pot[i] != e:
            da += 1
        i = i + 1
    for j in pot[1: -1]:
        if len(mapa[j]) <= 1:
            da -= 1
    if len(pot) - 1 == da:
        return True
    else:
        return False



def hamiltonova(pot, zemljevid):
    mapa = zemljevid
    i = 0
    seznam = []
    vse = 0
    da = 0
    ne = 0
    for e in pot[1:]:
        prvi = pot[i]
        if mozna_pot(pot, mapa) is True and prvi != e:
            da += 1
            vse += 1
        else:
            ne += 1
        i = i + 1
    if len(pot) - 1 == da and vse == 13 or vse == 3:
        return True
    else:
        return False


