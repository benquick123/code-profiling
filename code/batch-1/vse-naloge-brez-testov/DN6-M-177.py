#1.Naloga
def besedilo (tviti):
    return tviti.split(": ",1)[1]

#2.Naloga
def zadnji_tvit(tviti):
    slovar = {}
    for i in tviti:
        i = i.split(": ", 1)
        slovar[i[0]] = i[1]
    return slovar

#3.Naloga
def prvi_tvit(tviti):
    slovar = {}
    for i in tviti:
        i = i.split(": ", 1)
        if i[0] not in slovar:
            slovar[i[0]] = i[1]
        else:
            continue
    return slovar

#4.Naloga
def prestej_tvite(tviti):
    slovar = {}
    for i in tviti:
        i = i.split(": ", 1)[0]
        x = i.count(i[0])
        slovar[i] = x
    return slovar



