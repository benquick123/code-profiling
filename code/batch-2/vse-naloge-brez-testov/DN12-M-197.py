from collections import defaultdict
def preberi(ime_datoteke):

    out_seznam = defaultdict()
    raw_seznam = open(ime_datoteke, "r")
    for index, line in enumerate(raw_seznam, start = 1):
        raw_seq = [int(i) for i in line.split()]
        ref_start = raw_seq.index(min(raw_seq))
        out_seznam[index] = raw_seq[ref_start:] + raw_seq[:ref_start]

    return (out_seznam)
    #vprašanje, ali prazne dead end node tudi damo not

#preberi("nav_sample")

def mozna_pot(pot, zemljevid):
    prehodnost = [True if pot[pot.index(tocka)+1] in zemljevid[tocka] else False for tocka in pot[:-1]]
    start_konec = [True if (len(zemljevid[pot[0]]) == 1)
                     else False] \
                  + [True if (len(zemljevid[pot[-1]]) == 1)
                     else False]
    self_zanka = [not all([x == y for x, y in zip(pot, pot[1:])])]
    dead_end = [len(zemljevid[node])!=1 for node in pot[1:-1]]

    #I guess da ne sme zaviti nazaj v node s samo eno povezavo
    #print(pot)
    #print(prehodnost, start_konec, self_zanka, dead_end)

    if all(prehodnost + start_konec + self_zanka + dead_end):
        return True
    else:
        return False

def navodila(pot, zemljevid):

    premiki = []
    for origin, point, target in zip(pot, pot[1:], pot[2:]):
       srch = {value: pos for pos, value in enumerate(zemljevid[point])}
       if len(zemljevid[point]) > 1:
           turns = (srch[target]-srch[origin])%len(zemljevid[point])
           premiki.append(turns)
    return (premiki)
    #for point, connections in zemljevid.items():


def hamiltonova(pot, zemljevid):
    ends_not_visited = len([(name, connections) for name, connections in zemljevid.items() if len(connections) == 1]) -2

    if mozna_pot(pot, zemljevid) and (len(set(pot)) == len(pot)) and len(pot) == (len(zemljevid) - ends_not_visited):
        return True
    else:
        return False

def prevozi(zacetek, navodila, zemljevid):
    outp = [zacetek] + [zemljevid[zacetek][0]]
    #print (outp)
    for move in (navodila):
        last = outp[-2]
        current = outp[-1]
        next_gen = zemljevid[current]

        candidates = {value: pos for pos, value in enumerate(next_gen)}
        new_pos = (candidates[last] + move) % len(candidates)
        select = [value for value, pos in candidates.items() if pos == new_pos]
        outp += select
    return outp

def sosedi(doslej, zemljevid):
    outp = set()
    for i in doslej:
        outp |=(set(zemljevid[i]))
    return outp - doslej

def razdalja(x, y, zemljevid):
    counter = 0
    start = {x}
    while y not in start:
        start |= sosedi(start, zemljevid)
        counter += 1
    return counter

def najkrajsa_navodila(x, y, zemljevid):
    from collections import defaultdict
    preiskane = []

    to_do = [[x]]

    if x == y:
        return "nič ni treba"
    while to_do:
        #print(preiskane, to_do)

        pot = to_do.pop(0)
        node = pot[-1]
        if node not in preiskane:
            sosedi = zemljevid[node]
            for sosed in sosedi:
                nova_pot = list(pot)
                nova_pot.append(sosed)
                to_do.append(nova_pot)

                if sosed == y:
                    return navodila(nova_pot, zemljevid)
            preiskane.append(node)


