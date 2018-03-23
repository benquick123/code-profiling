#1. Obvezna
def unikati(s):
    unikati = []
    for i in s:
        if i not in unikati:
            unikati.append(i)
    return unikati

#2. Obvezna
def avtor(tvit):
    tvit = tvit.split(":")
    return tvit[0]

#3. Obvezna
def vsi_avtorji(tviti):
    vsi = []
    for i in tviti:
        avtor = i.split(":")
        vsi.append(avtor[0])
    return unikati(vsi)

#4. Obvezna
def izloci_besedo(beseda):
    for i in beseda:
        if i.isalnum() == False:
            beseda = beseda[1:]
        else:
            break
    for j in range(len(beseda) - 1, 0, -1):
        if beseda[j].isalnum() == False:
            beseda = beseda[:j]
        else:
            break
    return beseda

#5. Obvezna
def se_zacne_z(tvit, c):
    besede = []
    for i in tvit.split():
        if i[0] == c:
            besede.append(izloci_besedo(i))
    return besede

#6. Obvezna
def zberi_se_zacne_z(tviti, c):
    seznam = []
    for i in tviti:
        for j in i.split():
            if j[0] == c:
                seznam.append(izloci_besedo(j))
    return unikati(seznam)

#7. Obvezna
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

#8. Obvezna
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

#9. Obvezna
def vse_osebe(tviti):
    seznam = zberi_se_zacne_z(tviti, "@")
    for i in tviti:
        seznam.append(avtor(i))
    return unikati(sorted(seznam))




