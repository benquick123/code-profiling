#Napiši funkcijo preberi(ime_datoteke), ki prejme ime datoteke in vrne zemljevid. Datoteka je sestavljena tako,
# #da prva vrstica ustreza prvemu krožišču (ali uvozu/izvodu), druga drugemu, tretje tretjemu in tako naprej.
#Funkcija naj vrne slovar, katerega ključi so številke križišč,
# pripadajoče vrednosti pa seznami številk (int!) sosednjih križišč.
#f je seznam

def preberi(ime_datoteke):
    slovar = {}
    count = 1
    for i in open(ime_datoteke):
        i = i.strip()
        #print(i)
        i = i.split()
        i = list(map(int, i))
        if min(i) != i[0]:
            u = i.index(min(i))
            uu = i[:u]
            uu1 = i[u:]
            i = uu1 + uu
        slovar[count] = i
        count += 1
    print(slovar)
    return slovar



#Pot je možno prevoziti, če se začne in konča s končno povezavo
# #(prepoznate jo po tem, da je povezana le z enim krožiščem), če vmes ni končnih povezav, če se nobeno
#krožišče ne ponovi (iz krožišča 6 ne moremo zapeljati v krožišče 6) in če so vsa krožišča na poti dejansko povezana.

def mozna_pot(pot, zemljevid):
    count = 0
    for korak in pot:
        if count == 0 or count == len(pot) - 1:
            if len(zemljevid[korak]) != 1:
                return False
        else:
            if len(zemljevid[korak]) == 1:
                return False
        if count > 0:
            prejsni_korak = pot[count - 1]
            if korak not in zemljevid[prejsni_korak]:
                return False
        count += 1
    return True

def hamiltonova(pot, zemljevid):
    seznam = []
    if not mozna_pot(pot,zemljevid):
        print("ena")
        return False
    for i in pot:
        if i not in seznam:
            seznam.append(i)
        else:
            print("dva")
            return False
    st_koncnih_povezav = 0
    for kljuc, vrednost in zemljevid.items():
        if len(vrednost) == 1:
            st_koncnih_povezav += 1
    if not len(pot) - 2 == len(zemljevid.keys()) - st_koncnih_povezav:
        print(len(zemljevid.keys()), len(pot))
        print("tri")
        return False
    return True
































