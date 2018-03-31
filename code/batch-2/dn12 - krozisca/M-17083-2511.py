def preberi(ime_datoteke):
    file = open(ime_datoteke)
    s = {}
    st = 1
    for vrstica in file:
        izvozi = vrstica.strip().split(" ")
        s[st] = izvozi
        st += 1

    for krozisce in s:
        najmanjsi = min(int(izvoz) for izvoz in s[krozisce])
        d = len(s[krozisce])
        temp = [None] * d
        i = 0
        index = -1
        for izvoz in s[krozisce]:
            if najmanjsi == int(izvoz):
                index = i
                break
            i += 1
        x = 0
        j = 0
        for izvoz in s[krozisce]:
            if j >= index:
                temp[x] = int(izvoz)
                x += 1
            j += 1
        j = 0
        for izvoz in s[krozisce]:
            if j == index:
                break
            if j < index:
                temp[x] = int(izvoz)
                x += 1
            j += 1
        s[krozisce] = temp
    return s

def mozna_pot(pot, zemljevid):
    d = len(pot)
    if len(zemljevid[pot[0]]) > 1 or len(zemljevid[pot[d - 1]]) > 1:
        return False
    for i in range(1, d - 1):
        if len(zemljevid[pot[i]]) < 2:
            return False
    for i in range(0, d - 1):
        if pot[i] == pot[i + 1]:
            return False
        if pot[i + 1] not in zemljevid[pot[i]]:
            return False
    return True

def hamiltonova(pot, zemljevid):
    if not mozna_pot(pot, zemljevid):
        return False
    d = len(pot)
    s = []
    x = 0
    for krozisce in pot:
        if len(zemljevid[krozisce]) > 1:
            if krozisce not in s:
                s.append(krozisce)
            else:
                return False
    for krozisce in zemljevid:
        if len(zemljevid[krozisce]) > 1:
            x += 1
    if len(s) == x:
        return True
    else:
        return False