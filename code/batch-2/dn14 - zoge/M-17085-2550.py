import risar
from random import *
import random # brez tega ne dela random.uniform
from math import *
from time import *

# barva je rgb (torej red green blue)
def barva():
    r = randint(0, 255)  # s tem izračunamo poljubno vrednost rdeče barve
    g = randint(0, 255)  # s tem izračunamo poljubno vrednost zelene barve
    b = randint(0, 255)  # s tem izračunamo poljubno vrednost modre barve
    barva = risar.barva(r, g, b)  # skupna vrednost treh vrednost rgb barv nam da eno (risar)
    return barva

def pitagorov():
    c = 5                # koordinata c je 5, saj moramo na vsak poteg zanke se za 5 enot premakniti. (nove koordinate izračunamo po pitagorovem izreku)
    a = random.uniform(-5, 5) # v naovdilah ste dali namig za naključno koordinato x na intervalu od -5 do 5
    b = sqrt(pow(c, 2) - pow(a, 2)) #koordinato b zračunamo po pitagorovem izreku
    predznak=random.choice([1,-1])  # da se krogi naključno premikajo gor in dol, rabimo kdaj imeti drugo koordinato tudi negativno
    b=b*predznak # če pomnožimo z 1, vrednost ostane enaka, če pa z -1 pa rata vrednost y oz b negativna
    return a,b           # vrnemo vrednost a, b ( vrednosti x,y)

krogci = []                # seznam za shranjevanje krogcev
koordinatex=[]           # seznam za shranjevanje premikov po x osi
koordinatey=[]           # seznam za shranjevanje premikov po y osi

maxX=risar.maxX          # maksimalna vrednost okna po osi x
maxY=risar.maxY          # maksimalna vrednost okna po osi y

# zanka za začetni položaj, barvo in ostalo za vsakega izmed 30 krogcov
for krog in range(0,30):                        # naloga od nas zahteva 30 krogov
    x = randint(11, maxX-11)                    # da koordinate niso na robu, moramo dodati odmik takšen kolikšen je polmer
    y = randint(11, maxY-11)
    barva_kroga=barva()                         # pokličemo funkcijo barva

    krogec = risar.krog(x, y, 10, barva_kroga, sirina=4) # krog dobimo če v funkcijo risar.krog vnesemo koordinate x in y, polmerom kroga, barvo, ki sem jo prej izračunal, in širino krožnice, ki obdaja krog,
    krogci.append(krogec)                       # v seznam krogci dodamo prejšni krogec

    koordinatax, koordinatay= pitagorov()       # dobimo vrednosti za premik

    koordinatex.append(koordinatax)             # v seznam koordinat x dodamo trenutno vrednost koordinate x
    koordinatey.append(koordinatay)             # v seznam koordinat y dodamo trenutno vrednost koordinate y

cas= time() + 20                                # program mora ostati odprt 20 sekun

#dokler je okno odprto (20 sekund) se premikajo vsi krogci
while time()<=cas:                              # dokler cas ni manjsi ali enak casu programa
    # zanka za premikanje krogcev
    for stevec in range(0,30):                  # imamo 30 krogcev
        krogec=krogci[stevec]                   # vsak krogec premikamo posebej
        novakoordinatax=krogec.x()+koordinatex[stevec]          # trenutni vrednosti koordinate x prištejemo premik
        novakoordinatay=krogec.y()+koordinatey[stevec]          # trenutni vrednosti koordinate y prištejemo premik
        krogec.setPos(novakoordinatax, novakoordinatay)         # krogec postavimo na nove vrednosti koordinat

         # če vrednost ni med mejama 0 in maksimalno vrednostjo, potem obrni smer premika

        if krogec.x()<10 or krogec.x()>maxX-10:             # če je vrednost manjša od 10 (polmer krogca) ali večja od maksimalne vrednosti x - 10 (ker je polmer krogca 10)
            koordinatex[stevec] = -koordinatex[stevec]  # obrnemo smer premika
        if krogec.y()<10 or krogec.y()>maxY-10:             # če je vrednost manjša od 10 (polmer krogca) ali večja od maksimalne vrednosti y -10 (ker je polmer krogca 10)
            koordinatey[stevec] = -koordinatey[stevec]  # obrnemo smer premika

    risar.cakaj(0.02)                           # med vsako ponovitev zanke je paza 0.02 sekunde