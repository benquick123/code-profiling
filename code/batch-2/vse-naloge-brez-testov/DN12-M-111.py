def ocisti(s):
    s1 = []
    i = 0
    a = len(s)
    while i < a:
        if s[i] not in s1:
            s1.append(s[i])
            i+=1
        else:
            del s[i]
            a-=1

def unikati(s):
    prazen_seznam = []

    for i in s:                         # for i in s pomeni, da se i premika po vrednostih seznama s, NE PO INDEKSIH!
        if i not in prazen_seznam:
            prazen_seznam.append(i)

    return prazen_seznam

def preberi(ime_datoteke):
    prazen_slovar = {}
    stevec_vrst = 1
    prazen_seznam = []

    #Najprej ustvarim slovar zemljevida, kjer je ključ krožišče in vsebina ključa njegove povezave oz. sosednja krožišča
    for vrsta in open(ime_datoteke): #vsaka vrsta naslednje krožišče
        for kroz in vrsta.split():
            if kroz == " ":
                continue
            else: prazen_seznam.append(int(kroz))
        prazen_slovar[stevec_vrst] = prazen_seznam
        prazen_seznam = []
        stevec_vrst+=1

    #Sprehdim se po ustvarjenem slovarju in dam minimum na začetek, vsa prejšnja krožišča pred najmanjšo številko najprej zbrišem in nato na novo v isti seznam dodam
    for krozisce, povezave in prazen_slovar.items():
        for povezava in povezave:
            strazar = povezave[0] #strazar je torej prvi sosed sosedov
            if strazar != min(povezave): #ker je strazar na prvem mestu torej mi je v pomoc pri iskanju najmanjšega števila, če ni enak minimumu,
                # ga brišem in na novo dodajam v seznam toliko časa, dokler straza ni enak minimumu
                povezave.remove(strazar)
                povezave.append(strazar)
            else: #ko je strazar enak minimumu, spremenjen seznam sosedov določim krožišču
                prazen_slovar[krozisce] = povezave
                break

    return prazen_slovar

def mozna_pot(pot, zemljevid):
    izhodi = []
    index = 1

    #Po pogledu v teste opazim da testi vzamejo tudi nek drugi nov zemljevid, torej samo določitev izhodov [1, 2, 12, 15] ni pravilno. Moram jih najti. Najdem jih tako da preverim tiste kljuce ki imajo dolzino seznama ena,
    # kar pomeni da imajo samo eno povezavo. To so izhodne povezave:
    for krizisce1, povezave1 in zemljevid.items():
        if len(povezave1) == 1:
            izhodi.append(krizisce1)

    del_poti_povezave = []

    for del_poti in pot:
        naslednji_del_poti = pot[index]
        index += 1 #z njim bom lazje dostopal do naslednjega krozisca in preverjal ali je v seznamu sosedov trenutnega krozisca
        trenutno = del_poti

        for krozisce, povezava in zemljevid.items():
            if pot[0] in izhodi and pot[-1] in izhodi: #začetek in konec s končno povezavo
                if naslednji_del_poti in zemljevid[del_poti]: #ali je naslednje krožišče v seznamu sosedov trenutnega krožišča
                    if naslednji_del_poti == pot[-1]: #ali je naslednje krožišče enako koncu
                        if naslednji_del_poti in izhodi: #če se končna
                            return True
                        else:
                            return False
                    if naslednji_del_poti in izhodi: #ali je vmes končna povezava
                        return False
                else:
                    return False
            else:
                return False

def hamiltonova(pot, zemljevid):
    izhodi = []
    vsa = []
    vsa1 = []

    for krizisce1, povezave1 in zemljevid.items():
        if len(povezave1) == 1:
            izhodi.append(krizisce1)
        if len(povezave1) > 1:
           for povezava in povezave1:
                if len(povezave1) > 1 and povezava not in izhodi and len(zemljevid[povezava])>1:
                    vsa.append(povezava)

    ocisti(vsa) #uporabil sem funkcijo iz unikatov ki pobriše podvojene vrednosti
    vsa1 = sorted(vsa) #uredim po velikosti

    dol_pot = len(pot)
    dol_vsa = len(vsa)

    if mozna_pot(pot, zemljevid) and dol_pot == dol_vsa+2:
        return True
    else:
        return False

def navodila(pot, zemljevid):
    navodila1 = []

    for notri, krizisce, vn in zip(pot, pot[1:], pot[2:]): #naredim trojke s pomočjo zipa
        razlika = zemljevid[krizisce].index(vn) - zemljevid[krizisce].index(notri) #odštejem index izvoza ven v naslednje krožišče in indeks uvoza v trenutno krožišče
        navodila1.append(razlika%len(zemljevid[krizisce])) #appendam ostanek pri deljenju razlike in dolžine seznama sosedov

    return navodila1

import collections
