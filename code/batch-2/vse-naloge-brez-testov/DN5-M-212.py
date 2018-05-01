
tviti = ["sandra: Spet ta dež. #dougcajt",
         "berta: @sandra Delaj domačo za #programiranje1",
         "sandra: @berta Ne maram #programiranje1 #krneki",
         "ana: kdo so te @berta, @cilka, @dani? #krneki",
         "cilka: jst sm pa #luft",
         "benjamin: pogrešam ano #zalosten",
         "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


def unikati(s):
    c = int(input("vnesi število:  "))
    for x in c :
        if x in unikati(s):
            break
        else:
            unikati(s).append(c)

def avtor(tvit):
    ime = [("sandra" , "berta ", "ana", "cilka", "benjamin", "ema")]
    for k in (tviti):
        if k in tviti and k == ime:
            return k

def vsi_avtorji(tviti):
    avtor = []
    for ime in tviti:
        if ime in tviti and ime not in vsi_avtorji(tviti):
            avtor.append(tviti)


def izloci_besedo(beseda):
    for znake in beseda:
        if znake == str:
            return beseda

        else:
            beseda.replace(znake, "")


def se_zacne_z(tvit, c):
    tvit = ""
    c = ""
    for t in tvit.split():
        if t.startswith('c'):
            if t == str:
                return t
            else:
                t.replace(tviti, "")

def zberi_se_zacne_z(tviti, c):
    tvit = ""
    c = ""
    for t in tvit.split():
        if t.startswith('c'):
            if t == str:
                if t not in tvit:
                    return t
                else:
                    break

            else:
                t.replace(tviti, "")
                if t not in tvit:
                    return t
                else:
                    break

def vse_afne(tviti):
    for y in tviti:
        if y.startswith("@"):
            y.replace("@", "")
            return y

def vsi_hashtagi(tviti):
    for hash in tviti:
        if hash.startswith("#"):
           hash.replace("#", "")
           return hash

def vse_osebe(tviti):
    ime = [("sandra", "berta ", "ana", "cilka", "benjamin", "ema")]
    for vse in tviti:
        if vse in ime:
            return  ime




