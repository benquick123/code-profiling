def unikati(s):
    novi = []
    for del_seznama in s:
        if del_seznama in novi:
            None
        else:
            novi.append(del_seznama)
    return novi
def avtor(tvit):
    return tvit.split( )[0][:-1]
def vsi_avtorji(tviti):
    avtorji =[]
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)
def izloci_besedo(beseda):
    i= 0
    while i < len(beseda):
        if not str.isalnum(beseda[i]):
            beseda = beseda[i + 1:]
        else:
            break
    for i in range(len(beseda)):
        if i < len(beseda):
            if not str.isalnum(beseda[-1 - i]):
                beseda = beseda[:-1-i]
            else:
                break
    return beseda
def se_zacne_z(tvit, c):
    se_zacnejo =[]
    tvit = tvit.split( )
    for beseda in tvit:
        if beseda[0] == c:
            se_zacnejo.append(izloci_besedo(beseda))
    return se_zacnejo
def zberi_se_zacne_z(tviti, c):
    a = []
    besede = []
    for tvit in tviti:
        if c in tvit:
            besede_v_tvitu = se_zacne_z(tvit,c)
            a = a + besede_v_tvitu
    return unikati(a)
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")
def po_abecedi(imena):
    urejena = []
    while len(imena) != 0:
        najmanjse_ime = "zzzzzzzzz"
        for ime in imena:
            if ime < najmanjse_ime:
                najmanjse_ime=ime
        imena.remove(najmanjse_ime)
        urejena.append(najmanjse_ime)
    return urejena
def vse_osebe(tviti):
    vsi = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return po_abecedi(vsi)
def custva(tviti, hashtagi):
    imena = []
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in tvit:
                imena.append(avtor(tvit))
    return po_abecedi(unikati(imena))
def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1 and oseba2 in vse_afne(tvit.split( )) or oseba2 == avtor(tvit) and oseba1 in vse_afne(tvit.split( )):
            return True
    return False














