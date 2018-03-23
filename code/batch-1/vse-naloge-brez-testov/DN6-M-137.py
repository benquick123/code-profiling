def besedilo(tvit):
        i = 0
        while i < len(tvit) - 1:
            if tvit[i] == ":":
                break
            i += 1
        return tvit[i + 1:].strip()
#print(besedilo("ana: kdo so te: @berta, @cilka, @dani?"))

def avtor(tvit):
    avtor = ""
    for x in tvit:
        if x == ":":
            break
        else:
            avtor += x
    return avtor

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        if not avtor1 in slovar:
            slovar[avtor1] = besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    avtorji = {}
    for tvit in tviti:
        avt = avtor(tvit)
        if not avt in avtorji:
            avtorji[avt] = 0
        avtorji[avt] += 1
    return avtorji

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        avt = avtor(tvit)
        tekst = besedilo(tvit)
        if not avt in slovar:
            slovar[avt] = []
        imena = izlusci_imena(tvit)
        for ime in imena:
            if not ime in slovar[avt]:
                slovar[avt].append(ime)
    return slovar


def izlusci_imena(tvit):
    besede = besedilo(tvit).split()
    imena = []
    for beseda in besede:
        if beseda[0] == "@":
            imena.append(beseda.replace("@","").replace(",","").replace("?",""))
    return imena

def neomembe(ime,omembe):
    neomenjeni = []
    vsi = []
    for key,values in omembe.items():
        for value in values:
            if not value in vsi:
                vsi.append(value)
    imenovi = omembe[ime]
    for en in vsi:
        if not en in imenovi and en != ime and en in omembe.keys():
            neomenjeni.append(en)
    return neomenjeni

omembni = {"sandra": ["berta", "benjamin", "ana"],
"benjamin": [],
"cilka": [],
"berta": ["sandra"],
"ana": ["berta", "cilka", "dani"]}

#print(neomembe("sandra",omembni))

def se_poznata(ime1,ime2,omembe):
    for x,y in omembe.items():
        if ime1 == x and ime2 in y:
            return True
        if ime2 == x and ime1 in y:
            return True
    return False

def hashtagi(tviti):
    slovar = {}
    for tvit in tviti:
        avt = avtor(tvit)
        text = besedilo(tvit)
        hs = poisci_hastage(text)
        for x in hs:
            if not x in slovar:
                slovar[x] = []
            (slovar[x].append(avt))

    for x,y in slovar.items():
        slovar[x] = sorted(y)
    return slovar


def poisci_hastage(text):

    hash  = []
    hs = ""
    for beseda in text.split():
        if beseda[0] == "#":
            hash.append(beseda[1:].replace("?",""))
    return hash


print(hashtagi(["sandra: Spet ta dež. #dougcajt",
                      "berta: @sandra Delaj domačo za #programiranje1",
                      "sandra: @berta Ne maram #programiranje1 #krneki",
                      "ana: kdo so te @berta, @cilka, @dani? #krneki",
                      "cilka: jst sm pa #luft",
                      "benjamin: pogrešam ano #zalosten",
                      "ema: @benjamin @ana #split? po dvopičju, za začetek?"]))



