def unikati(s):
    list = []
    for n in s:
        if list.count(n) < 1:
            list.append(n)
    return list

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    seznam = []
    for n in tviti:
        seznam.append(avtor(n))
    return unikati(seznam)

def izloci_besedo(beseda):
    for n in beseda:
        if n.isalnum() != True:
            beseda = beseda.replace(n, "")
        if n.isalnum() == True:
            break
    for n in beseda[::-1]:
        if n.isalnum() != True:
            beseda = beseda.replace(n, "")
        if n.isalnum() == True:
            break
    return beseda

def se_zacne_z(tvit, c):
    list = []
    tvit = tvit.split(" ")
    for n in tvit:
        if n[0] == c:
            list.append(izloci_besedo(n))
    return list

def zberi_se_zacne_z(tviti, c):
    list = []
    for n in tviti:
        list.extend(se_zacne_z(n, c))
    return unikati(list)

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")






#naloge

def besedilo(tvit):
    c = 1
    for n in tvit:
        if n.isalnum() == False:
            tvit = tvit[c:]
            return tvit.lstrip()
        c += 1

def zadnji_tvit(tviti):
    dict = {}
    for tvit in tviti[::-1]:
        if tvit.split(":")[0] not in dict:
            dict[tvit.split(":")[0]] = besedilo(tvit)
    return dict

def prvi_tvit(tviti):
    dict = {}
    for tvit in tviti:
        if tvit.split(":")[0] not in dict:
            dict[tvit.split(":")[0]] = besedilo(tvit)
    return dict

def prestej_tvite(tviti):
    dict = {}
    seznam = []
    for n in tviti:
        seznam.append(avtor(n))
    for n in seznam:
        if n not in dict:
            dict[n] = seznam.count(n)
    return dict

def omembe(tviti):
    dict = {}
    for n in tviti:
        if avtor(n) not in dict:
            dict[avtor(n)] = []
        if se_zacne_z(n, "@") not in dict[avtor(n)]:
            dict[avtor(n)].extend(se_zacne_z(n, "@"))
    return dict

def neomembe(ime, omembe):
    seznam = list(omembe.keys())
    for n in omembe[ime]:
            if n in seznam:
                seznam.remove(n)
    seznam.remove(ime)
    return seznam

def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe.get(ime2, []) or ime2 in omembe.get(ime1, []):
        return True
    else:
        return False

def hashtagi(tviti):
    dict = {}
    for hashtag in vsi_hashtagi(tviti):
        dict[hashtag] = []
        for tvit in tviti:
            if hashtag in tvit:
                dict[hashtag].append(avtor(tvit))
                dict[hashtag].sort()
    return dict

