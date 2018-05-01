def shift(l, n):
     return l[n:] + l[:n]

def preberi(ime_datoteke):
    file = open(ime_datoteke, 'r')
    i = 1
    zemljevid = {}
    for line in file:
        list = line.split()
        list = [int(k) for k in list]
        for j in range (len(list)):
            if list[j] == min(list):
                list = shift(list, j)
        zemljevid[i] = list
        i+=1
    file.close()
    return zemljevid

def mozna_pot(pot, zemljevid):
    for i in range(len(pot)):
        if i != 0 and i != len(pot)-1:
            if  len(zemljevid[pot[i]]) < 2:
                return False
        if i == len(pot)-1 or i == 0:
            if len(zemljevid[pot[i]]) > 2:
                return False
        if pot[i] not in zemljevid.keys():
           return False
        else:
            if i < len(pot)-1:
                if pot[i+1] not in zemljevid[pot[i]]:
                    return False
                elif pot[i] == pot[i + 1]:
                    return False
    return True

def hamiltonova(pot, zemljevid):
    krozisca = []
    ze_uporabljeno_krozisce = []
    valid = 0
    used = 0
    for krozisce in zemljevid:
        if len(zemljevid[krozisce]) > 2:
            valid += 1
    for i in range(len(pot)):
        if mozna_pot(pot, zemljevid):
            krozisca.append(pot[i])
        else:
            return False
    for i in range(len(krozisca)):
        if krozisca[i] in zemljevid and len(zemljevid[krozisca[i]]) > 2:
            used += 1
            if krozisca[i] in ze_uporabljeno_krozisce:
                return False
            else:
                ze_uporabljeno_krozisce.append(krozisca[i])
    if used != valid:
        return False
    return True


