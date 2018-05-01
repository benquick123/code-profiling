#1.Napišite funkcijo unikati(s), ki prejme seznam nekih stvari in kot rezultat vrne nov seznam,
#  v katerem se vsak element pojavi le enkrat.
#  Vrstni red v rezultat naj bo enak vrstnemu redu prvih pojavitev v podanem seznamu. Klic unikati([1, 3, 2, 1, 1, 3, 2]) mora vrniti [1, 3, 2]

def unikati(s):
    novi_seznam=[]
    for podatki in s:
        if podatki not in novi_seznam:
            novi_seznam.append(podatki)
    return novi_seznam

print(unikati([1, 3, 2, 1, 1, 3, 2]) )

#Napišite funkcijo avtor(tvit), ki vrne ime avtorja podanega tvita.
#  Klic avtor("ana: kdo so te @berta, @cilka, @dani? #krneki") vrne "ana".

def avtor(tvit):
    ime_avtorja=tvit.split(":")
    return ime_avtorja[0]

print(avtor("ana: kdo so te @berta, @cilka, @dani? #krneki"))


#3.Napišite funkcijo vsi_avtorji(tviti), ki prejme seznam tvitov in vrne seznam vseh njihovih avtorje.
# Vsak naj se v seznamu pojavi le enkrat; vrstni red naj bo enak vrstnemu redu prvih pojavitev.
# Če funkcijo pokličemo z gornjim seznamom tvitov, mora vrniti
# ["sandra", "berta", "ana", "cilka", "benjamin", "ema"].
# Sandra se pojavi le enkrat, čeprav je napisala dva tvita.

def vsi_avtorji(tviti):
    novi_seznam_ko_samo_imena=[]
    for podatki in tviti: #za podatek dobim posamezni tvit
        ime_avtorja=avtor(podatki) #ker v podatkih shranjenj posamezni tvit
        #if ime_avtorja not in novi_seznam_ko_samo_imena:
        novi_seznam_ko_samo_imena.append(ime_avtorja)
    novi_seznam_ko_samo_imena=unikati(novi_seznam_ko_samo_imena)
    return novi_seznam_ko_samo_imena


#4.Napišite funkcijo izloci_besedo(beseda), ki prejme neko besedo in vrne to besedo brez vseh
#  ne-alfanumeričnih znakov (to je, znakov, ki niso črke ali števke) na začetku in koncu.
#  Če pokličemo izloci_besedo("!%$ana---"), mora vrniti "ana".
#  Če pokličemo izloci_besedo("@janez-novak!!!"), vrne "janez-novak" (in ne "janeznovak"!).
#  Namig: strip() tule morda ne bo preveč uporaben.
#  Pač pa v dokumentaciji Pythona preverite,
#  kaj dela metoda isalnum. Potem nalogo rešite tako,
# da odstranjujte prvi znak besede, dokler ta ni črka.
#  In potem na enak način še zadnjega.
# Kako besedi odstranimo znak, pa boste - če se ne boste spomnili sami - izvedeli v zapiskih o indeksiranju.

def izloci_besedo(beseda):
    for i in range(0,len(beseda)):
        znak=beseda[i]
        if not znak.isalnum():
            beseda=beseda[:i]+ " "+ beseda[i+1:]
        else:
            break


    for i in range(len(beseda)-1, 0, -1): #prva -1, je da dobimo zadnji indeks, drugi -1 pa je negativni korak
        znak=beseda[i]
        if not znak.isalnum():
             beseda= beseda[:i]+ " "+ beseda[i+1:]
        else:
            break

    return beseda.strip()


izloci_besedo("!%$ana---")


izloci_besedo("@janez-novak!!!")


#5Napišite funkcijo se_zacne_z(tvit, c),
# ki prejme nek tvit in nek znak c. Vrniti mora vse tiste besede iz tvita,
#  ki se začnejo s podanim znakom c.
# Pri tem mora od besed odluščiti vse nealfanumerične znake na začetku in na koncu.
#  Klic se_zacne_z("sandra: @berta Ne maram #programiranje1 #krneki", "#") vrne ["programiranje1", "krneki"].

def se_zacne_z(tvit, c):
    seznam_besed=tvit.split(" ") #dobimo seznam razdeljen po besedah
    seznam_besed_z_c=[]
    for beseda in seznam_besed:
        if beseda[0]==c:
            samo_alfanumerične=izloci_besedo(beseda)
            seznam_besed_z_c.append(samo_alfanumerične)

    return seznam_besed_z_c

print(se_zacne_z("sandra: @berta Ne maram #programiranje1 #krneki", "#"))

#6Napišite funkcijo zberi_se_zacne_z(tviti, c),
# ki je podobna prejšnji, vendar prejme seznam tvitov in vrne vse besede,
# ki se pojavijo v njih in se začnejo s podano črko.
#  Poleg tega naj se vsaka beseda pojavi le enkrat.
#  Če pokličemo zberi_se_zacne_z(tviti, "@")
# (kjer so tviti gornji tviti), vrne ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'].
#  Vrstni red besed v seznamu je enak vrstnemu redu njihovih pojavitev v tvitih.
def zberi_se_zacne_z(tviti, c):
    novi_seznam_besed_ki_jih_iscemo=[]
    for tvit in tviti:
        za_besede_ki_zacnejo_z_c=se_zacne_z(tvit,c)
        novi_seznam_besed_ki_jih_iscemo=novi_seznam_besed_ki_jih_iscemo+za_besede_ki_zacnejo_z_c

    nepodvojene_besede=unikati(novi_seznam_besed_ki_jih_iscemo)
    return nepodvojene_besede

#7Napišite funkcijo vse_afne(tviti), ki vrne vse besede v tvitih, ki se začnejo z @.
# Če ji podamo gornje tvite, mora vrniti ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana']

def vse_afne(tviti):
    afne=zberi_se_zacne_z(tviti,"@")

    return afne

#8Napišite funkcijo vsi_hashtagi(tviti). Za gornje tvite vrne ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'].

def vsi_hashtagi(tviti):
    brez_heštegov=zberi_se_zacne_z(tviti,"#")

    return brez_heštegov

#9Napišite funkcijo vse_osebe(tviti),
# ki vrne po abecedi urejen seznam vseh oseb,
# ki nastopajo v tvitih - bodisi kot avtorji,
# bodisi so omenjene v tvitih. Vsaka oseba naj se pojavi le enkrat.
# Za gornje tvite funkcija vrne ['ana', 'benjamin', 'berta', 'cilka', 'dani', 'ema', 'sandra'].

def vse_osebe(tviti):
    vseosebe=vsi_avtorji(tviti)
    ostale_osebe=vse_afne(tviti)
    vseosebe=vseosebe+ostale_osebe
    print(vseosebe)
    le_enkrat=unikati(vseosebe)
    print(le_enkrat)
    le_enkrat.sort() #to sortira po abecedi vse osebe tviti
    return le_enkrat




















