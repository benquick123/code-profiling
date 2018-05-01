def preberi(ime_datoteke):
    a = dict ()
    b = dict ()
    with open (ime_datoteke) as g:
        vrstica = g.readline ()
        count = 1
        while vrstica:
            a[count] = []
            b[count] = []
            for e in vrstica.strip ().split():
                e = int ( e )
                a[count].append ( e )
                for d in a.items ():
                    e, k = d
                    s = []
                    x = 1000000
                    for i in k:
                        if i < x:
                            x = i
                    index = k.index ( x )
                    for element in k[index:]:
                        s.append ( element )
                    for e in k[0:index]:
                        s.append ( e )
                b[count] = s

            vrstica = g.readline ()
            count += 1
    return b


def mozna_pot(pot, zemljevid):
    zk = []
    for d in zemljevid.items ():
        e, k = d
        if len ( k ) == 1:
            zk.append ( e )
    i = 0
    if pot[i] in zk and pot[-1] in zk:
        i += 1
        while (i < len ( pot ) - 1):
            if pot[i] not in zk:
                if pot[i] != pot[i + 1]:
                    i += 1
                else:
                    return False
                    break
            else:
                return False
                break
        for i in range ( 1, len ( pot ) ):
            if pot[i] not in zemljevid[pot[i - 1]]:
                return False
        return True
    else:
        return False

def hamiltonova(pot, zemljevid):
    zk = []
    for i in zemljevid:
        if len(zemljevid[i]) == 1:
            zk.append(i)


    if len(pot) > 1:
        if pot[0] not in zk:
            return False
        if pot[-1] not in zk:
            return False


    if len(zemljevid)-len(zk)+2 != len(pot):
        return False


    for i in range(0, len(pot)):
        for j in range(i, len(pot)):
            if i != j:
                if pot[i] == pot[j]:
                    return False

    
    for i in range(1, len(pot)):
        if pot[i] not in zemljevid[pot[i-1]]:
            return False
    return True





