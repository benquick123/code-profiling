import pprint

def preberi(datoteka):

    zemljevid = {}

    # Odpri datoteko
    d = open(datoteka, 'r')

    for index, vrstica in enumerate(d):

        # Dodaj v slovar. Kljuc je stevilka krozisca, vrednost je pa seznam sosednjih krozisc
        # 1a. preberi sosednja krizisca v seznam
        sosednja = [int(x) for x in vrstica.split() if x.isdigit()]

        # 1b. Uredi da se bo seznam zacel z najnizjo stevilko
        min_index = sosednja.index(min(sosednja))
        prva_polovica = sosednja[min_index:]
        druga_polovica = sosednja[:min_index]
        sosednja_urejeno = prva_polovica + druga_polovica

        # 2. dodaj ta seznam v slovar-zemljevid
        zemljevid[index + 1] = sosednja_urejeno

    pprint.pprint(zemljevid)
    return zemljevid


def mozna_pot(pot, zemljevid):

    for index, x in enumerate(pot):

        # Pot se mora začeti in končati s krajiščem (povezano samo z enim križiščem)
        # Zanimajo nas samo prva in zadnja točka
        if index == 0 or index == len(pot)-1:
            if len(zemljevid[x]) != 1:
                print("Točka", x, "ni skrajna točka!\n")
                return False

        # Vse vmesne točke morajo biti križišča (imeti več kot eno povezavo)
        elif len(zemljevid[x]) <= 1:
            print("Točka", x, "ni križišče!\n")
            return False

        if index > 0:
            # Preveri da ni zaporednih ponovitev križišč (ne moreš it iz 6 v 6)
            if zemljevid[x] == zemljevid[pot[index - 1]]:
                print("Zaporedna ponovitev krožišča!\n")
                return False

            # Križišča morajo biti dejansko povezana
            # Poglej če obstaja povezava s prejšnjim in z naslednjim križiščem
            if pot[index - 1] not in zemljevid[x]:
                print("Točka", x, "ni povezana s prejšnjim križiščem!\n")
                return False

    return True


def hamiltonova(pot, zemljevid):

    # Preveri če je pot možna
    if not mozna_pot(pot, zemljevid):
        print("Pot ni možna!\n")
        return False

    # Preveri če gre po vseh krožiščih
    # Pazi, ker niso vse točke v zemljevidu krožišča (so tudi krajišča)
    # Neprevožene točke -> razlika med točkami v "pot" in vsem točkami v "zemljevidu"
    razlika = set(pot).symmetric_difference(set(zemljevid.keys()))
    for k in razlika:
        # Če je neprevožena točka krajišče je ok, čne vrni False
        if len(zemljevid[k]) != 1:
            print("Točka", k, "ni skrajna točka!\n")
            return False

    # Preveri če ni podvojitev
    if len(set(pot)) != len(pot):
        print("Pot gre čez križišče več kot enkrat!\n")
        return False

    return True




