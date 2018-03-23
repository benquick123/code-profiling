from collections import *


def unikati(s):
    s2 = []
    for e in s:
        if e not in s2:
            s2.append(e)
    return(s2)


def avtor(tvit):
    ts = tvit.split(":")
    return ts[0]


def vsi_avtorji(tviti):
    s = []
    for t in tviti:
        a = avtor(t)
        s.append(a)
    return unikati(s)


def izloci_besedo(beseda):
    bes = beseda
    a = bes.isalnum()
    while not a:
        b = bes[0].isalnum()
        c = bes[-1].isalnum()
        if not b:
            bes = bes[1:]
        if not c:
            bes = bes[:-1]
        if b and c:
            break
    return bes



def se_zacne_z(tvit, c):
    t = tvit.split()
    s = []
    for e in t:
        if e[0] == c:
            e = izloci_besedo(e)
            s.append(e)
    return s

# Napišite funkcijo zberi_se_zacne_z(tviti, c), ki je podobna prejšnji, vendar prejme seznam tvitov in
# vrne vse besede, ki se pojavijo v njih in se začnejo s podano črko. Poleg tega naj se vsaka beseda
# pojavi le enkrat. Če pokličemo zberi_se_zacne_z(tviti, "@") (kjer so tviti gornji tviti), vrne
# ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana']. Vrstni red besed v seznamu je enak vrstnemu
# redu njihovih pojavitev v tvitih.

def zberi_se_zacne_z(tviti, c):
    s = []
    for tvit in tviti:
        a = se_zacne_z(tvit, c)
        if a != []:
            s.extend(a)
    return unikati(s)

# Napišite funkcijo vse_afne(tviti), ki vrne vse besede v tvitih, ki se začnejo z @.
# Če ji podamo gornje tvite, mora vrniti ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'].

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

#Napišite funkcijo vsi_hashtagi(tviti). Za gornje tvite vrne
#['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'].

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

#Napišite funkcijo vse_osebe(tviti), ki vrne po abecedi urejen seznam vseh oseb,
# ki nastopajo v tvitih - bodisi kot avtorji, bodisi so omenjene v tvitih.
# Vsaka oseba naj se pojavi le enkrat. Za gornje tvite funkcija vrne
# ['ana', 'benjamin', 'berta', 'cilka', 'dani', 'ema', 'sandra'].

def vse_osebe(tviti):
    a = vsi_avtorji(tviti)
    b = vse_afne(tviti)
    b.extend(a)
    b.sort()
    return unikati(b)

 # Obvezne naloge

#Funkcija besedilo(tvit) prejme tvit in vrne besedilo - torej vse, kar sledi prvemu dvopičju.
 #  Klic besedilo("ana: kdo so te: @berta, @cilka, @dani?") vrne "kdo so te: @berta, @cilka, @dani?.

def besedilo(tvit):
    tvit = tvit.split(": ", 1)
    a = tvit[0]
    b = tvit[1]
    return b


#Funkcija zadnji_tvit(tviti) prejme seznam tvitov in vrne slovar, katerega ključi so avtorji tvitov,
 #  vrednosti pa njihovi tviti. Če je en in isti avtor napisal več tvitov, naj bo v slovarju njegov
 # zadnji tvit. Rezultat je lahko, recimo

#{"berta": "@sandra Delaj domačo za #programiranje1",
# "sandra": "@berta Ne maram #programiranje1 #krneki",
# "ana": "kdo so te: @berta, @cilka, @dani? #krneki"}
#če so to edini trije avtorji in so to njihovi (zadnji) tviti.

def zadnji_tvit(tviti):
    s = {}
    for tvit in tviti:
        a = avtor(tvit)
        b = besedilo(tvit)
        s[a] = b
    return s

#Funkcija prvi_tvit(tviti) je jako podobna, le da v primeru, da je ista oseba napisala več tvitov,
#  obdrži njen prvi tvit.

def prvi_tvit(tviti):
    s = {}
    for tvit in tviti:
        a = avtor(tvit)
        b = besedilo(tvit)
        if a not in s:
            s[a] = b
    return s

