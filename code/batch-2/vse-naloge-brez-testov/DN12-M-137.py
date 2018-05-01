def preberi(ime_datoteke):
    s = {}
    dat = open(ime_datoteke)
    st = 1
    for i in dat:
        i = i.rstrip()
        i = i.split(" ")
        seznam = []
        for a in i:
            a = int(a)
            seznam.append(a)
        najmanj = min(seznam)
        st_seznama = 0
        seznam1 = seznam
        for b in seznam1:
            if b != najmanj:
                seznam = seznam[1:] + seznam[:1]
            else:
                break
        s[st] = seznam
        st += 1
    return s


def mozna_pot(pot, zemljevid):
    s = []
    prvi = pot[0]
    zadnji = pot[-1]
    dolzina = len(pot)
    stevec = 0
    for i in pot:
        if len(zemljevid[prvi]) != 1:
            return False
        if len(zemljevid[zadnji]) != 1:
            return False

        if stevec > 1 and stevec < dolzina -1:
            if len(zemljevid[i]) < 2:
                return False

        if stevec < dolzina - 1:
            if pot[stevec] == pot[stevec+1]:
                return False

        if stevec < dolzina -1:
            if pot[stevec + 1] not in zemljevid[i]:
                return False
        stevec += 1
    return True

def hamiltonova(pot, zemljevid):
    s = []
    s1 = []
    for b in zemljevid:
        if len(zemljevid[b]) != 1:
            s.append(b)

    for c in pot:
        if len(zemljevid[c]) != 1:
           s1.append(c)
    s_s = s.sort()
    s1_s = s1.sort()
    if s != s1:
        return False
    for i in s:
        st = 0
        for a in s:
            if i == a:
                st += 1
        if st > 1:
            break
    if mozna_pot(pot,zemljevid) and st < 2:
        return True
    else:
        return False

def navodila(pot, zemljevid):
    s = []
    st = 0
    for i in pot:
        if len(zemljevid[i]) == 1:
            st += 1
            continue
        else:
            stevc = 0
            for a in zemljevid[i]:
                if a == pot[st + 1]:
                    prvi = zemljevid[i][0]
                    if len(zemljevid[prvi]) == 1:
                        stevc -= 0
                    s.append(stevc)
                    break
                stevc += 1
        st += 1
    return s




