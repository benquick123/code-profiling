import collections
def besedilo(tvit):
    return tvit.split(": ", 1)[1]

def zadnji_tvit(tviti):
    dic = {}
    for tvit in tviti:
        a = tvit.split(": ", 1)
        kljuc=a[0]
        podatek=a[1]
        dic[kljuc] = podatek

    return dic

def prvi_tvit(tviti):
    dic = {}
    for tvit in reversed (tviti):
        a = tvit.split(": ", 1)
        kljuc=a[0]
        podatek=a[1]
        dic[kljuc] = podatek

    return dic

def prestej_tvite(tviti):
    seznam = []
    for tvit in tviti:
        oseba=tvit.split(":", 1) [0]
        seznam.append(oseba)
    st_tviti=collections.Counter(seznam)
    return st_tviti


