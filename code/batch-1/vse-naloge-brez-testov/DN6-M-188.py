def unikati(s):
    nov_s = []

    for i in s:
        for j in nov_s:
            if i == j:
                break
        else:
            nov_s.append(i)

    return nov_s


def avtor(tvit):
    tvit = tvit.split(":")
    return tvit[0]

def vsi_avtorji(tviti):
    s = []
    for i in range(len(tviti)):
        if avtor(tviti[i]) not in s:
            s.append(avtor(tviti[i]))
    return s



def izloci_besedo(beseda):
    st1 = 0
    st2 = len(beseda)
    for i in beseda:
        if not i.isalnum():
            st1 += 1
        else:
            break
    for j in range(len(beseda)):
        if not beseda[len(beseda)-1-j].isalnum():
            st2 -= 1
        else:
            break
    return beseda[st1:st2]



def se_zacne_z(tvit, c):
    s = tvit.split()
    sez = []
    for i in range(len(s)):
        if s[i].startswith(c):
            sez.append(izloci_besedo(s[i]))
    return sez




def zberi_se_zacne_z(tviti, c):
    s = []
    for i in tviti:
        s += (se_zacne_z(i, c))
    return unikati(s)


def vse_afne(tviti):
    s = []
    for i in tviti:
        s += se_zacne_z(i, '@')
    return unikati(s)


def vsi_hashtagi(tviti):
    s = []
    for i in tviti:
        s += se_zacne_z(i, '#')
    return unikati(s)



def vse_osebe(tviti):
    s = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return sorted(s)



def custva(tviti, hashtagi):
    s = []

    for i in tviti:
        for j in hashtagi:
            if '#'+j in i:
                s.append(avtor(i))
                break
    return sorted(unikati(s))


def se_poznata(tviti, oseba1, oseba2):
    for i in tviti:
        if avtor(i) == oseba1:
            if oseba2 in se_zacne_z(i, '@'):
                return True
    else:
        return False










import collections





def besedilo(tvit):
    b = avtor(tvit)
    return tvit.split(b + ": ")[1]

def zadnji_tvit(tviti):
    s = {}
    for i in tviti:
        if avtor(i) not in s:
            s[avtor(i)] = ""
        s[avtor(i)] = besedilo(i)
    return s


def prvi_tvit(tviti):
    s = {}
    for i in tviti:
        if avtor(i) not in s:
            s[avtor(i)] = besedilo(i)
    return s


def prestej_tvite(tviti):
    s = {}
    avtorji = []
    for i in tviti:
        avtorji += [avtor(i)]
    c = collections.Counter(avtorji)
    for j in tviti:
        if avtor(j) not in s:
            s[avtor(j)] = c[avtor(j)]
    return s




def omembe(tviti):
    s = {}
    for i in tviti:
        if avtor(i) not in s:
            s[avtor(i)] = []
        s[avtor(i)] += zberi_se_zacne_z([i], "@")
    return s



def neomembe(ime, omembe):
    print(omembe)
    s = []
    k = []
    for naslov, vrednost in omembe.items():
        if naslov == ime:
            s = vrednost
    for n, v in omembe.items():
        if n not in s and n != ime:
            k += [n]
    return k





