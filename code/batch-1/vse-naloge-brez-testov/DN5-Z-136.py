#Napišite funkcijo unikati(s), ki prejme seznam nekih stvari
#in kot rezultat vrne nov seznam, v katerem se vsak element pojavi le enkrat. Vrstni red v
#rezultat naj bo enak vrstnemu redu prvih pojavitev v podanem
#seznamu. Klic unikati([1, 3, 2, 1, 1, 3, 2]) mora vrniti [1, 3, 2].

def unikati(s):
    seznam = []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

#napišite funkcijo avtor(tvit), ki vrne ime avtorja podanega tvita. Klic avtor("ana: kdo so te @berta, @cilka, @dani? #krneki") vrne "ana".

def avtor(tvit):
    presledki = tvit.split()
    prvi = presledki[0]
    ime, text = prvi.split(":")
    return ime

# Napišite funkcijo vsi_avtorji(tviti), ki prejme seznam tvitov in vrne seznam vseh njihovih avtorje.
# Vsak naj se v seznamu pojavi le enkrat; vrstni red naj bo enak vrstnemu redu prvih pojavitev.
# Če funkcijo pokličemo z gornjim seznamom tvitov,
# mora vrniti ["sandra", "berta", "ana", "cilka", "benjamin", "ema"]. Sandra se pojavi le enkrat, čeprav je napisala dva tvita.

def vsi_avtorji(tviti):
    s=[]
    for i in tviti:
        s.append(avtor(i))
    return unikati(s)

#Napišite funkcijo izloci_besedo(beseda),
# ki prejme neko besedo in vrne to besedo brez vseh ne-alfanumeričnih znakov (to je, znakov, ki niso črke ali števke) na začetku in koncu.
# Če pokličemo izloci_besedo("!%$ana---"), mora vrniti "ana".
# Če pokličemo izloci_besedo("@janez-novak!!!"), vrne "janez-novak" (in ne "janeznovak"!). Namig: strip() tule morda ne bo preveč uporaben.
# Pač pa v dokumentaciji Pythona preverite, kaj dela metoda isalnum. Potem nalogo rešite tako, da odstranjujte prvi znak besede, dokler ta ni črka.
# In potem na enak način še zadnjega. Kako besedi odstranimo znak, pa boste - če se ne boste spomnili sami - izvedeli v zapiskih o indeksiranju.

def izloci_besedo(beseda):
    s = []
    s = list(beseda)
    if beseda.isalnum() == False:
        while s[0].isalnum() == False:
                del s[0]
        while s[-1].isalnum() == False:
                del s[-1]
    return "".join(s)


def se_zacne_z(tvit, c):
    s = tvit.split()
    m = []
    for i in s:
        if i[0] == c:
            m.append(izloci_besedo(i))
    return m

#Napišite funkcijo zberi_se_zacne_z(tviti, c),
# ki je podobna prejšnji, vendar prejme seznam tvitov in vrne vse besede,
#  ki se pojavijo v njih in se začnejo s podano črko. Poleg tega naj se vsaka beseda pojavi le enkrat.
# Če pokličemo zberi_se_zacne_z(tviti, "@") (kjer so tviti gornji tviti),
# vrne ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana']. Vrstni red besed v seznamu je enak vrstnemu redu njihovih pojavitev v tvitih.

def zberi_se_zacne_z(tviti, c):
    zbrani = []
    for tvit in tviti:
        loceni = tvit.split()
        for i in loceni:
            if c in i:
                zbrani.append(izloci_besedo(i))
    return unikati(zbrani)

#Napišite funkcijo vse_afne(tviti), ki vrne vse besede v tvitih,
# ki se začnejo z @. Če ji podamo gornje tvite, mora vrniti
# ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'].

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

#Napišite funkcijo vsi_hashtagi(tviti).
# Za gornje tvite vrne ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'].

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

#Napišite funkcijo vse_osebe(tviti), ki vrne po abecedi urejen seznam vseh oseb, ki nastopajo v tvitih - bodisi kot avtorji,
#  bodisi so omenjene v tvitih. Vsaka oseba naj se pojavi le enkrat.
# Za gornje tvite funkcija vrne ['ana', 'benjamin', 'berta', 'cilka', 'dani', 'ema', 'sandra'].

def vse_osebe(tviti):
    return sorted(unikati(vse_afne(tviti) + vsi_avtorji(tviti)))









