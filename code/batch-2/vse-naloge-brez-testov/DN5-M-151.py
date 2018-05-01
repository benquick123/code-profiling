def unikati(s):
    new = []
    for a in s:
        if a not in new:
            new.append(a)
    return new

def avtor(tvit):
    if isinstance(tvit, str):
        for avt in tvit.split():
            if ":" in avt and "@" not in avt:
               return avt.strip(":")
    else:
        lis = ', '
        sus = []
        new = lis.join(map(str, tvit))
        for avt in new.split():
            if ":" in avt and "@" not in avt:
                sus.append(avt)
        return [i.split(':', 1)[0] for i in sus]



def vsi_avtorji(tviti):
    return unikati(avtor(tviti))

def izloci_besedo(beseda):
    for beginning, a in enumerate(beseda):
        if a.isalnum():
            break
    for end, a in enumerate(beseda[::-1]):
        if a.isalnum():
            break
    return beseda[beginning:len(beseda) - end]


def se_zacne_z(tvit, c):
    new = []
    for a in tvit.split():
        if c in a:
            cra = izloci_besedo(a)
            new.append(cra)
    return new


def zberi_se_zacne_z(tviti, c):
    vsi_avtorji(se_zacne_z(tviti, c))

def zberi_se_zacne_z(tviti, c):
    lis = []
    for a in tviti:
        cra = (se_zacne_z(a, c))
        lis += cra
    return unikati(lis)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    return unikati(sorted(vse_afne(tviti) + avtor(tviti)))

def custva(tviti, hashtagi):
    new = []
    for a in tviti:
        for b in a.split():
            for c in hashtagi:
                if c in b:
                    lok = avtor(a)
                    new.append(lok)
    return unikati(sorted(new))


def se_poznata(tviti, oseba1, oseba2):
    for a in tviti:
        if oseba2 in vsi_avtorji(tviti):
            if oseba1 in a and oseba2 in a:
                return True
    return False

