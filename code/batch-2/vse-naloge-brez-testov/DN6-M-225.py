


tviti = ["sandra: Spet ta dež. #dougcajt",
         "berta: @sandra Delaj domačo za #programiranje1",
         "sandra: @berta Ne maram #programiranje1 #krneki",
         "ana: kdo so te @berta, @cilka, @dani? #krneki",
         "cilka: jst sm pa #luft",
         "benjamin: pogrešam ano #zalosten",
         "ema: @benjamin @ana #split? po dvopičju, za začetek?"]

def unikati(s):
    d = []
    for i in range(0, len(s)):
        if d.count(s[i]) == 0:
            d.append(s[i])
    return d

def avtor(tvit):
    s = tvit.split(':')
    return s[0]

def vsi_avtorji(tvits):
    d = []
    for s in tvits:
       if d.count(avtor(s)) == 0:
            d.append(avtor(s))
    return d

def izloci_besedo(beseda):
    while beseda[0].isalnum() == False:
        beseda = beseda[1:]
    while beseda[-1].isalnum() == False:
        beseda = beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    tvit = tvit.split()
    d = []
    for s in tvit:
        if s[0] == c:
            d.append(izloci_besedo(s))
    return d

def zberi_se_zacne_z(tvits, c):
    f = []
    for i in tvits:
        d = se_zacne_z(i, c)
        for z in d:
            if (z in f) == False:
                f.append(z)
    return f

def vse_afne(tvits):
    return zberi_se_zacne_z(tvits, '@')

def vsi_hashtagi(tvits):
    return zberi_se_zacne_z(tvits, '#')

def vse_osebe(tvits):
    d = vse_afne(tvits)
    f = vsi_avtorji(tvits)
    for i in f:
        if (i in d) == False:
            d.append(i)
    d.sort()
    return d

def custva(tvits, hashtagi):
    j = []
    for i in tvits:
        for h in hashtagi:
            if (h in i) == True:
                if (avtor(i) in j) == False:
                    j.append(avtor(i))
                    break
    j.sort()
    return j

def se_poznata(oseba1, oseba2, omembe):
    if (oseba1 in omembe) and (oseba2 in omembe[oseba1]):
        return True
    if (oseba2 in omembe) and (oseba1 in omembe[oseba2]):
        return True
    return False

def besedilo(tvit):
   i = 0
   while True:
        if tvit[i] == ":":
            break
        i += 1
   return tvit[i+2:]

def zadnji_tvit(tviti):
    avt = vsi_avtorji(tviti)
    dic = dict.fromkeys(avt)
    for i in tviti:
        s = i.split(':')
        dic[s[0]] = besedilo(i)
    return dic

def prvi_tvit(tviti):
    avt = vsi_avtorji(tviti)
    dic = dict.fromkeys(avt, None)
    for i in tviti:
        s = i.split(':')
        if dic[s[0]] == None:
            dic[s[0]] = besedilo(i)
    return dic

def prestej_tvite(tviti):
    avt = vsi_avtorji(tviti)
    dic = dict.fromkeys(avt, 0)
    for i in tviti:
        s = i.split(':')
        dic[s[0]] += 1
    return dic

def omembe(tviti):
    avt = vsi_avtorji(tviti)
    dic = dict.fromkeys(avt, None)
    for i in tviti:
        s = i.split(':')
        if dic[s[0]] == None:
            dic[s[0]] = se_zacne_z(i, '@')
        else:
            dic[s[0]] += se_zacne_z(i, '@')
    return dic

def neomembe(ime, omembe):
    avtors = list(omembe.keys())
    avtors.remove(ime)
    for i in omembe[ime]:
        if i in avtors:
            avtors.remove(i)
    return avtors

def hashtagi(tviti):
    dic = dict.fromkeys(vsi_hashtagi(tviti), None)
    for i in tviti:
        hashtags = se_zacne_z(i, '#')
        for j in hashtags:
            if dic[j] == None:
                dic[j] = [avtor(i)]
            else:
                dic[j] += [avtor(i)]
    for i in list(dic.keys()):
        dic[i].sort()
    return dic


