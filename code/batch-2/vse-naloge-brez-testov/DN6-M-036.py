from collections import defaultdict

def se_zacne_z(tvit, znak):
    hestag = []
    text = tvit.split()
    for i in range(len(text)):
        if znak in text[i]:
            od_znak = text[i]
            beseda = ""
            for a in range(len(od_znak)):
                if od_znak[a].isalnum():
                    beseda += (od_znak[a])
                else:
                    pass
            hestag.append(beseda)
    return hestag

def avtor(tvit):
    tvit1 = tvit.split(":")
    ime = tvit1[0]
    return ime

def besedilo(tvit):
    besedilo = tvit.split(":", 1)
    return besedilo[1].strip()

def zadnji_tvit(tviti):
    slovar = {}
    for i in range(len(tviti)):
        besedilo = tviti[i].split(":", 1)
        avtor_tvita = avtor(tviti[i])
        tvit = besedilo[1].strip()
        slovar.update({avtor_tvita: tvit})           
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for i in range(len(tviti)):
        besedilo = tviti[i].split(":" ,1)
        avtor_tvita = avtor(tviti[i])
        tvit = besedilo[1].strip()
        if avtor_tvita in slovar:
            pass
        else:
            slovar.update({avtor_tvita: tvit})                  
    return slovar

def prestej_tvite(tviti):
    stevci = defaultdict(int)
    for i in range(len(tviti)):
        besedilo = tviti[i].split(":")
        avtor = besedilo[0]
        stevci[avtor] += 1
    return stevci

def omembe(tviti):
    slovar = {}
    for i in range(len(tviti)):
        afna = se_zacne_z(tviti[i], "@")
        avtor_tvita = avtor(tviti[i])
        if avtor_tvita in slovar:
            slovar[avtor_tvita] += afna
        else:
            slovar.update({avtor_tvita: afna})
    return slovar

def neomembe(ime, omembe):
    osebe = []
    osebe = list(omembe.keys())
    neomenjene_osebe = []
    omenjene_osebe =  omembe[ime]
    for i in range(len(osebe)):
        neomenjena_oseba = osebe[i]
        if neomenjena_oseba in omenjene_osebe or neomenjena_oseba == ime:
            pass
        else:
            neomenjene_osebe.append(neomenjena_oseba)
    return neomenjene_osebe

