def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def avtor(tvit):
    a = tvit.split(": ")
    return a[0]

def vsi_avtorji(tviti):
    t = []
    a = [i.split(': ')[0] for i in tviti]
    for name in a:
        if name not in t:
            t.append(name)
    return t

def izloci_besedo(beseda):
    s = 0
    z = 1
    y = ""
    x = ""
    g = ""
    for b in beseda:
        if b.isalnum() == False:
            s += 1
        elif b.isalnum() == True:
            break
    y += beseda[s:]
    for d in y[::-1]:
        if d.isalnum() == False:
            z += 1
        elif d.isalnum() == True:
            break
    x += beseda[:-z]
    for i in y:
        if i in x:
            g += i
    return g

def se_zacne_z(tvit, c):
    n = []
    a = tvit.split(" ")
    while (True):
        for i in a:
            if i.isalnum() == False and i[0][:1] == c:
                n.append(i[1:])
        for d in n:
            if d.isalnum() == False:
                n.append(d[:-1])
                n.remove(d)
                n.sort()
        return n

def zberi_se_zacne_z(tviti, c):
    n = []
    s = []
    a = [i.split(' ') for i in tviti]
    for e in a:
        for d in e:
            if d[0] == c:
                n.append(d[1:])
            for k in n:
                if k.isalnum() == False:
                    n.append(k[:-1])
                    n.remove(k)
    for i in n:
        if i not in s:
            s.append(i)
    return s

def vse_afne(tviti):
    n = []
    s = []
    a = [i.split(" ") for i in tviti]
    while (True):
        for tvit in a:
            for e in tvit:
                if e[0] == "@":
                    n.append(e[1:])
                for d in n:
                    if d.isalnum() == False:
                        n.append(d[:-1])
                        n.remove(d)
        for i in n:
            if i not in s:
                s.append(i)

        break
    return s

def vsi_hashtagi(tviti):
    a = [i.split(" ") for i in tviti]
    n = []
    s = []
    while (True):
        for tvit in a:
            for e in tvit:
                if e[0] == "#":
                    n.append(e[1:])
            for d in n:
                if d.isalnum() == False:
                    n.append(d[:-1])
                    n.remove(d)
        for i in n:
            if i not in s:
                s.append(i)
        break
    return s

def vse_osebe(tviti):
    a = vse_afne(tviti)
    b = vsi_avtorji(tviti)
    return sorted(unikati(a+b))


def besedilo(tvit):
    x = tvit.split(" ")
    y = " ".join(x[1:])
    return y

def zadnji_tvit(tviti):
    zadtweet = {}
    for tweet in tviti:
        zadtweet[avtor(tweet)] = besedilo(tweet)
    return zadtweet

def prvi_tvit(tviti):
    zadtweet = {}
    for tweet in tviti:
        if avtor(tweet) not in zadtweet:
            zadtweet[avtor(tweet)] = besedilo(tweet)
    return zadtweet

def prestej_tvite(tviti):
    stetje = {}
    for tweet in tviti:
        if avtor(tweet) not in stetje:
            stetje[avtor(tweet)] = 0
        stetje[avtor(tweet)] += 1
    return stetje

def omembe(tviti):
    omenjeni = {}
    for tweet in tviti:
        if avtor(tweet) not in omenjeni:
            omenjeni[avtor(tweet)] = se_zacne_z(tweet, "@")
        else:
            omenjeni[avtor(tweet)].extend(se_zacne_z(tweet, "@"))
    return omenjeni

def neomembe(ime, omembe):
    neom = []
    for ime1 in omembe:
        if ime1 not in neom and ime1 not in omembe[ime] and not ime1 == ime:
            neom.append(ime1)
    return neom

def se_poznata(ime1, ime2, omembe):
    if ime1 not in omembe:
        omembe[ime1] = []
    if ime2 not in omembe:
        omembe[ime2] = []
    if ime1 in omembe[ime2] or ime2 in omembe[ime1]:
        return True
    else:
        return False

def hashtagi(tviti):
    hashi = {}
    for hash in vsi_hashtagi(tviti):
        hashi[hash] = []
        for tweet in tviti:
            if hash in tweet:
                hashi[hash].append(avtor(tweet))
        hashi[hash] = sorted(hashi[hash])
    return hashi

