#bucha = nespremenljivka
tviti = ([
    "sandra: Spet ta dež. #dougcajt",
    "berta: @sandra Delaj domačo za #programiranje1",
    "sandra: @berta Ne maram #programiranje1 #krneki",
    "ana: kdo so te: @berta, @cilka, @dani? #krneki",
    "cilka: jst sm pa #luft",
    "benjamin: pogrešam ano #zalosten",
    "cilka: @benjamin @ana #split? po dvopičju, za začetek?"])
tviti2 = (["sandra: Spet ta dež. #dougcajt",
                    "berta: @sandra Delaj domačo za #programiranje1",
                    "sandra: @berta Ne maram #programiranje1 #krneki",
                    "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                    "cilka: jst sm pa #luft",
                    "benjamin: pogrešam ano #zalosten",
                    "sandra: @benjamin @ana #split? po dvopičju, za začetek?"])
def izloci_besedo(beseda):
    besedica = ""
    koncno = ""
    for x in beseda:
        if x.isalnum() != True:
            beseda = beseda.replace(x, "")
        else:
            besedica = beseda[::-1]
            break
    for y in besedica:
        if y.isalnum() != True:
            besedica = besedica.replace(y, "")
        else:
            koncno = besedica[::-1]
            break
    return koncno

def se_zacne_z(tvit, c):
    seznam = []
    koncni_seznam = []
    seznam.append(tvit.split())
    for x in seznam:
        for y in x:
            if c in y:
                koncni_seznam.append(izloci_besedo(y))
    return koncni_seznam

def besedilo(tvit):
    return tvit.split(" ", 1)[1]

def besedilo_avtor(tvit):
    return tvit.split(":", 1)[0]

def zadnji_tvit(tviti):
    seznam = {}
    for x in tviti:
        seznam[besedilo_avtor(x)] = besedilo(x)
    return seznam

def prvi_tvit(tviti):
    seznam = {}
    s = tviti[::-1]
    for x in s:
        seznam[besedilo_avtor(x)] = besedilo(x)
    return seznam


def prestej_tvite(tviti):
    seznam = []
    drugi = {}
    slovar = {}
    for x in tviti:
        seznam.append(besedilo_avtor(x))
        slovar[besedilo_avtor(x)] = 0
    for y in seznam:
        drugi[y] = seznam.count(y)
    return drugi


def omembe(tviti):
    y = {}
    for x in tviti:
        if besedilo_avtor(x) not in y:
            y[besedilo_avtor(x)] = se_zacne_z(x, "@")
        else:
            y[besedilo_avtor(x)].extend(se_zacne_z(x, "@"))
    return y


def neomembe(ime, omembe):
    avtorji = omembe[ime]
    osebe = ["sandra", "berta", "ana", "cilka", "benjamin"]

    for x in avtorji:
        if x in osebe:
            osebe.remove(x)
    osebe.remove(ime)
    return osebe

#def se_poznata(ime1, ime2, omembe):


