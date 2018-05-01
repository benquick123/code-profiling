def unikati (s):
    uniqe_elements = []
    for unit in s:
        if unit not in uniqe_elements:
            uniqe_elements.append(unit)
    return uniqe_elements

def avtor(tvit):
    breakpoint = tvit.index(":")
    avtor = tvit[:breakpoint]
    return avtor

def vsi_avtorji(tviti):
    return unikati([avtor(i) for i in tviti])

def izloci_besedo(beseda):
    start = 0
    end = 0
    for char in beseda:
        if char.isalnum():
            start = beseda.index(char)
            break
    for char in beseda[::-1]:
        if char.isalnum():
            end = beseda.rindex(char)
            break
    return(beseda[start:end+1])

def se_zacne_z(tvit, c):
    out = []
    for word in tvit.split(" "):
        for letter in word:
            if letter == c:
                out.append(izloci_besedo(word))
    return(out)

def zberi_se_zacne_z(tviti, c):
    out = []
    for tvit in tviti:
        out +=(se_zacne_z(tvit, c))
    return unikati(out)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    out_avtorji = [avtor(x) for x in tviti]
    out_omenjeni = vse_afne(tviti)
    vse_osebe = out_avtorji + out_omenjeni
    return sorted(unikati(vse_osebe))

def custva(tviti, hashtagi):

    hashi = [vsi_hashtagi(tviti)]
    avtorji_z_hash = []
    for hash in hashtagi:
        for tvit in tviti:
            if hash in tvit:
                avtorji_z_hash.append(avtor(tvit))
    return sorted(unikati(avtorji_z_hash))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if oseba1 == avtor(tvit):
            if "@" + oseba2 in tvit:
                return True
            else:
                return False

