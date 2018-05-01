import collections
def unikati(s):
    novi = []
    for del_seznama in s:
        if del_seznama in novi:
            None
        else:
            novi.append(del_seznama)
    return novi
def avtor(tvit):
    return tvit.split( )[0][:-1]
def vsi_avtorji(tviti):
    avtorji =[]
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)
def izloci_besedo(beseda):
    i= 0
    while i < len(beseda):
        if not str.isalnum(beseda[i]):
            beseda = beseda[i + 1:]
        else:
            break
    for i in range(len(beseda)):
        if i < len(beseda):
            if not str.isalnum(beseda[-1 - i]):
                beseda = beseda[:-1-i]
            else:
                break
    return beseda
def se_zacne_z(tvit, c):
    se_zacnejo =[]
    tvit = tvit.split( )
    for beseda in tvit:
        if beseda[0] == c:
            se_zacnejo.append(izloci_besedo(beseda))
    return se_zacnejo
def zberi_se_zacne_z(tviti, c):
    a = []
    for tvit in tviti:
        if c in tvit:
            besede_v_tvitu = se_zacne_z(tvit,c)
            a = a + besede_v_tvitu
    return unikati(a)
def vse_afne(tviti):
    return se_zacne_z(tviti,"@")
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")
def po_abecedi(imena):
    urejena = []
    while len(imena) != 0:
        najmanjse_ime = "zzzzzzzzz"
        for ime in imena:
            if ime < najmanjse_ime:
                najmanjse_ime=ime
        imena.remove(najmanjse_ime)
        urejena.append(najmanjse_ime)
    return urejena
def vse_osebe(tviti):
    vsi = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return po_abecedi(vsi)
def custva(tviti, hashtagi):
    imena = []
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in tvit:
                imena.append(avtor(tvit))
    return po_abecedi(unikati(imena))
def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1 and oseba2 in vse_afne(tvit.split( )) or oseba2 == avtor(tvit) and oseba1 in vse_afne(tvit.split( )):
            return True
    return False
def besedilo(tvit):
    return tvit.split(": ",1)[-1]
def zadnji_tvit(tviti):
    s = collections.defaultdict(str)
    for tvit in tviti:
        s[avtor(tvit)] = besedilo(tvit)
    return s
def prvi_tvit(tviti):
    s= {}
    for tvit in tviti:
        if avtor(tvit) not in s.keys():
            s[avtor(tvit)] = besedilo(tvit)
    return s
def prestej_tvite(tviti):
    s = {}
    for tvit in tviti:
        if avtor(tvit) not in s.keys():
            s[avtor(tvit)] = 1
        else:
            s[avtor(tvit)] += 1
    return s
def omembe(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        if avtor(tvit) not in s.keys():
            s[avtor(tvit)] = vse_afne(tvit)
        else:
            s[avtor(tvit)] += vse_afne(tvit)
            s[avtor(tvit)] = unikati(s[avtor(tvit)])
    return s
def neomembe(ime, omembe):
    tviti = ["sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "cilka: @benjamin @ana #split? po dvopičju, za začetek?"]
    s = vsi_avtorji(tviti)
    if ime in omembe.keys():
        for ime_kljuc in omembe[ime]:
            if ime_kljuc in omembe.keys():
                s.remove(ime_kljuc)
            else:
                None
        s.remove(ime)
        return s
    return []
def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe.keys() and ime2 in omembe.keys():
        if ime1 in omembe[ime2] or ime2 in omembe[ime1]:
            return True
        return False
def hashtagi(tviti):
    s = collections.defaultdict(list)
    for tvit in tviti:
        avtor1 = avtor(tvit)
        for beseda in tvit.split( ):
            if beseda[0] == "#":
                s[izloci_besedo(beseda)].append(avtor1)
                s[izloci_besedo(beseda)] = sorted(s[izloci_besedo(beseda)])
    return s













