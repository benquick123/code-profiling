# Obvezen del

def unikati(s):
    xs = []
    for e in s:
        if e not in xs:
            xs.append(e)
    return xs

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    s = []
    for tvit in tviti:
        s.append(avtor(tvit))
    return unikati(s)

def izloci_besedo(beseda):
    i = j = 0
    for e in beseda:
        if e.isalnum():
            break
        else:
            i += 1
    for e in beseda[::-1]:
        if e.isalnum():
            break
        else:
            j += 1
    j = len(beseda) - j
    return beseda[i:j]

def se_zacne_z(tvit, c):
    s = []
    for e in tvit.split():
        if e[0] == c:
            s.append(izloci_besedo(e))
    return s

def zberi_se_zacne_z(tviti, c):
    s = []
    for tvit in tviti:
        s.append(se_zacne_z(tvit, c))
    xs = [x for xs in s for x in xs] # == for xs in s:    for x in xs:        xs.append(x)
    return unikati(xs)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    s = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    s.sort()
    return s

# Dodaten del

def custva(tviti, hashtagi):
    s = []
    for hashtag in hashtagi:
        for tvit in tviti:
            vsi_hashi = se_zacne_z(tvit, "#")
            if hashtag in vsi_hashi:
                s.append(avtor(tvit))
    return vse_osebe(s)

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if oseba1 == avtor(tvit) and oseba2 in se_zacne_z(tvit, "@") or oseba2 == avtor(tvit) and oseba1 in se_zacne_z(tvit, "@"):
            return True
    return False

# Testi

