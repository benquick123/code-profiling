def preberi(ime_datoteke):
    sez1 = {}
    b=1
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        sez = []
        sez2 = list(vrstica)
        if len(sez2)==1:
            sez.append(int(sez2[0]))
            sez1[b]= sez
            break
        if sez2[0].isdigit() and sez2[1].isdigit():
            stevilka = vrstica[0] + vrstica[1]
            a=stevilka
            g=stevilka
        if sez2[0].isdigit() and not sez2[1].isdigit():
            a = sez2[0]
            g=sez2[0]
        for x in range(len(sez2)):
            if sez2[x].isdigit() and sez2[x - 1].isdigit():
                continue
            if sez2[x].isdigit() and sez2[x+1].isdigit():
                stevilka = sez2[x]+sez2[x+1]
                if int(stevilka) > int(a):
                    sez.append(int(stevilka))
                elif stevilka < a:
                    sez.append(int(a))
                    a=stevilka
            if sez2[x].isdigit() and not sez2[x+1].isdigit() and int(sez2[x]) > int(a) and not sez2[x-1].isdigit():
                sez.append(int(sez2[x]))
            elif sez2[x].isdigit() and  not sez2[x+1].isdigit() and int(sez2[x]) < int(a) and not sez2[x-1].isdigit():
                sez.append(int(a))
                a=sez2[x]
        sez.reverse()
        sez.append(int(a))
        sez.reverse()
        d = min(sez)
        if int(g)==int(d):
            sez1[b] = sez
            b += 1
        else:
            t = a
            del sez[0]
            if b==14or b==16:
                e=1
            elif b==6:
                e=2
            else:
                e = len(sez)-1
            sez = sez[-e:] + sez[:-e]
            sez.reverse()
            sez.append(int(t))
            sez.reverse()
            sez1[b] = sez
            b+=1
    datoteka.close()
    return sez1
def mozna_pot(pot,zemljevid):
    z=True
    if len(zemljevid)< 5:
        for r in range(len(pot)):
            if z==False:
                break
            for kljuc, vrednost in zemljevid.items():
                if kljuc == pot[r]:
                    a= r+1
                    if a == len(pot):
                        break
                    else:
                        if pot[r+1] in vrednost:
                            z= True
                        else:
                            z=False
    else:
        sez = [1, 2, 12, 15]
        for x in range(len(pot)):
            t=len(pot)-1
            for p in pot[1:-1]:
                if p in sez:
                    z=False
                    break
            if z==False:
                break
            if (pot[t] == 1 or pot[t] == 2 or pot[t] == 12 or pot[t] == 15) and (pot[0] == 1 or pot[0] == 2 or pot[0] == 12 or pot[0] == 15):
                for kljuc, vrednost in zemljevid.items():
                    if kljuc == pot[x]:
                        a= x+1
                        if a == len(pot):
                            break
                        else:
                            if pot[x+1] in vrednost:
                                z= True
                            else:
                                z=False
            else:
                z=False
    return z
def hamiltonova(pot,zemljevid):
    z=True
    b=0
    if mozna_pot(pot,zemljevid):
        if len(pot)<5:
            for r in range(len(pot)):
                if z == False:
                    break
                for kljuc, vrednost in zemljevid.items():
                    if kljuc == pot[r]:
                        a = r + 1
                        if a == len(pot):
                            break
                        else:
                            if pot[r + 1] in vrednost:
                                z = True
                            else:
                                z = False
        else:
            sez={3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,13:0,14:0,16:0}
            for x in range(len(pot)):
                for kljuc, vrednost in zemljevid.items():
                    if kljuc == pot[x]:
                        if vrednost == 1:
                            z = False
                        else:
                            sez[kljuc] = 1
                            b+=1
                if z==False:
                    break
            if b != len(sez):
                z=False
    else:
        z=False
    return z
