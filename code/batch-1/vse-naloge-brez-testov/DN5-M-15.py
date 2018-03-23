def unikati(s):
    seen = set()
    seen_add = seen.add
    return [x for x in s if not (x in seen or seen_add(x))]
###################################################
def avtor(tvit):
    for beseda in tvit:
        continue
    return tvit.split(":")[0]
####################################################
def vsi_avtorji(tviti):
    avtor = []
    for i in tviti:
        avtor.append(i.split()[0])
        continue
    seen = set()
    rezultat = []
    for item in avtor:
        if item not in seen:
            seen.add(item)
            rezultat.append(item.strip(":"))
    return rezultat
####################################################
def izloci_besedo(beseda):
    bes = []
    for i in range(len(beseda)):
        prva = i
        if beseda[i].isalpha() == True:
            break
    for j in range(len(beseda),0,-1):
        zadnja = j-1
        if beseda[j-1].isalpha() == True:
            break
    for k in range(len(beseda)):
        if k >= prva and k <= zadnja:
            bes.append(beseda[k])
    return "".join(bes)
####################################################
def se_zacne_z(tvit, c):
    zac = []
    for beseda in tvit.split():
        if c in beseda:
            zac.append(beseda[0:].strip("[$,/,!,@,?]"))
    return zac
####################################################
def zberi_se_zacne_z(tviti,c):
    sezac = []
    for tvit in tviti:
        for beseda in tvit:
            if c in beseda:
                sezac.append(beseda[:2])
    print(sezac)
    return sezac

####################################################
def vse_afne(tviti):
    zac = []
    for tvit in tviti:
        if "@" in tvit:
            zac.append(tvit)
    print(zac)
    return zac
####################################################
def vsi_hashtagi(tviti):
    zac = []
    for tvit in tviti:
        if "#" in tvit:
            zac.append(tvit)
    print(zac)
    return zac
####################################################

####################################################