#Funkcija prestej_tvite(tviti) vrne slovar, katerega ključi so (spet) avtorji, pripadajoče vrednosti
 # pa število tvitov, ki so jih napisali, na primer {"sandra": 2, "berta": 1, "ana": 1, "cilka": 4, "benjamin": 1}

def prestej_tvite(tviti):
    s = defaultdict(int)
    for tvit in tviti:
        a = avtor(tvit)
        b = besedilo(tvit)
        s[a] += 1
    return s


#Funkcija omembe(tviti) vrne slovar, katerega ključi so avtorji tvitov, vrednosti pa seznami oseb,
 # ki so jih ti avtorji omenjali v svojih tvitih. Vrstni red oseb mora biti enak vrstnemu redu omenjanj.
 # Funkcija lahko vrne, recimo
#{"sandra": ["berta", "benjamin", "ana"],
#"benjamin": [],
#"cilka": [],
#"berta": ["sandra"],
#"ana": ["berta", "cilka", "dani"]}
def omembe(tviti):
    s = defaultdict(list)
    for tvit in tviti:
        a = avtor(tvit)
        b = se_zacne_z(tvit, "@")
        if b != []:
            s[a] += b
        else: s[a] += []
    return s



#Funkcija neomembe(ime, omembe) prejme ime neke osebe in takšen slovar, kakršnega vrne gornja funkcija.
# Vrniti mora seznam vseh ljudi, ki so avtorji kakega tvita, podana oseba (ime) pa jih ni omenjala.
# Če funkciji kot argument podamo ime "Ana" in gornji slovar, mora vrniti ["sandra", "benjamin],
# saj Ana ni omenjala Sandre in Benjamina, Cilko in Berto pa je. Iz seznama naj bo seveda izključena
# oseba sama (v tem primeru Ana). Vrstni red oseb v seznamu je lahko poljuben.

def neomembe(ime, omembe):
    avtorji = omembe.keys() #vsi avtorji
    s = []
    for avtor, om in omembe.items():
        if avtor == ime:
            for a in avtorji:
                if a != ime and a not in om:
                    s.append(a)
    return s




#Dodatna naloga

#Napišite funkcijo se_poznata(ime1, ime2, omembe), ki je podobna kot v prejšnji domači nalogi,
# le da kot argument namesto tvitov dobi gornji slovar. Povedati mora, ali je prva oseba kdaj
# omenila drugo (ali obratno) ali ne. Funkcija vrne True ali False.

def se_poznata(ime1, ime2, omembe):
    s1 = []
    s2 = []
    for av, om in omembe.items():
        if av == ime1:
            s1 = om
        if av == ime2:
            s2 = om
    if ime1 in s2 or ime2 in s1:
        return True
    else: return False

 #custva(tviti, hashtagi), ki prejme seznam tvitov in seznam hashtagov (brez začetnega #).
    # Vrne naj vse avtorje, ki so uporabili vsaj enega od naštetih tagov. Avtorji naj bodo
    # urejeni po abecedi in vsak naj se pojavi le enkrat. Klic custva(tviti, ["dougcajt",
    # "krneki"]) vrne ["ana", "sandra"].

#def custva(tviti, hashtagi):
  #  avtorji = []
  #  for tvit in tviti:
 #       if neprazen_presek(se_zacne_z(tvit, "#"), hashtagi):
  #          avtorji.append(avtor(tvit))
  #  avtorji.sort()
  #  return unikati(avtorji)


def custva(tviti, hashtagi):
    return unikati(sorted(avtor(tvit) for tvit in tviti if set(hashtagi) & set(se_zacne_z(tvit, "#"))))


#Napišite funkcijo hashtagi(tviti), ki prejme seznam tvitov in vrne slovar, katerega ključi so
# hashtagi (brez znaka #), pripadajoče vrednosti pa seznami avtorjev, ki so uporabili ta hashtagi.
# Avtorji naj bodo urejeni po abecedi.

def hashtagi(tviti):
    s = {}
    for h in vsi_hashtagi(tviti):
        s[h] = custva(tviti, [h])
    return s













