#_________________________________________ NALOGA 11  _________________________________________

def preberi(ime_datoteke):
    s = {}
    d = open(ime_datoteke, "r")
    v = 1
    for i in d:
        vrstica = i.strip().split()
        vrsta = list(map(int, vrstica))
        najmanjsa = vrsta.index(min(vrsta))
        vrsta = vrsta[najmanjsa:] + vrsta[:najmanjsa]
        s[v] = vrsta
        v = v + 1
    return s

print(preberi("zemljevid.txt"))



def mozna_pot(pot, zemljevid):
        if len(zemljevid[pot[0]]) == 1 and len(zemljevid[pot[-1]]) == 1:




#_________________________________________ TESTI  _________________________________________

