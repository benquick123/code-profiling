def unikati(s):
    nov_seznam = []
    [nov_seznam.append(unikat) for unikat in s if unikat not in nov_seznam]
    return nov_seznam

def avtor(tvit):
    nov_seznam = []
    nov_seznam = tvit.split(':')[0]
    return nov_seznam

def vsi_avtorji(tviti):
    nov_seznam = []
    for test in tviti:
        nov_seznam.append(avtor(test))
    nov_seznam = unikati(nov_seznam)
    return nov_seznam

def izloci_besedo(beseda):
    nov_seznam = []
    for crka in beseda:
        asd = crka.isalnum()
        if asd == True or crka == '-':
            nov_seznam.append(crka)
    return ''.join(nov_seznam)

def se_zacne_z(tvit, c):
    nov_seznam = []
    seznam = []
    for zacne in tvit.split():
        if zacne.startswith(c):
            nov_seznam.append(zacne)
    seznam = [s[1:] for s in nov_seznam]
    return [''.join(c for c in e if c.isalnum()) for e in seznam]

def zberi_se_zacne_z(tviti, c):
    nov_seznam = []
    for tvit in tviti:
        words = tvit.split(" ")
        for character in words:
            if character[0] == c:
                nov_seznam.append(character)
    nov_seznam = [''.join(c for c in e if c.isalnum()) for e in nov_seznam]
    return unikati(nov_seznam)

def vse_afne(tviti):
    nov_seznam = []
    seznam = []
    nov_seznam = ''.join(tviti)
    seznam = se_zacne_z(nov_seznam, '@')
    return unikati(seznam)

def vsi_hashtagi(tviti):
    nov_seznam = []
    for tvit in tviti:
        words = tvit.split()
        for character in words:
            if character[0] == '#':
                nov_seznam.append(character)
    nov_seznam = [''.join(c for c in e if c.isalnum()) for e in nov_seznam]
    return unikati(nov_seznam)

def vse_osebe(tviti):
    seznam_afen = []
    seznam_seenih = []
    seznam_afen = vse_afne(tviti)
    seznam_seenih = vsi_avtorji(tviti)
    return sorted(unikati(seznam_seenih + seznam_afen))