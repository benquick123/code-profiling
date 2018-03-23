# Napišite funkcijo unikati(s), ki prejme seznam nekih stvari in kot rezultat vrne nov seznam, v katerem se vsak element pojavi le enkrat.
# Vrstni red v rezultat naj bo enak vrstnemu redu prvih pojavitev v podanem seznamu.
# Klic unikati([1, 3, 2, 1, 1, 3, 2]) mora vrniti [1, 3, 2].

def unikati(s):
    s2 = []
    for i in s:
        if i not in s2:
            s2.append(i)
    return s2


# Napišite funkcijo avtor(tvit), ki vrne ime avtorja podanega tvita.
# Klic avtor("ana: kdo so te @berta, @cilka, @dani? #krneki") vrne "ana".

def avtor(tvit):
    s = tvit.split(":")
    return s[0]


# Napišite funkcijo vsi_avtorji(tviti), ki prejme seznam tvitov in vrne seznam vseh njihovih avtorje.
# Vsak naj se v seznamu pojavi le enkrat; vrstni red naj bo enak vrstnemu redu prvih pojavitev.
# Če funkcijo pokličemo z gornjim seznamom tvitov, mora vrniti ["sandra", "berta", "ana", "cilka", "benjamin", "ema"].
# Sandra se pojavi le enkrat, čeprav je napisala dva tvita.

def vsi_avtorji(tviti):
    s = [i.split(":")[0] for i in tviti]
    s2 = []
    for i in s:
        if i not in s2:
            s2.append(i)
    return s2


# Napišite funkcijo izloci_besedo(beseda), ki prejme neko besedo in vrne to besedo brez vseh ne-alfanumeričnih znakov
# (to je, znakov, ki niso črke ali števke) na začetku in koncu. Če pokličemo izloci_besedo("!%$ana---"), mora vrniti "ana".
# Če pokličemo izloci_besedo("@janez-novak!!!"), vrne "janez-novak" (in ne "janeznovak"!).
# Namig: strip() tule morda ne bo preveč uporaben. Pač pa v dokumentaciji Pythona preverite, kaj dela metoda isalnum.
# Potem nalogo rešite tako, da odstranjujte prvi znak besede, dokler ta ni črka. In potem na enak način še zadnjega.
# Kako besedi odstranimo znak, pa boste - če se ne boste spomnili sami - izvedeli v zapiskih o indeksiranju.

def izloci_besedo(beseda):
    i1 = 0
    j1 = len(beseda)
    for i in range(0, len(beseda)):
        if (beseda[i].isalnum()):
            break
        else:
            i1 += 1
    for i in range(len(beseda) - 1, -1, -1):
        if (beseda[i].isalnum()):
            break
        else:
            j1 -= 1
    prava_beseda = beseda[i1:j1]
    return prava_beseda


# Napišite funkcijo se_zacne_z(tvit, c), ki prejme nek tvit in nek znak c.
# Vrniti mora vse tiste besede iz tvita, ki se začnejo s podanim znakom c.
# Pri tem mora od besed odluščiti vse nealfanumerične znake na začetku in na koncu.
# Klic se_zacne_z("sandra: @berta Ne maram #programiranje1 #krneki", "#") vrne ["programiranje1", "krneki"].

def se_zacne_z(tvit, c):
    s = []
    t = tvit.split()

    for e in t:
        if e.startswith(c):
            if e[-1].isalnum() == True:
                s.append(e[1:])
            else:
                s.append(e[1:][:-1])
    return s


# Napišite funkcijo zberi_se_zacne_z(tviti, c), ki je podobna prejšnji, vendar prejme seznam tvitov in vrne vse besede,
# ki se pojavijo v njih in se začnejo s podano črko. Poleg tega naj se vsaka beseda pojavi le enkrat.
# Če pokličemo zberi_se_zacne_z(tviti, "@") (kjer so tviti gornji tviti), vrne ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'].
# Vrstni red besed v seznamu je enak vrstnemu redu njihovih pojavitev v tvitih.

def zberi_se_zacne_z(tviti, c):
    s1 = []

    for i in tviti:
        tvit = i.split()
        for beseda in tvit:
            if beseda[0] == c:
                i1 = 0
                j1 = len(beseda)
                for i in range(0, len(beseda)):
                    if (beseda[i].isalnum()):
                        break
                    else:
                        i1 += 1
                for i in range(len(beseda) - 1, -1, -1):
                    if (beseda[i].isalnum()):
                        break
                    else:
                        j1 -= 1
                prava_beseda = beseda[i1:j1]
                s1.append(prava_beseda)

    s2 = []
    for i in s1:
        if i not in s2:
            s2.append(i)
    return s2


# Napišite funkcijo vse_afne(tviti), ki vrne vse besede v tvitih, ki se začnejo z @.
# Če ji podamo gornje tvite, mora vrniti ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'].

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


# Napišite funkcijo vsi_hashtagi(tviti). Za gornje tvite vrne ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'].

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


# Napišite funkcijo vse_osebe(tviti), ki vrne po abecedi urejen seznam vseh oseb, ki nastopajo v tvitih - bodisi kot avtorji, bodisi so omenjene v tvitih.
# Vsaka oseba naj se pojavi le enkrat. Za gornje tvite funkcija vrne ['ana', 'benjamin', 'berta', 'cilka', 'dani', 'ema', 'sandra'].

def vse_osebe(tviti):
    s = []
    a = vsi_avtorji(tviti)
    b = zberi_se_zacne_z(tviti, "@")

    s.extend(a)
    s.extend(b)

    u = unikati(s)

    sorted_list = sorted(u)

    return sorted_list



