
import re

def besedilo(tvit):
    return tvit.split(": ",1)[1]

def zadnji_tvit(tviti):
    avt_tvit = {}
    for tvit in tviti:
        t = tvit.split(": ",1)
        avt_tvit[t[0]] = t[1]
    return avt_tvit

def prvi_tvit(tviti):
    avt_tvit = {}
    for tvit in tviti:
        t = tvit.split(": ", 1)
        if t[0] not in avt_tvit:
           avt_tvit[t[0]] = t[1]
    return avt_tvit

def prestej_tvite(tviti):
    avt_tvit = {}
    for tvit in tviti:
        t = tvit.split(": ", 1)
        if t[0] not in avt_tvit:
           avt_tvit[t[0]] = 1
        else:
            avt_tvit[t[0]] += 1
    return avt_tvit

def izloci_besedo(beseda):
    return re.sub('^[^A-z0-9]*|[^A-z0-9]*$','',beseda)

def se_zacne_z(tvit, c):
    besede = tvit.split(" ")
    izlocene_besede = []
    for ele in besede:
        if ele[0] == c:
            izlocene_besede.append(izloci_besedo(ele))
    return izlocene_besede

def omembe(tviti):
    avt_tvit = {}
    for tvit in tviti:
        t = tvit.split(": ", 1)

        if t[0] not in avt_tvit:
            avt_tvit[t[0]] = se_zacne_z(tvit, "@")
        else:
            seznam = avt_tvit.get(t[0])
            seznam += se_zacne_z(tvit, "@")
            #avt_tvit[t[0]] = seznam
    return avt_tvit

def neomembe(ime, omembe):
    vsi_avt= list(omembe.keys())
    imena = []
    for k, v in omembe.items():
        if k == ime:
            imena = v
    ele = list(set(vsi_avt) - set(imena))
    ele.remove(ime)
    return ele

