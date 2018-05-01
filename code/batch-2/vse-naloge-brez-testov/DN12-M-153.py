# Napiši funkcijo preberi(ime_datoteke), ki prejme ime datoteke in vrne zemljevid.
# Datoteka je sestavljena tako, da prva vrstica ustreza prvemu krožišču (ali uvozu/izvodu), druga drugemu, tretje tretjemu in tako naprej.
# Vsaka vrstica vsebuje številke krožišč, s katerimi je posamično krožišče povezano. Krožišča so našteta po vrsti, začenši s poljubnim.
# Gornjemu zemljevidu ustreza datoteka
#   3
#   4
#   1 8 7 6 4
#   5 2 3 6
#   10 4 11
#   11 4 3
#   3 8 11
#   3 16 9 7
#   11 8 16 14
#   5 11 13
#   10 5 6 7 9 14
#   13
#   12 10 14
#   13 11 9 16
#   16
#   14 9 8 15
# Četrta vrstica, recimo, vsebuje 5 2 3 6, ker je četrto križišče povezano s križišči 5, 2, 3 in 6.
# Funkcija naj vrne slovar, katerega ključi so številke križišč, pripadajoče vrednosti pa seznami številk (int!) sosednjih križišč.
# Funkcija naj "preobrne" sezname tako, da se bodo začeli z najmanjšo številko, križišča pa morajo biti še vedno po vrsti.
# Tako bo ključu 4 pripadal element [2, 3, 6, 5] (in ne [5, 2, 3, 6], ko bi direktno prebrali iz datoteke, in tudi ne [2, 3, 5, 6], kot bi dobili, če bi seznam le uredili).

def preberi(ime_datoteke):
    slovar = {}
    dat = open(ime_datoteke, encoding='utf8')

    for i in range(1, 17):
        slovar[i] = []

    for j in range(1, 17):

        for vrstica in dat:
            stevila = vrstica.strip().split(" ")

            najm_st = 17
            for najm in stevila:
                if int(najm) < najm_st:
                    najm_st = int(najm)

            if stevila.index(str(najm_st)) == 0:
                urejena_stevila = stevila

            else:

                if len(stevila) >= 3:
                    stevila_od_najm_naprej = stevila.index(str(najm_st)) + 1
                    urejena_stevila = []
                    urejena_stevila.append(str(najm_st))
                    dolzina = len(stevila)
                    do_st = stevila.index(str(najm_st))

                    if (stevila_od_najm_naprej == 0) or (stevila.index(str(najm_st)) + 1 == dolzina):
                        for b in stevila[0:do_st]:
                            urejena_stevila.append(b)
                    else:
                        for a in stevila[stevila_od_najm_naprej:]:
                            urejena_stevila.append(a)
                            continue

                        if do_st >= dolzina%2:
                            urejena_stevila.append(str(stevila[0]))
                            for c in stevila[1:do_st]:
                                urejena_stevila.append(c)

                elif len(stevila) == 2:
                    urejena_stevila = []
                    urejena_stevila.append(stevila[1])
                    urejena_stevila.append(stevila[0])

                else:
                    urejena_stevila = stevila

            for e in urejena_stevila:

                if e == " ":
                    continue
                else:
                    slovar[j].append(int(e))
            break

    for x in list(slovar.keys()):
        if slovar[x] == []:
            del slovar[x]

    dat.close()

    return slovar


# Napiši funkcijo mozna_pot(pot, zemljevid), ki prejme seznam številk krožišč/krajišč in zemljevid.
# Vrne naj True, če je takšno pot možno prevoziti, in False, če ne.
# Pot je možno prevoziti, če se začne in konča s končno povezavo (prepoznate jo po tem, da je povezana le z enim krožiščem),
# če vmes ni končnih povezav, če se nobeno krožišče ne ponovi (iz krožišča 6 ne moremo zapeljati v krožišče 6) in če so vsa krožišča na poti dejansko povezana.

def mozna_pot(pot, zemljevid):
    zacetki_konci = []

    for kljuci in zemljevid:
        i = 0
        for vrednosti in zemljevid[kljuci]:
            if vrednosti > 0:
                i = i + 1
        if i == 1:
            zacetki_konci.append(kljuci)

    vmes = pot[1:len(pot) - 1]

    if pot[0] in zacetki_konci and pot[len(pot)-1] in zacetki_konci:

        for e in vmes:
            if e not in zacetki_konci:
                continue
            else:
                return False

        prejsnja = pot[0]
        for st in pot[1:]:
            if st != prejsnja:
                prejsnja = st
                continue
            else:
                return False

        kljuc = pot[0]
        for vrednost_k in pot[1:]:
            if vrednost_k in zemljevid[kljuc]:
                kljuc = vrednost_k
                continue
            else:
                return False

        return True

    else:
        return False


# Napiši funkcijo hamiltonova(pot, zemljevid), ki pove (True ali False), če je pot Hamiltonova.
# Pot je Hamiltonova, če je možna (prejšnja funkcija), gre prek vseh krožišč in to prek vsakega natančno enkrat.

def hamiltonova(pot, zemljevid):
    if mozna_pot(pot, zemljevid):

        zacetki_konci = []
        for kljuci in zemljevid:
            i = 0
            for vrednosti in zemljevid[kljuci]:
                if vrednosti > 0:
                    i = i + 1
            if i == 1:
                zacetki_konci.append(kljuci)

        vsi_kljuci = []
        for kljuc in zemljevid.keys():
            vsi_kljuci.append(kljuc)

        manjka_kljuci = []
        for vsi_kljuci2 in vsi_kljuci:
            if vsi_kljuci2 not in zacetki_konci:
                manjka_kljuci.append(vsi_kljuci2)

        for manjka_kljuci2 in zacetki_konci:
            if manjka_kljuci2 in pot:
                manjka_kljuci.append(manjka_kljuci2)

        for pot2 in manjka_kljuci:
            if pot2 in pot:
                continue
            else:
                return False

        vsi_kljuci3 = []
        for pot3 in pot:
            if pot3 not in vsi_kljuci3:
                vsi_kljuci3.append(pot3)
            else:
                return False

        return True

    else:
        return False


