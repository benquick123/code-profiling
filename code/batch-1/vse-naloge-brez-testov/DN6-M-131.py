def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def presek(s1, s2):
    p = []
    for e in s1:
        if e in s2:
            p.append(e)
    return p

def avtor(tvit):
    tvit=tvit.split()
    return tvit[0].strip(":")

def vsi_avtorji(tviti):
    avtorji=[]
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)

def izloci_besedo(beseda):
    for prva in range(len(beseda)):
        if beseda[prva].isalnum():
            break
    for zadnja in range(len(beseda), 0, -1):
        if beseda[zadnja-1].isalnum():
            break
    return beseda[prva:zadnja]

def se_zacne_z(tvit, c):
    besede = []
    for beseda in tvit.split():
        if beseda[0] == c:
            besede.append(izloci_besedo(beseda))
    return besede

def zberi_se_zacne_z(tviti, c):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit, c)
    return unikati(afne)

def vse_afne(tviti):
    return unikati(zberi_se_zacne_z(tviti, "@"))

def vsi_hashtagi(tviti):
    s = []
    for tvit in tviti:
        s += (se_zacne_z(tvit, "#"))
    return unikati(s)

def vse_osebe(tviti):
    osebe=[]
    osebe += vsi_avtorji(tviti)
    osebe += vse_afne(tviti)
    return sorted(unikati(osebe))

def custva(tviti,hashtagi):
    custvene_osebe=[]
    s=[]
    for tvit in tviti:
        tvit=tvit.split()
        for beseda in tvit:
            for hashtag in hashtagi:
                if beseda == "#"+hashtag:
                    custvene_osebe.append(tvit[0])
    for custvena_oseba in custvene_osebe:
        s.append(izloci_besedo(custvena_oseba))
    return sorted(unikati(s))

def se_poznata(tviti,oseba1,oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            for beseda in se_zacne_z(tvit,"@"):
                if beseda == oseba2:
                    return True
        elif avtor(tvit) == oseba2:
            for beseda in se_zacne_z(tvit,"@"):
                if beseda == oseba1:
                    return True

def besedilo(tvit):
    for znak in tvit:
        if znak == ":":
            tvit = tvit[tvit.index(":")+2:]
            break
    return tvit

def zadnji_tvit(tviti):
    slovar_tvitov = {}
    for tvit in tviti:
        slovar_tvitov[avtor(tvit)]= besedilo(tvit)
    return slovar_tvitov

def prvi_tvit(tviti):
    slovar_tvitov = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar_tvitov:
            slovar_tvitov[avtor(tvit)] = besedilo(tvit)
    return slovar_tvitov

def prestej_tvite(tviti):
    število_tvitov = {}
    for tvit in tviti:
        if avtor(tvit) not in število_tvitov:
            število_tvitov[avtor(tvit)]= 1
        else:
            število_tvitov[avtor(tvit)] +=1
    return število_tvitov

def omembe(tviti):
    slovar_omemb = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar_omemb:
            slovar_omemb[avtor(tvit)] = []
    for tvit in tviti:
        slovar_omemb[avtor(tvit)].extend(se_zacne_z(tvit,"@"))
    return slovar_omemb

def neomembe(ime,omembe):
    a = []
    s = []
    for osebe in omembe:
        if osebe != ime:
            a.append(osebe)
    s.extend(omembe[ime])
    return(list(set(a) - set(presek(a,s))))

