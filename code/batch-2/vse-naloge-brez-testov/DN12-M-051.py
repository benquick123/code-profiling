def preberi(ime_datoteke):
    datoteka = open(ime_datoteke,"r")
    sosednje = {}
    for i,vrstica in enumerate(datoteka):
        s = []
        for izvoz in vrstica.strip().split():
            s.append(int(izvoz))
        s *= 2
        for a,stev in enumerate(s):
            if stev == min(s):
                s = s[a:a+(len(s)//2)]
                break
        sosednje[i+1] = s
    return sosednje

def mozna_pot(pot, zemljevid):
    ne_vmes_ven = len(pot) - 2 == sum([True for krozisce in pot if len(zemljevid[krozisce]) != 1])
    if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1:
        if ne_vmes_ven:
            for premik1,premik2 in zip(pot,pot[1:]):
                if premik2 in zemljevid[premik1] and premik1 != premik2:
                    continue
                else:
                    return False
            return True
    return False

def hamiltonova(pot, zemljevid):
    s = []
    for p in pot:
        if p not in s:
            s.append(p)
        else:
            return False
    vsa_krozisca = {krozisce for krozisce in zemljevid.keys() if len(zemljevid[krozisce]) > 1}
    pot1 = {a for a in pot}
    return vsa_krozisca <= pot1 and mozna_pot(pot,zemljevid)

def navodila(pot, zemljevid):
    odcepi = []
    for premik1,premik2,premik3 in zip(pot,pot[1:],pot[2:]):
        urejeno = zemljevid[premik2] *2
        for i,b in enumerate(urejeno):
            if b == premik1:
                urejeno = urejeno[i:len(urejeno)//2 + i]
                break

        for i,a in enumerate(urejeno):
            if a == premik3:
                if i:
                    odcepi.append(i)
                    break
    if odcepi:
        return odcepi
    return [0]

def prevozi(zacetek, navodila, zemljevid):
    krozisca = [zacetek,zemljevid[zacetek][0]]
    trenutno = zemljevid[zacetek][0]
    stevec = 0
    for navodilo in navodila:
        od = zemljevid[trenutno] * 2
        for i,b in enumerate(od):
            if b == krozisca[stevec]:
                od = od[i:len(od)//2 + i]
                stevec += 1
                break
        for i,odcep in enumerate(od):
            if i == navodilo:
                krozisca.append(odcep)
                trenutno = odcep
                break
    return krozisca

def sosedi(doslej, zemljevid):
    povezane = set()
    for krozisce in doslej:
        for a in zemljevid[krozisce]:
            if a not in doslej:
                povezane.add(a)
    return povezane

def razdalja(x, y, zemljevid):
    stevec = 0
    sosedje = {x}
    x = {x}
    while y not in sosedje:
        for sosed in sosedi(x,zemljevid):
            sosedje.add(sosed)
        x = sosedi(x, zemljevid)
        stevec += 1
    return stevec












