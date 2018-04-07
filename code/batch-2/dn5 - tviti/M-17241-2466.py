def unikati(s):
    list = []
    for a in c:
        if a not in list:
            list.append(a)
    return list


def avtor(tvit):
    ter_tvit = ""
    x = 0
    y = 0
    for x in tvit:
        y = tvit.find(":")
        while x != y:
            ter_tvit += tvit[a]
            x += 1
    return ter_tvit


def vsi_avtorji(tviti):
    o = ""
    list = []
    list_nm2 = []
    for a in tviti:
        list.append(a)
        i = a.split(":")
        list_nm2.append(i[0])
    return unikati(list_nm2)


def izloci_besedo(word):
    clen = ""
    izpis = ""
    for a in word:
        if a.isalnum() != True:
            word = word.replace(a, "")
        else:
            clen = word[::-1]
            break
    for b in clen:
        if b.isalnum() != True:
            clen = clen.replace(b, "")
        else:
            koncno = clen[::-1]
            break
    return izpis


def zberi_se_zacne_z(tviti, d):
    e = 0
    list = []
    final_list = []
    for a in tviti:
        list.append(a.split())
    for b in list:
        for e in b:
            if d in e:
                final_list.append(izloci_besedo(e))
    return unikati(final_list)


def vse_afne(tviti):
    e = 0
    list = []
    final_list = []
    for a in tviti:
        list.append(a.split())
    for b in list:
        for e in b:
            if "@" in e:
                final_list.append(izloci_besedo(e))
    novi = unikati(final_list)
    return novi


def vsi_hashtagi(tviti):
    e = 0
    list = []
    final_list = []
    for x in tviti:
        list.append(x.split())
    for b in list:
        for e in b:
            if "#" in e:
                final_list.append(izloci_besedo(e))
    return unikati(final_list)


def vse_osebe(tviti):
    list = []
    novi = []
    new_final = []
    omega_list = []
    list.append(vse_afne(tviti))
    list.append(vsi_avtorji(tviti))
    for e in list:
        for d in e:
            novi.append(d)
    new_final = sorted(novi)
    omega_list = (unikati(new_final))
    return omega_list
