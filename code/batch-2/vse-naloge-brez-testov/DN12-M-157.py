import collections
def preberi(ime_datoteke):
    s = {}
    c = 0
    z = 0
    d = open(ime_datoteke)
    d = d.readlines()
    for let in d:
        c += 1
    for num in range(1,c+1):
        s[num] = []
    for key in s:
        for num in range(1,c+1):
            if key == num:
                s[num] += d[num-1].split(' ')
    for key,path in s.items():
        y = []
        for i in path:
            y.append(int(i))
            if i[-1] == '\n':
                i = i.replace('\n','')
                path = path[:-1] + [i]
                s[key] = path
        while y[0] != min(y):
            x = y.pop(0)
            y.append(x)
        s[key] = y
    return s

def mozna_pot(pot, zemljevid):
    z = zemljevid
    zac = pot[0]
    kon = pot[-1]
    sre = pot[1:-1]
    st_pon = -1

    if len(z[zac]) > 1:
        return False
    if len(z[kon]) > 1:
        return False
    for s in sre:
        if len(z[s]) < 2:
            return False
    for kroz in pot:
        st_pon += 1
        trenutno = z[pot[st_pon]]
        if st_pon+1 == len(pot):
            continue
        naslednje = pot[st_pon+1]
        if naslednje not in trenutno:
            return False
    else:
        return True

def hamiltonova(pot, zemljevid):
    z = zemljevid
    l = []
    r = []
    if mozna_pot(pot, zemljevid) == True:
        for kroz in pot:
            if kroz in l:
                return False
            else:
                l.append(kroz)
        for key in z:
            if len(z[key]) > 1:
                r.append(key)
        for num in l[1:-1]:
            for n in r:
                if n not in l:
                    return False

        return True



