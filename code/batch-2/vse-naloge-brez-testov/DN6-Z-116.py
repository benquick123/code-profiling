x = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
     "ema: @benjamin @ana #split? po dvopičju, za začetek?"]

#Prejšnja naloga - TVITI
def unikati(s):
    t = s[:]
    i = 0
    while i < len(t):
        if t[i] in t[:i]:
            del t[i]
        else:
            i += 1
    return t

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        imena.append(avtor(tvit))
    return unikati(imena)

def izloci_besedo(beseda):
    while beseda and not beseda[0].isalnum():
        beseda = beseda[1:]
    while beseda and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    return [izloci_besedo(beseda) for beseda in tvit.split() if beseda[0] == c]

def zberi_se_zacne_z(tviti, c):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, c)
    return unikati(afne)

def vse_afne(tviti):
    return unikati(zberi_se_zacne_z(tviti, "@"))

def vsi_hashtagi(tviti):
    return unikati(zberi_se_zacne_z(tviti, "#"))

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

def custva(tviti, hashtagi):
    return unikati(sorted(avtor(tvit) for tvit in tviti if set(hashtagi) & set(se_zacne_z(tvit, "#"))))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        pisec = avtor(tvit)
        omenjeni = se_zacne_z(tvit, "@")
        if oseba1 == pisec and oseba2 in omenjeni or \
                oseba2 == pisec and oseba1 in omenjeni:
            return True
    return False


#ZDAJŠNJA NALOGA - SPET TVITI
def besedilo(tviti):
    return tviti.split(": ", 1)[1]

def zadnji_tvit(tviti):
    slovar = {}
    for deli in tviti:
        slovar[avtor(deli)] = besedilo(deli)
    return slovar


def prvi_tvit(tviti):
    slovar = {}
    for deli in tviti:
        ime = avtor(deli)
        if not ime in slovar:
            slovar[ime] = besedilo(deli)
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for deli in tviti:
        if avtor(deli) in slovar:
            slovar[avtor(deli)] += 1
        else:
            slovar[avtor(deli)] = 1
    return slovar

def omembe(tviti):
    slovar = {}
    for deli in tviti:
        if avtor(deli) in slovar:
            for element in se_zacne_z(besedilo(deli), "@"):
                slovar[avtor(deli)].append(element)
        else:
            slovar[avtor(deli)] = se_zacne_z(besedilo(deli), "@")

    return slovar

def neomembe(ime, omembe):
    seznam = []
    smetje = []
    smetje.append(ime)
    for vrednosti in omembe[ime]:
        smetje.append(vrednosti)
    for kljuc, vrednost in omembe.items():
        if kljuc not in smetje:
            seznam.append(kljuc)
    return seznam
