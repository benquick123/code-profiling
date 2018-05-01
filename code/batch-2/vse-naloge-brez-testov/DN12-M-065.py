def preberi(ime_datoteke):
    krozisca = {}

    with open(ime_datoteke, 'r') as datoteka:
        for index, vrstica in enumerate(datoteka.readlines()):
            index += 1
            elementi = [int(element) for element in vrstica.strip().split(' ')]

            krozisca[index] = elementi

            if len(elementi) > 1:
                minimum_element = min(elementi)

                if minimum_element != krozisca[index][0]:
                    minimum_element_index = krozisca[index].index(minimum_element)

                    krozisca[index].remove(minimum_element)
                    krozisca[index] = [minimum_element] + krozisca[index][minimum_element_index:] + krozisca[index][:minimum_element_index]

    return krozisca


def mozna_pot(pot, zemljevid):
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False

    for k in range(len(pot) - 1):
        if pot[k + 1] not in zemljevid[pot[k]] or pot[k] == pot[k + 1] or (len(zemljevid[pot[k + 1]]) == 1 and pot[k+1] != pot[-1]):
            return False

    return True


def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False

    x = {}

    for k, v in zemljevid.items():
        if len(v) > 1 and k not in x:
            x[k] = 0

    for p in pot[1:-1]:
        x[p] += 1

    for k, v in x.items():
        if v != 1:
            return False

    return True

def navodila(pot, zemljevid):
    return [(zemljevid[pot[index + 1]].index(pot[index + 2]) - zemljevid[pot[index + 1]].index(pot[index])) % len(zemljevid[pot[index + 1]]) for index in range(0, len(pot) - 2)]

def prevozi(zacetek, navodila, zemljevid):
    path = [zacetek]
    previous_node = zacetek
    current_node = zemljevid[zacetek][0]

    path.append(current_node)

    for navodilo in navodila:
        previous_node_index = zemljevid[current_node].index(previous_node)
        next_node_index = (previous_node_index + navodilo) % len(zemljevid[current_node])

        next_node = zemljevid[current_node][next_node_index]

        path.append(next_node)

        previous_node = current_node
        current_node = next_node

    return path