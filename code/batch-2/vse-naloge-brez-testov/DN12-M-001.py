from collections import *
def preberi(ime_datoteke):
    file = open(ime_datoteke)
    dictionary = defaultdict(list)
    line_counter = 1
    for line in file:
        line = line.replace("\n", "")
        clean_line = map(int, line.split(" "))
        dictionary[line_counter] += clean_line
        line_counter += 1
    for key, value in dictionary.items():
        for a in value:
            if value[0] > a:
                value.insert(0, value.pop())
    file.close()
    return(dictionary)

def mozna_pot(pot, zemljevid):
    a = None
    exits = []
    for key, value in zemljevid.items():
        if len(value) == 1:
            exits.append(key)
    for (x, y) in zip(pot, pot[1::]):
        for b in exits:
            if pot[0] in exits and pot[-1] in exits:
                if b not in pot[1::]:
                    if y in zemljevid[x]:
                        a = True
                    if y not in zemljevid[x]:
                        return False
                elif b in pot[1:-1]:
                    return False
            elif pot[0] not in exits or pot[-1] not in exits:
                return False
    return a

def hamiltonova(pot, zemljevid):
    a = None
    exits = []
    roundabout = []
    checked = []
    for key, value in zemljevid.items():
        if len(value) == 1:
            exits.append(key)
        else:
            roundabout.append(key)
    for c in pot:
        for b in roundabout:
            if b not in pot:
                return False
        if c in checked:
            return False
        if c not in zemljevid.keys():
            return False
        if c in zemljevid.keys():
            a = mozna_pot(pot, zemljevid)
        checked.append(c)
    return a



