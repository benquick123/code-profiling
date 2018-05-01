import collections

def besedilo(tvit):
    for y in tvit.split(" "):
        if y.endswith(":"):
            tvit = tvit.replace(y, "")
            break
    return tvit.lstrip()

def avtor(tvit):
    spl = tvit.split(" ")
    ime = spl[0]
    return ime[:-1]

def zacne(tvit):
    sez = []
    for x in tvit.split(" "):
        if x.startswith("@"):
            koš = "!@#$=:?,."

            for smet in koš:
                x = x.replace(smet, "")
            sez.append(x)
    return sez

def zadnji_tvit(tviti):
    slov = collections.defaultdict(int)
    for x in tviti:
        ime = avtor(x)
        val = besedilo(x)
        if ime not in slov:
            slov[ime] += 1
        slov[ime] = val
    return slov

def prvi_tvit(tviti):
    slov = collections.defaultdict(int)
    for x in tviti:
        ime = avtor(x)
        val = besedilo(x)
        if ime not in slov:
            slov[ime] += 1
            slov[ime] = val
    return slov

def prestej_tvite(tviti):
    slov = collections.defaultdict(int)
    for x in tviti:
        ime = avtor(x)
        if ime not in slov:
            slov[ime] += 1
        else:
            slov[ime] +=1

    return slov

def omembe(tviti):
    slov = collections.defaultdict(int)
    for x in tviti:
        ime = avtor(x)
        val = zacne(x)
        if ime not in slov:
            slov[ime] += 1
            slov[ime] = val
        else:
            slov[ime] += val

    return slov

def neomembe(ime, omembe):
    sez = []

    for x in omembe:
        if x == ime:
            imena = omembe[ime]
            for y in omembe:
                if y not in imena and y != ime:
                    sez.append(y)
    return sez



